#!/usr/bin/env python3
"""Turn the raw vial-sort files into the JSON the site reads. CPU only; network only for the HF API.

    ~/lerobot/.venv/bin/python scripts/build_data.py              # LEROBOT defaults to ~/lerobot
    ~/lerobot/.venv/bin/python scripts/build_data.py --offline    # HF answers from build/cache

Reads, never writes, the lerobot checkout:
  ee/eval_runs_v5.csv          the 79 human-scored v5 rollouts (the paper's evaluation)
  ee/robometer_runs.csv        run log of the same sessions: which capture belongs to which move
  outputs/*.log                pi0.5 and FLUX training logs
  outputs/rollout_reports/<day>/report.json   tools/assess_rollouts.py --json, one per rollout day
  outputs/*_rollouts/*/meta    the recordings themselves (for takes assess_rollouts cannot read)
  data/*/meta                  local datasets; the HF Hub API for the public ones
Writes src/data/*.json for the pages and build/clips.json for scripts/make_clips.py. Local paths
stay in build/, never in src/. Every number on the site comes from here; no page types one in.
"""

import argparse
import csv
import json
import math
import os
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import pandas as pd
import yaml

SITE = Path(__file__).resolve().parents[1]
LR = Path(os.environ.get("LEROBOT", Path.home() / "lerobot"))
sys.path.insert(0, str(LR / "tools"))
sys.path.insert(0, str(LR / "ee"))
from relabel_positions import parse_sheet  # noqa: E402
from vial_prompts import code, parse_move, place_code  # noqa: E402

OUT, BUILD = SITE / "src/data", SITE / "build"
HF_USER = "sari-abdan"
FPS = 30
SHORT_TAKE_S = 3  # same cut as tools/assess_rollouts.py: shorter takes ended before the policy moved

# The 79 scored rollouts start with task 1 (L1 -> R1) at 18:50 on Aug 22; earlier runs of the
# same moves in ee/robometer_runs.csv were warm-ups. Runs shorter than this were aborted.
EVAL_FROM, ABORTED_S = "2026-08-22T18:50", 20

# How far a take got, worst to best. v5 uses the report's four outcomes (ee/plot_eval_v5.py),
# the WS100 takes the four stages tools/assess_rollouts.py can read off the arm.
V5_STAGES = [("missed_pickup", "Missed the pickup"), ("wrong_target", "Wrong vial or slot"),
             ("missed_drop", "Missed the drop"), ("complete", "Complete")]
# How far a rollout got, worst to best. The last stage is success: the vial ended in the asked slot. A vial dropped
# in front of or behind the asked slot is a failure, like one put in another slot (the operator's rule, 24 Nov).
# Noted sessions take it from the notes; rollouts scored from the arm count the arm letting go at the asked slot,
# unless a person saw the vial was not in it (curation.yaml `checked`), which makes it "carried".
# The keys stay as they were ("released" is the success stage) so older data and code keep working.
WS_STAGES = [("no_grasp", "Never picked it up"), ("carried", "Picked up, not in the asked slot"),
             ("released", "In the asked slot")]
STAGE_DEF = {
    "no_grasp": "The arm never picked up the vial in the asked source slot: the gripper closed on another vial, on an "
                "empty hole or not at all, or closed on the right vial but never lifted it.",
    "carried": "The arm picked up the right vial, but it did not end in the asked slot: let go at another slot, dropped "
               "in front of or behind the asked slot, or never let go before the rollout ended.",
    "released": "The vial ended in the asked slot. With the operator's notes, that is what the operator saw. Scored from "
                "the arm, it is the arm letting go at the asked slot (within half a slot), unless a person saw the vial "
                "was not in it.",
}

# Every model the site describes lives in models.yaml. RUNS (the ones with a training log) and PROBES are
# views of it; the legacy "model" key ("pi05" | "flux") is what the colour tokens are named after.
FAMILY_KEY = {"pi05": "pi05", "flux3": "flux", "isaac": "isaac"}
CAMERAS = ["top_down", "left_top", "left_bottom", "right", "wrist"]


def load_models():
    return yaml.safe_load((SITE / "models.yaml").read_text())["models"]


def train_set_of(m):
    """The public training set a model learned from ('vial-sort-slots-220' / '-100'), from models.yaml `data`."""
    first = (m.get("data") or "").split(",")[0].strip()
    return first if first.startswith("vial-sort-slots-") else None


MODELS = load_models()
RUNS = [{"id": m["run"], "model": FAMILY_KEY[m["family"]], "name": m["name"], "recipe": m["what"], "dataset": m["data"],
         "logs": [tuple(x) for x in m["logs"]]} for m in MODELS if m.get("logs")]
PROBES = {m["run"]: m["name"] for m in MODELS if m.get("probe")}
# Model-table rows no log on this machine measures: what the report and the project notes record,
# each with its source. Runs in RUNS get their numbers from their logs instead.
NOTED = [
    {"id": "pi05-v5", "model": "pi05", "era": "paper", "name": "π0.5, frozen backbone",
     "trained": "Action expert only; vision-language backbone frozen", "data": "vial-sort-v5, 150 demos, 3 cameras",
     "steps": "30k (12k deployed)", "time": None, "memory": None, "robot": "eval", "source": "report"},
    {"id": "pi0", "model": "pi0", "era": "paper", "name": "π0",
     "trained": "Action expert, full fine-tune vs LoRA; backbone frozen", "data": "vial-sort-v1, 100 demos",
     "steps": "30k", "time": "about 5–6 h each", "memory": "same for both",
     "verdict": "Same training loss, but LoRA sometimes missed the grasp; full fine-tune grasped reliably. "
                "Only one fixed command was tried.", "source": "project notes (June 2026), report"},
    {"id": "groot", "model": "groot", "era": "paper", "name": "GR00T N1.5",
     "trained": "Fine-tune, batch 16", "data": "vial-sort-v4", "steps": "20k", "time": "3 h 58 min",
     "memory": "54.7 GB", "verdict": "Exploratory; not carried through to deployment.",
     "source": "project notes (July 2026), report"},
    {"id": "act", "model": "act", "era": "paper", "name": "ACT", "trained": None, "data": None, "steps": None,
     "time": None, "memory": None, "verdict": "No language input; a motion baseline only.", "source": "report"},
    {"id": "lingbot", "model": None, "era": "considered", "name": "LingBot-VA (world-action model)",
     "trained": "Not trained", "data": None, "steps": None, "time": None, "memory": None,
     "verdict": "5,230 ms per inference as published: far too slow for closed-loop control.",
     "source": "arXiv 2603.22078"},
    {"id": "molmoact2", "model": None, "era": "planned", "name": "MolmoAct2 (Allen Institute for AI)",
     "trained": "Not trained. Planned: fine-tune on the same 100 demonstrations and compare with π0.5 and FLUX",
     "data": "vial-sort-slots-100 (planned)", "steps": None, "time": None,
     "memory": "16.5 to 48.3 GiB, as documented",
     "verdict": "Of interest for depth reasoning from the colour images alone, since the RealSense cannot see the "
                "translucent vials. Already in LeRobot as policy.type=molmoact2; its depth-reasoning (Think) "
                "variant is not in that port yet. Memory is the authors' figure for fine-tuning the action expert "
                "only (batch 8) up to the full model, on an H100 with LIBERO, not measured here.",
     "source": "LeRobot docs/source/molmoact2.mdx, allenai.org/blog/molmoact2, ee/DEPTH_PLAN.md"},
]


def wilson(s, n, z=1.96):
    """95 % Wilson interval of s/n as fractions -- the same formula as ee/plot_eval_v5.py."""
    if not n:
        return 0.0, 0.0
    p, d = s / n, 1 + z * z / n
    c, h = (p + z * z / (2 * n)) / d, z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)


def move_code(move):
    """'R3->L3' / 'L4->bin', the site's key for a move (tools/vial_prompts.code without spaces)."""
    return code(move).replace(" ", "")


def write(name, obj):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.json").write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")
    print(f"  src/data/{name}.json")


# ── v5 evaluation ───────────────────────────────────────────────────────────────────────────────

def v5_stage(r):
    """The report's primary outcome (success > missed pickup > missed drop > other)."""
    if r["complete_success"]:
        return "complete"
    if r["missed_pickup"]:
        return "missed_pickup"
    if r["missed_drop"]:
        return "missed_drop"
    return "wrong_target"


def eval_captures():
    """{move: [run, ...]} for every full-length run of the scored sessions, oldest first."""
    runs = defaultdict(list)
    for r in list(csv.reader(open(LR / "ee/robometer_runs.csv")))[1:]:
        if r[0] < EVAL_FROM or not re.fullmatch(r"\d{8}-\d{6}", r[1]):
            continue
        rid, move = r[1], parse_move(r[2])
        video, series = LR / f"ee/robometer_runs/{rid}/video.mp4", LR / f"ee/robometer_runs/{rid}/series.json"
        if move is None or not video.exists():
            continue
        dur = json.loads(series.read_text()).get("duration", 0) if series.exists() else 0
        if dur >= ABORTED_S:
            runs[move_code(move)].append({"id": rid, "secs": round(dur, 1), "video": str(video)})
    return runs


def evals(clips):
    flags = ("trained_source", "missed_drop", "missed_pickup", "collision", "complete_success")
    rows = [{k: (int(v) if k in flags else v) for k, v in r.items()} for r in csv.DictReader(open(LR / "ee/eval_runs_v5.csv"))]
    caps = eval_captures()
    scen, trials = [], []
    for task in sorted({int(r["task"]) for r in rows}):
        rs = [r for r in rows if int(r["task"]) == task]
        mv = rs[0]["prompt"]
        runs = caps.get(mv, [])
        # one capture per trial only when the session has exactly one full run per scored trial
        matched = len(runs) == len(rs)
        n, s = len(rs), sum(r["complete_success"] for r in rs)
        lo, hi = wilson(s, n)
        st = Counter(v5_stage(r) for r in rs)
        for i, r in enumerate(rs):
            trials.append({"task": task, "i": i, "move": mv, "stage": v5_stage(r), "collision": bool(r["collision"]),
                           "missed_pickup": bool(r["missed_pickup"]), "missed_drop": bool(r["missed_drop"]),
                           "note": r["note"], "capture": runs[i]["id"] if matched else None})
        for c in runs:
            clips.append({"id": f"v5-{c['id']}", "kind": "capture", "src": c["video"]})
        scen.append({"task": task, "move": mv, "src": rs[0]["source"], "dst": rs[0]["dest"],
                     "trained": bool(rs[0]["trained_source"]), "n": n, "complete": s, "rate": round(s / n, 4),
                     "lo": lo, "hi": hi, "stages": {k: st[k] for k, _ in V5_STAGES},
                     "collision": sum(r["collision"] for r in rs),
                     "captures": [{"id": c["id"], "secs": c["secs"]} for c in runs], "matched": matched})
    n = len(rows)
    first = [r for r in rows if not r["missed_pickup"]]
    group = lambda rs: {"rollouts": len(rs), "complete": sum(r["complete_success"] for r in rs),
                        "scenarios": len({r["task"] for r in rs}),
                        **dict(zip(("lo", "hi"), wilson(sum(r["complete_success"] for r in rs), len(rs))))}
    kpi = {
        "rollouts": n, "scenarios": len(scen),
        "complete": sum(r["complete_success"] for r in rows),
        "wrong_target": sum(v5_stage(r) == "wrong_target" for r in rows),
        "missed_first_grasp": sum(r["missed_pickup"] for r in rows),
        "first_grasp": len(first),
        "complete_after_first_grasp": sum(r["complete_success"] for r in first),
        "released_away": sum(r["missed_drop"] for r in first),
        "recovered": sum(r["missed_pickup"] and r["complete_success"] for r in rows),
        "collision": sum(r["collision"] for r in rows),
        "missed_drop": sum(r["missed_drop"] for r in rows),
    }
    write("evals", {"source": "v5 evaluation: π0.5 (frozen vision-language backbone) at 12k steps, "
                              "79 rollouts scored by a person, 22–24 Aug 2026",
                    "stages": [{"key": k, "label": lab} for k, lab in V5_STAGES], "kpi": kpi,
                    "trained": group([r for r in rows if r["trained_source"]]),
                    "held_out": group([r for r in rows if not r["trained_source"]]),
                    "scenarios": scen, "trials": trials})
    return scen, kpi


# ── training logs ───────────────────────────────────────────────────────────────────────────────

REC_PLAIN = re.compile(r"INFO (\S+ \S+) \S+ step:\S+ .*?loss:([\d.]+) grdn:([\d.]+) lr:(\S+) .*?step_s:([\d.]+) .*?mem_gb:([\d.]+)")
REC = re.compile(r"(\d+)/\d+ \[[^\]]*\]INFO (\S+ \S+) \S+ step:\S+ .*?loss:([\d.]+) grdn:([\d.]+) lr:(\S+) "
                 r".*?step_s:([\d.]+) .*?mem_gb:([\d.]+)(?: video_mse:([\d.]+) action_mse:([\d.]+))?")


FLOW_LOSS = re.compile(r"flow_loss:([\d.]+)")


def parse_log(path, first, flow=False):
    """[{step, t, loss, ...}] of one log; the step is the tqdm count plus where the run resumed. flow=True (Isaac) takes
    the action expert's flow loss as the loss: Isaac's `loss` also holds the frozen language model's text losses, which
    stay near 5 because nothing trains them."""
    out = []
    text = path.read_bytes().decode("utf-8", "replace").replace("\r", "\n")
    if path.suffix == ".out":           # Slurm log of a cluster job: lerobot turns tqdm off there
        for k, m in enumerate(REC_PLAIN.finditer(text)):
            ts, loss, gn, lr, ss, mem = m.groups()
            out.append({"step": first + 100 * (k + 1), "t": datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"),
                        "loss": float(loss), "grad_norm": float(gn), "lr": float(lr), "step_s": float(ss),
                        "mem_gb": float(mem)})
        return out
    for chunk in text.split("\n"):
        m = REC.search(chunk)
        if m:
            n, ts, loss, gn, lr, ss, mem, vid, act = m.groups()
            if flow:
                f = FLOW_LOSS.search(chunk)
                if not f:
                    continue
                loss = f.group(1)
            out.append({"step": first + int(n), "t": datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"),
                        "loss": float(loss), "grad_norm": float(gn), "lr": float(lr), "step_s": float(ss),
                        "mem_gb": float(mem), **({"action_mse": float(act), "video_mse": float(vid)} if act else {})})
    return out


def training(robot):
    runs = []
    for spec in RUNS:
        recs, wall = [], 0.0
        for name, first in spec["logs"]:
            rs = parse_log(LR / "outputs" / name, first, flow=spec["model"] == "isaac")
            if rs:
                wall += (rs[-1]["t"] - rs[0]["t"]).total_seconds() + rs[0]["step_s"] * (rs[0]["step"] - first)
            recs += rs
        recs.sort(key=lambda r: r["step"])
        # FLUX logs every 20 steps, pi0.5 every 100: plot both as 100-step means
        bins = defaultdict(list)
        for r in recs:
            bins[math.ceil(r["step"] / 100) * 100].append(r)
        keys = [k for k in ("loss", "grad_norm", "action_mse") if k in recs[0]]
        points = [{"step": s, **{k: round(sum(r[k] for r in b) / len(b), 5) for k in keys}} for s, b in sorted(bins.items())]
        ss = sorted(r["step_s"] for r in recs)
        runs.append({k: spec[k] for k in ("id", "model", "name", "recipe", "dataset")} | {
            "steps": recs[-1]["step"], "hours": round(wall / 3600, 1), "step_s": round(ss[len(ss) // 2], 2),
            "mem_gb": round(max(r["mem_gb"] for r in recs), 1), "metric": "loss", "points": points,
            "robot": robot.get(spec["id"], [])})
    probes = [{"id": k, "name": v, "robot": robot.get(k, [])} for k, v in PROBES.items()]
    write("training", {"runs": runs, "probes": probes})
    return runs


def robot_summary(rows):
    """Plain-language tally of a run's assessed takes (trained moves, takes over 3 s)."""
    st = Counter()
    for r in rows:
        st.update(r["stages"])
    n = sum(st.values())
    if not n:
        return None
    return {"takes": n, "released": st["released"], "right_vial": n - st["no_grasp"], "stages": dict(st)}


def models(runs, kpi):
    rows = []
    for m in NOTED:
        row = dict(m)
        if m.get("robot") == "eval":
            row["robot"] = {"rollouts": kpi["rollouts"], "complete": kpi["complete"]}
            row["verdict"] = "Deployed and evaluated: the system in the report."
        rows.append(row)
    flux_hz = 15.46  # cadence summary of the 2026-10-16 FLUX session (30 Hz target), see the FLUX notes
    for r in runs:
        tally = robot_summary(r["robot"])
        rows.append({"id": r["id"], "model": r["model"], "era": "after", "name": r["name"], "trained": r["recipe"],
                     "data": r["dataset"], "steps": f"{r['steps'] // 1000}k", "time": f"{r['hours']} h",
                     "memory": f"{r['mem_gb']} GB", "step_s": r["step_s"], "robot": tally,
                     "rate_hz": flux_hz if r["id"] == "flux-ws100" else None,
                     "verdict": None if tally else "Rollouts not scored: an earlier scene layout.",
                     "source": "training log"})
    write("models", {"rows": rows})


# ── the October (WS100) work ────────────────────────────────────────────────────────────────────

FUNNEL = [("rollouts", "Rollouts"), ("grasped_right", "Picked up the right vial"), ("released", "In the asked slot")]
GATE = re.compile(r"step (\d+) \| SOURCE:(\w+) ROLES:(\w+) DEST:(\w+) \| source pan ([^|]+)\| dest (\d+)/(\d+) \| "
                  r"go rows (\d+)/(\d+): (\d+)/(\d+) \| insertion err ([\d.]+) deg, gripper err ([\d.]+)")


def gate():
    """One line per checkpoint of the canonical-prompt run's offline gate (tools/pi05/probe_*.py):
    does it leave home, order the source reaches, bind the digits to roles, and read the destination."""
    path = LR / "outputs/pi05_full_vial-sort-ws100_canon_base12k/gate/summary.txt"
    rows = []
    for line in path.read_text().splitlines():
        m = GATE.search(line)
        if m:
            step, src, roles, dst, pan, ok, of, _a, _b, go_ok, go_of, ins, grip = m.groups()
            rows.append({"step": int(step), "source": src.lower() == "pass", "roles": roles.lower() == "pass",
                         "dest": dst.lower() == "pass", "dest_frames": int(ok), "dest_of": int(of),
                         "go_ok": int(go_ok), "go_of": int(go_of),  # test frames where every seed leaves home
                         "pan": {k: int(v) for k, v in re.findall(r"(\d):([+-]\d+)", pan)},
                         "insertion_err": float(ins), "gripper_err": float(grip)})
    write("gate", {"run": "pi05-canon", "recorded_pan": {"1": 36, "3": 21, "6": 3}, "checkpoints": rows})
    return rows


def ws100_coverage():
    """The 100 demonstrations the October runs trained on: how many per move, source and destination,
    and the wording pools the labels were drawn from (imported, not retyped)."""
    import relabel_positions as rp
    sheet = parse_sheet(LR / "ee/SORT_SHEET_WS.txt")
    demos = Counter(f"{place_code(s)}->{place_code(d)}" for s, d in sheet.values())
    src, dst = Counter(), Counter()
    for mv, n in demos.items():
        a, b = mv.split("->")
        src[a] += n
        dst[b] += n
    info = json.loads((LR / "data/vial-sort-ws100/meta/info.json").read_text())
    trim = json.loads((LR / "data/vial-sort-ws100_trim/meta/info.json").read_text())
    tasks = pd.read_parquet(LR / "data/vial-sort-ws100/meta/tasks.parquet")
    per_move = Counter(move_code(parse_move(t)) for t in tasks.index)
    slots = [f"{r}{n}" for r in "LR" for n in range(1, 7)]
    return {"dataset": "vial-sort-slots-100", "episodes": info["total_episodes"], "frames": info["total_frames"],
            "fps": info["fps"], "minutes": round(info["total_frames"] / info["fps"] / 60),
            "trim_frames": trim["total_frames"],
            "cameras": [k.split(".")[-1] for k in info["features"] if k.startswith("observation.images")],
            "slots": slots,
            "heldout_sources": [s for s in slots if int(s[1]) in (2, 5)],
            "heldout_destinations": [s for s in slots if int(s[1]) in (2, 4, 5)],
            "demos": dict(sorted(demos.items())), "per_source": dict(sorted(src.items())),
            "per_destination": dict(sorted(dst.items())),
            "wordings": {"distinct": len(tasks), "moves": len(demos), "max_per_move": max(per_move.values()),
                         "example_move": "R3->L6",
                         "example": sorted(t for t in tasks.index if move_code(parse_move(t)) == "R3->L6")},
            "pools": {"verb": rp.VERBS, "object": rp.OBJECTS,
                      "slot": {str(k): v for k, v in rp.POS_PHRASES.items()},
                      "slot_count": len(rp.POS_PHRASES[1]), "rack": dict(rp.RACK_PHRASES),
                      "bin": rp.BIN_PHRASES,
                      "template": ["… from S to D", "… in S to D", "… from S over to D", "… at S to / into D"]}}


# ── hyperparameters, read from each model's saved train_config.json ───────────────────────────────

def _g(c, *path, default=None):
    for k in path:
        if not isinstance(c, dict) or k not in c:
            return default
        c = c[k]
    return c


def _num(x):
    return f"{x:,}" if isinstance(x, int) else f"{x:g}"


def hyper_pi05(c, m, steps):
    p, b = c["policy"], c["batch_size"]
    warm, decay = _g(c, "scheduler", "num_warmup_steps"), _g(c, "scheduler", "num_decay_steps")
    set_warm, set_decay = warm, decay
    scaled = steps < decay  # lerobot shrinks the schedule to fit a shorter run
    if scaled:
        warm, decay = int(warm * steps / decay), steps
    tf = _g(c, "dataset", "image_transforms", "tfs", default={})
    aug = (f"colour jitter (brightness ±20%, contrast ±20%, saturation ±50%, hue ±0.05), sharpness, and a small shift and "
           f"rotation (≤5% and ±5°); up to {_g(c, 'dataset', 'image_transforms', 'max_num_transforms')} applied to each image"
           if tf else "none")
    return [
        {"group": "What trains", "rows": [
            ["Starting weights", m["base"], "The checkpoint training began from."],
            ["Parameters trained", "All of them" if not p["freeze_vision_encoder"] and not p["train_expert_only"] else "Part",
             "Vision encoder, language model and action expert all receive gradients: a full fine-tune, no LoRA."],
            ["Precision", p["dtype"] + (", gradient checkpointing" if p["gradient_checkpointing"] else ""),
             "Number format of the weights and activations; checkpointing trades speed for memory."]]},
        {"group": "Optimiser", "rows": [
            ["Optimiser", "AdamW", "The update rule."],
            ["Peak learning rate", _num(p["optimizer_lr"]), "The step size at its largest."],
            ["Betas", ", ".join(_num(x) for x in p["optimizer_betas"]), "How strongly AdamW remembers past gradients."],
            ["Weight decay", _num(p["optimizer_weight_decay"]), "A pull of the weights toward zero."],
            ["Gradient clipping", _num(p["optimizer_grad_clip_norm"]), "Largest allowed size of one update's gradient."]]},
        {"group": "Learning-rate schedule", "rows": [
            ["Shape", "Linear warm-up, then cosine decay", "The learning rate rises, then falls smoothly."],
            ["Warm-up steps", _num(warm) + (f" (set to {_num(set_warm)}, scaled to fit the run)" if scaled else ""),
             "Steps over which the rate rises to its peak."],
            ["Decay steps", _num(decay) + (f" (set to {_num(set_decay)}, scaled to fit the run)" if scaled else ""),
             "Steps over which it falls to the final rate."],
            ["Final learning rate", _num(_g(c, "scheduler", "decay_lr")), "The rate at the end of the decay."]]},
        {"group": "Batches and length", "rows": [
            ["Batch size", _num(b), "Frames per optimiser step."],
            ["Steps", _num(steps), "Optimiser steps. Checkpoints were saved every " + _num(c["save_freq"]) + "."],
            ["Passes over the data", f"{steps * b / m['frames']:.2f}", "Steps × batch size ÷ frames in the training data."],
            ["Validation split", "none", "Every demonstration is used for training, so the loss cannot show when the model starts to memorise."]]},
        {"group": "What it sees and predicts", "rows": [
            ["Cameras", ", ".join(m["cams"]) or "–", "The views fed to the model at every step."],
            ["Image size", " × ".join(str(x) for x in p["image_resolution"]), "Each camera image is resized to this many pixels."],
            ["Prompt length", f"{p['tokenizer_max_length']} tokens", "Longest command the text tokenizer keeps."],
            ["Action chunk", f"{p['chunk_size']} actions", "How many future joint targets one forward pass predicts (1.7 s at 30 Hz)."],
            ["Denoising steps", _num(p["num_inference_steps"]), "Steps the action expert takes to turn noise into a chunk when running."],
            ["Normalisation", "state and action by quantiles; images unchanged",
             "Joint values are rescaled with the 1st and 99th percentile of this data set, so its own joint ranges are used."]]},
        {"group": "Image augmentation", "rows": [["Augmentation", aug, "Random changes to each training image."]]},
        {"group": "Reproducibility", "rows": [["Seed", _num(c["seed"]), "Fixes the random choices."]]},
    ]


def hyper_flux(c, m, steps):
    p, b = c["policy"], c["batch_size"]
    acc = _g(c, "accelerator", "gradient_accumulation", "steps", default=1)
    peft = c.get("peft") or {}
    return [
        {"group": "What trains", "rows": [
            ["Starting weights", m["base"], "The checkpoint training began from; the joint ranges built into it were replaced by this data set's own."],
            ["Method", f"LoRA, rank {peft.get('r')}, alpha {peft.get('lora_alpha')}",
             "Small low-rank adapters are trained on the attention and feed-forward layers; the 7-billion-parameter base stays frozen. About 137 million parameters train."],
            ["Action layers", "trained in full", "The layers that read and write joint values are not adapted, they are trained directly."],
            ["Precision", p["dtype"] + (", gradient checkpointing" if p["gradient_checkpointing"] else ""),
             "Number format of the weights and activations; checkpointing trades speed for memory."]]},
        {"group": "Optimiser", "rows": [
            ["Optimiser", "AdamW", "The update rule."],
            ["Learning rate", f"{_num(p['optimizer_lr'])} (adapters), {_num(p['optimizer_lr'] * p['optimizer_lr_heads_multiplier'])} (action layers)",
             "The step size; the action layers learn five times faster."],
            ["Schedule", "constant", "No warm-up and no decay, so every checkpoint is a finished model."],
            ["Betas", ", ".join(_num(x) for x in p["optimizer_betas"]), "How strongly AdamW remembers past gradients."],
            ["Weight decay", _num(p["optimizer_weight_decay"]), "A pull of the weights toward zero."],
            ["Gradient clipping", _num(p["optimizer_grad_clip_norm"]), "Largest allowed size of one update's gradient."],
            ["EMA of the weights", f"decay {_num(_g(c, 'ema', 'decay'))}", "A slowly moving average of the weights, saved beside the raw ones. Rollouts were run with both."]]},
        {"group": "Batches and length", "rows": [
            ["Batch size", f"{b} × {acc} accumulation = {b * acc}", "Frames per optimiser update: 4 per step, 4 steps added up before each update."],
            ["Steps", _num(steps), f"Steps of {b} frames, so {_num(steps // acc)} updates. Checkpoints were saved every {_num(c['save_freq'])}."],
            ["Passes over the data", f"{steps * b / m['frames']:.2f}", "Steps × frames per step ÷ frames in the training data."],
            ["Validation split", "none", "Every demonstration is used for training."]]},
        {"group": "What it sees and predicts", "rows": [
            ["Cameras", ", ".join(m["cams"]) or m.get("cams_note", "–"), "The two views are placed side by side on one canvas."],
            ["Canvas", f"{p['canvas_hw'][0]} × {p['canvas_hw'][1]} pixels", "Each camera is 256 × 256; the picture is divided into 8 × 8 cells."],
            ["Past observations", f"{p['n_obs_steps']} frames, {p['history_snapshots']} history snapshots", "How much recent past the model sees."],
            ["Action chunk", f"{p['chunk_size']} predicted, {p['n_action_steps']} executed", "Joint targets per forward pass, and how many are run before it replans."],
            ["Denoising steps", f"{p['num_inference_steps']}, guidance {_num(p['guidance_scale'])}", "Steps to turn noise into a chunk; guidance strengthens the pull toward the prompt. Each replan costs 8 passes of the 7B model."],
            ["Loss weights", f"video {_num(p['video_loss_weight'])}, action {_num(p['action_loss_weight'])}, gripper channel ×{_num(p['action_channel_weights'][-1])}",
             "FLUX learns to predict future video as well as actions."],
            ["Prompt dropout", _num(p["caption_dropout"]), "Share of training samples shown without their prompt."],
            ["Actions", p["action_representation"] + " joint targets", "Each action is the change from the current joint position."],
            ["Normalisation", "built into the base", "The base was rebuilt with this data set's 1st and 99th percentiles."]]},
        {"group": "Reproducibility", "rows": [["Seed", _num(c["seed"]), "Fixes the random choices."]]},
    ]


def hyper_isaac(c, m, steps):
    """Isaac 0.5 fine-tuned with only its action expert training. The saved config says train_expert_only false: the
    expert-only switch is ~/lerobot/tools/isaac/finetune.py (ISAAC_TRAIN=expert), outside the config."""
    p, b, s = c["policy"], c["batch_size"], c.get("scheduler") or {}
    peak = p["optimizer_action_expert_lr"]
    final = peak * s["decay_lr"] / s["peak_lr"] if s.get("peak_lr") else None
    tf = _g(c, "dataset", "image_transforms", "tfs", default={})
    aug = (f"colour jitter (brightness ±20%, contrast ±20%, saturation ±50%, hue ±0.05), sharpness, and a small shift and "
           f"rotation (≤5% and ±5°); up to {_g(c, 'dataset', 'image_transforms', 'max_num_transforms')} applied to each image"
           if tf else "none")
    slot = {v.split(".")[-1]: k.split(".")[-1] for k, v in (c.get("rename_map") or {}).items()}
    return [
        {"group": "What trains", "rows": [
            ["Starting weights", m["base"], "Perceptron's Isaac 0.5, already fine-tuned by them on SO-100 and SO-101 arms."],
            ["Parameters trained", "The action expert only",
             "About 0.58 billion of the model's 36 billion parameters receive gradients: the part that turns what the model "
             "sees into joint targets. The vision encoder and the language model stay as Perceptron released them."],
            ["Precision", p["dtype"] + (", the trained part kept in 32-bit floats" if p.get("train_storage_fp32") else ""),
             "Number format of the computation, and of the weights that train."]]},
        {"group": "Optimiser", "rows": [
            ["Optimiser", "AdamW", "The update rule."],
            ["Peak learning rate", _num(peak), "The step size at its largest, for the action expert."],
            ["Betas", ", ".join(_num(x) for x in c["optimizer"]["betas"]), "How strongly AdamW remembers past gradients."],
            ["Weight decay", _num(p["optimizer_weight_decay"]), "A pull of the weights toward zero."],
            ["Gradient clipping", _num(p["optimizer_grad_clip_norm"]), "Largest allowed size of one update's gradient."]]},
        {"group": "Learning-rate schedule", "rows": [
            ["Shape", "Linear warm-up, then cosine decay", "The learning rate rises, then falls smoothly."],
            ["Warm-up steps", _num(p["optimizer_warmup_steps"]), "Steps over which the rate rises to its peak."],
            ["Decay steps", _num(s.get("num_decay_steps")), "Steps over which it falls to the final rate."],
            ["Final learning rate", _num(float(f"{final:.3g}")) if final else "–", "The rate at the end of the decay: a tenth of the peak."]]},
        {"group": "Batches and length", "rows": [
            ["Batch size", _num(b), "Frames per optimiser step."],
            ["Steps", _num(steps), "Optimiser steps. Checkpoints were saved every " + _num(c["save_freq"]) + "."],
            ["Passes over the data", f"{steps * b / m['frames']:.2f}", "Steps × batch size ÷ frames in the training data."],
            ["Validation split", "8 demonstrations held out",
             "They were left out of training and scored offline: the predicted next second against what the demonstration did."]]},
        {"group": "What it sees and predicts", "rows": [
            ["Cameras", ", ".join(f"{cam} (its '{slot[cam]}' slot)" if cam in slot else cam for cam in m["cams"]) or "–",
             "The checkpoint has exactly two camera slots, so it sees two of the five cameras."],
            ["Image size", " × ".join(str(x) for x in p["image_size"]), "Each camera image is resized to this many pixels."],
            ["Action chunk", f"{p['chunk_size']} actions", "Future joint targets one forward pass predicts (2 s at 30 Hz); "
             "on the arm the first 30 run before it plans again."],
            ["Denoising steps", _num(p["num_inference_steps"]), "Steps the action expert takes to turn noise into a chunk when running."],
            ["Clock", "seconds since the start", "Each prediction is also told how long the rollout has been running."],
            ["Normalisation", "state and action by quantiles, Isaac's ranges widened to fit",
             "The checkpoint's own 1st and 99th percentiles are kept, widened only where this data reaches further, so the "
             "joint values mean what they meant to it before."]]},
        {"group": "Image augmentation", "rows": [["Augmentation", aug, "Random changes to each training image."]]},
        {"group": "Reproducibility", "rows": [["Seed", _num(c["seed"]), "Fixes the random choices."]]},
    ]


HYPER = {"pi05": hyper_pi05, "flux3": hyper_flux, "isaac": hyper_isaac}


def config_of(m):
    cfg = LR / "outputs" / m["config"] if m.get("config") else None
    return json.loads(cfg.read_text()) if cfg and cfg.exists() else None


def hyper_of(m, steps):
    c = config_of(m)
    if c:
        return HYPER[m["family"]](c, m, steps), "the train_config.json saved with the checkpoint"
    rows = [[a, b, c_] for a, b, c_ in m.get("manual", [])]
    return ([{"group": "Recipe", "rows": rows}] if rows else []), "the project notes (the checkpoint and its config were deleted)"


# ── the October models: registry, per-checkpoint results, per-model move tables ───────────────────

MODE_NAME = {"rtc": "RTC", "sync": "sync"}


def kstep(n):
    return f"{n // 1000}k" if n >= 1000 and n % 1000 == 0 else str(n)


def new_tally():
    return {"rollouts": 0, "grasped_right": 0, "lifted": 0, "released": 0, "seen_in_slot": 0, "stages": Counter()}


def tally(t, take):
    st = take["stage"]
    t["rollouts"] += 1
    t["grasped_right"] += st != "no_grasp"
    t["lifted"] += st in ("carried", "released")
    t["released"] += st == "released"
    t["seen_in_slot"] += (take["checked"] or {}).get("vial") == "in_slot"
    t["stages"][st] += 1


def freeze(t):
    return {**{k: v for k, v in t.items() if k != "stages"}, "stages": {k: t["stages"][k] for k, _ in WS_STAGES}}


def october(gate_rows, runs_json):
    """Registry (one entry per model), results (one row per model + checkpoint + mode), and per-model
    experiments (hyperparameters, checkpoint rows, move tables). Scored rollouts are every rollout over 3 s
    with a readable command (the cuts tools/assess_rollouts.py makes), moves the model never trained on
    included: n is the total, and each row also says how many were on untrained moves. A session with
    operator's notes counts each noted move once, scored from the note (rollouts()); its restarts are left
    out, counted as such."""
    sessions = json.loads((OUT / "rollouts.json").read_text())["sessions"]
    by_run = {m["run"]: m for m in MODELS}
    cov = ws100_coverage()
    rows, left_out = {}, defaultdict(Counter)
    untr = defaultdict(lambda: {"total": new_tally(), "moves": Counter()})  # the part of a row on untrained moves
    scored_by, restarts, noted = defaultdict(Counter), Counter(), defaultdict(list)
    demos_of = lambda run, mv: (demos_in(run) if run in WS220_RUNS or run in WS212_RUNS else cov["demos"]).get(mv, 0)
    for s in sessions:
        m = by_run.get(s["run"])
        if m is None:
            continue
        key = (m["id"], s["step"], s["mode"], s["ema"])
        for t in s["takes"]:
            nt = t.get("noted")
            if t.get("restart"):
                left_out[m["id"]]["restart"] += 1
                restarts[key] += 1
                continue
            if nt:  # every noted move, trained or not, in the operator's order, for the move table
                noted[key].append({"n": nt["n"], "move": t["move"], "trained": t["trained_move"],
                                   "demos": demos_of(m["run"], t["move"]), "outcome": nt["outcome"], "stage": t["stage"],
                                   "ended": nt["ended"], "retried": nt["retried"], "attempts": nt["attempts"],
                                   "note": nt["note"], "take": t["id"], "_order": (nt["file"], nt["i"])})
            if t["short"] and not nt:
                left_out[m["id"]]["short"] += 1
            elif m.get("scored") is False:
                left_out[m["id"]]["earlier_scene"] += 1  # 7 Oct, before the racks moved: the assessment cannot read it
            elif not t["move"]:
                left_out[m["id"]]["unreadable"] += 1
            else:
                if not t["trained_move"]:  # in n like the rest; counted apart too, for the pages to say how many
                    tally(untr[key]["total"], t)
                    untr[key]["moves"][t["move"]] += 1
                scored_by[key]["notes" if nt else "arm"] += 1
                r = rows.setdefault(key, {"total": new_tally(), "moves": defaultdict(new_tally), "src": defaultdict(new_tally),
                                          "dst": defaultdict(new_tally), "sessions": [], "days": set()})
                a, b = t["move"].split("->")
                for tl in (r["total"], r["moves"][t["move"]], r["src"][a], r["dst"][b]):
                    tally(tl, t)
                if s["name"] not in r["sessions"]:
                    r["sessions"].append(s["name"])
                r["days"].add(s["day"])
    pick = lambda d: {k: {x: v[x] for x in ("rollouts", "grasped_right", "released")} for k, v in sorted(d.items())}
    results, per_model = [], defaultdict(list)
    for (mid, step, mode, ema), r in sorted(rows.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2], kv[0][3])):
        m = next(x for x in MODELS if x["id"] == mid)
        by = scored_by[(mid, step, mode, ema)]
        if by["notes"] and by["arm"]:
            sys.exit(f"{mid} at {step} ({mode}): {by['notes']} rollouts scored from notes and {by['arm']} from the arm in one "
                     f"row. Note the other sessions too (scripts/notes_to_yaml.py), or none of them.")
        tag = f"{kstep(step)} · {MODE_NAME.get(mode, 'mode unknown')}{' · EMA' if ema else ''}"
        row = {"key": f"{mid}-{step}-{mode}{'-ema' if ema else ''}", "model": mid, "name": m["name"], "family": FAMILY_KEY[m["family"]],
               "step": step, "mode": mode, "ema": ema, "label": f"{m['name']} · {tag}", "short": tag,
               **freeze(r["total"]), "days": sorted(r["days"]), "sessions": r["sessions"],
               "by_source": pick(r["src"]), "by_destination": pick(r["dst"]),
               "untrained": ({**freeze(untr[(mid, step, mode, ema)]["total"]),
                              "moves": dict(sorted(untr[(mid, step, mode, ema)]["moves"].items()))}
                             if (mid, step, mode, ema) in untr else None),
               "scored_by": "notes" if by["notes"] else "arm", "restarts": restarts[(mid, step, mode, ema)],
               "train_set": train_set_of(m),
               "noted_moves": [{k: v for k, v in x.items() if k != "_order"}
                               for x in sorted(noted[(mid, step, mode, ema)], key=lambda x: x["_order"])] or None,
               "moves": [{"move": mv, "demos": demos_of(m["run"], mv), **freeze(t)}
                         for mv, t in sorted(r["moves"].items(), key=lambda kv: (-kv[1]["rollouts"], kv[0]))]}
        results.append(row)
        per_model[mid].append(row)

    reg = []
    runs_by_id = {r["id"]: r for r in runs_json}
    for m in MODELS:
        tr = runs_by_id.get(m["run"])
        steps = (tr or {}).get("steps") or m.get("steps")
        hyp, hyp_src = hyper_of(m, steps) if steps else ([], "")
        c = config_of(m)
        last_day = max((d for r in per_model[m["id"]] for d in r["days"]), default=None)
        reg.append({
            "id": m["id"], "name": m["name"], "family": m["family"], "model": FAMILY_KEY[m["family"]], "run": m["run"],
            "what": m["what"], "base": m["base"], "data": m["data"], "frames": m["frames"], "cams": m["cams"],
            "cams_note": m.get("cams_note"), "hub": m.get("hub"), "probe": bool(m.get("probe")), "scored": m.get("scored") is not False,
            "steps": steps, "hours": (tr or {}).get("hours"), "step_s": (tr or {}).get("step_s"),
            "mem_gb": (tr or {}).get("mem_gb"),
            "passes": round(steps * c["batch_size"] / m["frames"], 2) if steps and c else None,
            "has_loss": bool(tr), "notes": m.get("notes", []), "camera_choice": m.get("camera_choice"),
            "hyper": hyp, "hyper_source": hyp_src, "left_out": dict(left_out[m["id"]]),
            "last_day": last_day, "rows": [r["key"] for r in per_model[m["id"]]],
            "rollouts": sum(r["rollouts"] for r in per_model[m["id"]]),
            "checkpoints": sorted({r["step"] for r in per_model[m["id"]]})})
    # the model each family's headline uses: its newest model with scored rollouts, and that model's
    # highest-step sync row on raw weights (RTC never lifted the vial with these checkpoints, EMA is a variant)
    heads = {}
    for fam in ("pi05", "flux", "isaac"):
        cands = [m for m in reg if m["model"] == fam and m["rollouts"] and not m["probe"]]
        if cands:
            newest = max(cands, key=lambda m: m["last_day"])
            rs = [r for r in results if r["model"] == newest["id"]]
            plain = [r for r in rs if r["mode"] == "sync" and not r["ema"]] or rs
            heads[fam] = max(plain, key=lambda r: r["step"])["key"]
    # the eye checks: only some rollouts were watched, so this is a caveat on the last stage, not a stage. Rollouts
    # scored from the operator's notes are left out: there the note is the score, not a check beside it.
    eye = Counter()
    for s_ in sessions:
        for t in s_["takes"]:
            v = (t["checked"] or {}).get("vial")
            if v and not t.get("noted"):
                eye[v] += 1
                eye["checked"] += 1
    byk = {r["key"]: r for r in results}
    tiles = {fam: {"key": k, "name": byk[k]["name"], "label": byk[k]["label"], "short": byk[k]["short"], "rollouts": byk[k]["rollouts"],
                   "grasped_right": byk[k]["grasped_right"], "released": byk[k]["released"], "scored_by": byk[k]["scored_by"]}
             for fam, k in heads.items()}
    tiles["gate"] = {"checkpoints": len(gate_rows), "dest_passed": sum(g["dest"] for g in gate_rows),
                     "dest_frames": gate_rows[-1]["dest_of"], "source_passed": sum(g["source"] for g in gate_rows),
                     "source_from": next(g["step"] for g in gate_rows if all(h["source"] for h in gate_rows if h["step"] >= g["step"]))}
    stages = [{"key": k, "label": lab, "def": STAGE_DEF[k]} for k, lab in WS_STAGES]
    write("registry", {"models": [{k: v for k, v in m.items() if k not in ("hyper", "notes", "camera_choice")} for m in reg],
                       "cameras": CAMERAS})
    write("experiments", {"models": reg, "stages": stages, "rows": results})
    write("results", {"stages": stages, "funnel": [{"key": k, "label": lab} for k, lab in FUNNEL],
                      "rows": [{k: v for k, v in r.items() if k not in ("moves", "noted_moves")} for r in results],
                      "noted_models": [m["name"] for m in MODELS if any(r["model"] == m["id"] and r["scored_by"] == "notes"
                                                                       for r in results)],
                      "defaults": list(heads.values()), "eye": dict(eye), "tiles": tiles,
                      "total": sum(r["rollouts"] for r in results),
                      "untrained": sum((r["untrained"] or {}).get("rollouts", 0) for r in results),
                      "demo_sets": demo_sets(cov),
                      "left_out": {k: sum(v[k] for v in left_out.values()) for k in ("short", "unreadable", "earlier_scene", "restart")}})
    write("october", {"stages": stages, "coverage": cov, "tiles": tiles, "eye": dict(eye)})
    pick_featured(sessions, results)


def demo_sets(cov):
    """Demonstrations per slot of each training set, by its public name: what the Results page draws beside a row."""
    w = json.loads((OUT / "ws220.json").read_text())
    per_src, per_dst = Counter(), Counter()
    for mv, n in ws212_demos().items():
        a, b = mv.split("->")
        per_src[a] += n
        per_dst[b] += n
    return {"vial-sort-slots-220": {"episodes": w["episodes"], "per_source": w["per_source"], "per_destination": w["per_destination"]},
            WS212_SET: {"episodes": sum(ws212_demos().values()), "per_source": dict(sorted(per_src.items())),
                        "per_destination": dict(sorted(per_dst.items()))},
            "vial-sort-slots-100": {"episodes": cov["episodes"], "per_source": cov["per_source"],
                                    "per_destination": cov["per_destination"]}}


# ── the rollouts every model shows: three, one of each outcome ──────────────────────────────────

CLIP_STAGES = ("released", "carried", "no_grasp")  # success first


def day_text(day):
    return datetime.strptime(day, "%Y%m%d").strftime("%-d %b %Y")


def clip_story(t, name, step, day):
    """(caption, where the vial ended for the small rack drawing) of an automatically picked rollout: the operator's
    words where the session was noted, else what the arm did."""
    dst = t["move"].split("->")[1]
    head = f"{name} at {kstep(step)} steps, {day_text(day)}."
    nt = t.get("noted")
    if nt:
        o, e = nt["outcome"], nt["ended"]
        at = (dst if o in ("placed", "drop_missed") else "source" if o in ("no_grasp", "wrong_vial")
              else f"held:{e.split('/')[0]}" if o == "never_let_go" and e else e or "source")
        return f"{head} The operator's note: “{nt['note']}”.", at
    to, seen = t.get("to") or "", (t.get("checked") or {}).get("vial")
    slot = lambda x: (re.search(r"\b[LR][1-6]\b", x or "") or [None])[0]
    if t["stage"] == "released":
        return f"{head} The arm let go at the asked slot" + ("; a person saw the vial in it." if seen == "in_slot" else "."), dst
    if t["stage"] == "carried":
        if "never let go" in to:
            w = slot(to.split("held over")[-1])
            return f"{head} It picked up the vial and never let go" + (f", holding it over {w}." if w else "."), (f"held:{w}" if w else "source")
        if seen == "not_in_slot" and t.get("dst_ok"):
            return f"{head} The arm let go at the asked slot, but a person saw the vial was not in it.", dst
        w = slot(to)
        return f"{head} It picked up the vial and let go at {w or 'another slot'}.", (w or dst)
    return f"{head} It never picked up the vial.", "source"


def clip_kind(t):
    """The one-line label above a picked clip: what kind of rollout it is, in the operator's terms where noted."""
    nt = t.get("noted")
    if nt:
        o, e = nt["outcome"], nt["ended"]
        return {"placed": "Success: in the asked slot", "drop_missed": "Missed drop: beside the asked slot",
                "off_slot": f"Wrong slot: put in {e}" if e else "Wrong slot", "never_let_go": "Never let go",
                "wrong_vial": "Failed pickup: took another vial", "no_grasp": "Failed pickup: never picked it up"}[o]
    to, seen = t.get("to") or "", (t.get("checked") or {}).get("vial")
    if t["stage"] == "released":
        return "Success: in the asked slot"
    if t["stage"] == "carried":
        if "never let go" in to:
            return "Never let go"
        if seen == "not_in_slot" and t.get("dst_ok"):
            return "Missed drop: beside the asked slot"
        w = (re.search(r"\b[LR][1-6]\b", to) or [None])[0]
        return f"Wrong slot: let go at {w}" if w else "Wrong slot"
    return "Failed pickup: never picked it up"


def pick_featured(sessions, results):
    """Three rollouts per model, one of each outcome, from its headline row (highest step, sync, raw weights), so every
    model shows the same. A take listed in curation.yaml `featured` wins (with its caption); then rollouts with the
    operator's notes, then ones a person checked, trained moves, the newest session, a typical length. A model without
    one of the outcomes gets another of those it has. Written to build/featured.json for scripts/make_clips.py."""
    cur = {f["take"]: f for f in (yaml.safe_load((SITE / "curation.yaml").read_text()) or {}).get("featured") or []}
    by_run = {m["run"]: m for m in MODELS}
    takes_of = defaultdict(list)
    for s in sessions:
        m = by_run.get(s["run"])
        if m is None:
            continue
        key = f"{m['id']}-{s['step']}-{s['mode']}{'-ema' if s['ema'] else ''}"
        for t in s["takes"]:
            if t.get("stage") and t.get("move") and not t.get("restart") and (t.get("noted") or not t["short"]):
                takes_of[key].append((s, t))
    rows_of = defaultdict(list)
    for r in results:
        rows_of[r["model"]].append(r)
    out = []
    for m in MODELS:
        rs = rows_of.get(m["id"])
        if not rs:
            continue
        row = max([r for r in rs if r["mode"] == "sync" and not r["ema"]] or rs, key=lambda r: (r["step"], r["rollouts"]))
        cands = takes_of[row["key"]]
        if not cands:
            continue
        mid = sorted(t["secs"] for _, t in cands)[len(cands) // 2]
        rank = lambda c: (c[1]["id"] not in cur, not c[1].get("noted"), not (c[1].get("checked") or {}).get("vial"),
                          not c[1]["trained_move"], -int(c[0]["name"].split("_")[-2] + c[0]["name"].split("_")[-1]),
                          abs(c[1]["secs"] - mid), c[1]["id"])
        picked = []
        for stage in CLIP_STAGES:
            pool = sorted((c for c in cands if c[1]["stage"] == stage), key=rank)
            if pool:
                picked.append(pool[0])
        rest = sorted((c for c in cands if c not in picked), key=lambda c: (CLIP_STAGES.index(c[1]["stage"]), rank(c)))
        picked += rest[: max(0, 3 - len(picked))]
        for s, t in picked:
            f = cur.get(t["id"])
            cap, at = clip_story(t, m["name"], s["step"], s["day"])
            out.append({"take": t["id"], "model_id": m["id"], "row": row["key"], "kind": clip_kind(t),
                        "caption": f["caption"].format(name=m["name"]) if f else cap,
                        "vial": (f or {}).get("vial"), "at": (f or {}).get("at") if f else at, "miss": (f or {}).get("miss")})
    BUILD.mkdir(exist_ok=True)
    (BUILD / "featured.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"  build/featured.json ({len(out)} rollouts, {len({f['model_id'] for f in out})} models)")


# ── rollouts ────────────────────────────────────────────────────────────────────────────────────

# November runs, by the checkpoint folder the session log names (tools/rollout_logged.py, session.json)
CKPT_RUN = [("ws220_canon_ft012000_v2/", "pi05-b16k"), ("ws220_canon_base16k/", "pi05-a16k"),
            ("checkpoints/004000_q37g/", "pi05-b4k-q37g"), ("checkpoints/004000_q37/", "pi05-b4k-q37"),
            ("ws220_canon_ft012000/", "pi05-b4k"), ("isaac_expert_ws212_b12_21000/", "isaac-i21k")]
# Isaac's first session (25 Nov, 4 takes) ran before the operator's 42-move sheet and has no notes. Scoring it from the
# arm beside the noted sheet would mix the two in one row, so it gets a run of its own that no model in models.yaml claims.
SESSION_RUN = {"021000_20261125_204715": ("isaac-i21k-unnoted", "Isaac's first test session, before the noted sheet")}


def run_of(policy, day, step, name=None):
    """(training run, how we know) of a rollout session. Sessions before tools/rollout_logged.py
    carry no checkpoint path, so this is read off the shell history and what each run kept."""
    if name in SESSION_RUN:
        return SESSION_RUN[name]
    if name:
        sj = LR / f"outputs/{policy}_rollouts/_sessions/{name}/session.json"
        if sj.exists():
            ck = json.loads(sj.read_text()).get("checkpoint") or ""
            for frag, run in CKPT_RUN:
                if frag in ck:
                    return run, "checkpoint path in the session log"
    if policy == "flux":
        return ("flux-flux25", "left camera, only that run's cameras") if day == "20261007" else \
               ("flux-ws100", "RUN_DIR in the shell history / rollout.sh default")
    if step == "000250":
        return "pi05-noop", "RUN_DIR in the shell history"
    if step == "000500":
        return "pi05-trim2", "RUN_DIR in the shell history"
    if day == "20261021":
        return "pi05-canon", "inferred: the only run that kept the 10k and 12k checkpoints tested that day"
    return "pi05-allcams", "rollout.sh default RUN_DIR, shell history"


def ws_stage(r, check=None):
    """How far a take got, read off the arm by tools/assess_rollouts.py (it cannot see the vial)."""
    if r["src_ok"] and r["dst_ok"]:
        return "released"
    if r["src_ok"] and r["lifted"]:
        return "carried"
    if r["src_ok"]:
        return "no_grasp"  # closed on the right vial but never lifted it: never picked it up
    return "no_grasp"


def episode_rows(root):
    eps = pd.read_parquet(root / "meta/episodes")
    cams = sorted(c[len("videos/"):-len("/chunk_index")] for c in eps.columns
                  if c.startswith("videos/") and c.endswith("/chunk_index"))
    return eps, cams


def video_of(root, row, cam):
    return (str(root / f"videos/{cam}/chunk-{int(row[f'videos/{cam}/chunk_index']):03d}/"
                       f"file-{int(row[f'videos/{cam}/file_index']):03d}.mp4"), float(row[f"videos/{cam}/from_timestamp"]))


WS220_RUNS = ("pi05-b4k", "pi05-b4k-q37", "pi05-b4k-q37g", "pi05-b16k", "pi05-a16k")
WS220_DEMOS = {}  # move -> demonstrations of it in the 220 (src/data/ws220.json)
# Isaac trained on the 220 minus the 8 demonstrations its offline check holds out (episodes 7, 34, 61, 88, 115, 142, 169,
# 196), read from its training copy; the Results page names that set WS212_SET.
WS212_RUNS = ("isaac-i21k",)
WS212_SET = "vial-sort-slots-220 minus 8 held out"
WS212_DEMOS = {}


def ws212_demos():
    if not WS212_DEMOS:
        eps = pd.read_parquet(LR / "data/vial-sort-ws212_isaac/meta/episodes", columns=["tasks"])
        WS212_DEMOS.update(Counter(move_code(parse_move(t[0])) for t in eps["tasks"]))
    return WS212_DEMOS


def demos_in(run):
    """move -> demonstrations of it in the training set of a WS220-era run."""
    return ws212_demos() if run in WS212_RUNS else WS220_DEMOS

# Arm tests the operator noted move by move (notes/*.yaml, written by scripts/notes_to_yaml.py) are scored from
# the notes, not the arm: one rollout per noted move, its result on the move's last take, the takes before it
# restarts. What each outcome is on the site's scale:
NOTE_STAGE = {"placed": "released", "drop_missed": "carried", "off_slot": "carried", "never_let_go": "carried",
              "no_grasp": "no_grasp", "wrong_vial": "no_grasp"}


def load_notes():
    """({take id: (move entry, 'final' | 'restart')}, {session name: notes file}) from notes/*.yaml."""
    by_take, sessions = {}, {}
    for f in sorted((SITE / "notes").glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        for s in d["sessions"]:
            sessions[s] = f.name
        for i, mv in enumerate(d["moves"]):
            if mv["outcome"] not in NOTE_STAGE:
                sys.exit(f"notes/{f.name} #{mv['n']}: outcome {mv['outcome']!r} is not one of {', '.join(NOTE_STAGE)}")
            for k, tid in enumerate(mv["takes"]):
                if tid in by_take:
                    sys.exit(f"notes/{f.name}: {tid} is under two notes")
                by_take[tid] = ({**mv, "file": f.name, "i": i}, "final" if k == len(mv["takes"]) - 1 else "restart")
    return by_take, sessions


def rollouts(clips, checked, notes):
    WS220_DEMOS.update(json.loads((OUT / "ws220.json").read_text())["demos"])
    note_takes, note_sessions = notes
    sessions = []
    for rep in sorted(glob_days()):
        for s in json.loads(rep.read_text())["sessions"]:
            sessions.append((s, True))
    known = {s["name"] for s, _ in sessions}
    # the 2026-10-07 FLUX sessions ran on the earlier scene; assess_rollouts' slot map does not apply
    for root in sorted((LR / "outputs/flux_rollouts").glob("*_20261007_*")):
        if root.name in known or not (root / "meta/episodes").exists():
            continue
        eps, _ = episode_rows(root)
        tasks = pd.read_parquet(root / "meta/tasks.parquet")
        tmap = {int(r.task_index): t for t, r in tasks.iterrows()}
        data = pd.concat(pd.read_parquet(f) for f in sorted(root.glob("data/*/*.parquet")))
        rows = []
        for ep, g in data.groupby("episode_index"):
            task = tmap.get(int(g["task_index"].iloc[0]), "?")
            mv = parse_move(task)
            rows.append({"take": int(ep), "secs": len(g) / FPS, "asked": code(mv) if mv else task, "task": task,
                         "short": len(g) / FPS < SHORT_TAKE_S, "flags": [], "holds": []})
        sessions.append(({"name": root.name, "policy": "flux", "day": "20261007", "mode": "sync",
                          "inferred": True, "step": root.name.split("_")[0], "rows": rows}, False))
    out, robot = [], defaultdict(lambda: defaultdict(Counter))
    for s, assessed in sessions:
        name = s["name"]
        policy = "pi05" if s["policy"].startswith("pi05") else "isaac" if s["policy"].startswith("isaac") else "flux"
        root = LR / "outputs" / f"{policy}_rollouts" / name
        run, how = run_of(policy, s["day"], s["step"], name)
        eps, cams = episode_rows(root)
        takes = []
        for r in s["rows"]:
            row = eps[eps.episode_index == r["take"]].iloc[0]
            mv = parse_move(r.get("task") or "")
            tid = f"{name}_t{r['take']}"
            stage = ws_stage(r, checked.get(tid)) if assessed and not r["short"] else None
            trained_move = not any("NEVER" in f or "no move" in f for f in r["flags"])
            if (run in WS220_RUNS or run in WS212_RUNS) and mv:
                # assess_rollouts checks against the 100-demonstration sheet, which has no move inside one rack;
                # these models trained on the 220 (Isaac: 212 of them), so a move counts as trained if those contain it
                trained_move = demos_in(run).get(move_code(mv), 0) > 0
                r = {**r, "flags": [f for f in r["flags"] if "NEVER" not in f] if trained_move else r["flags"]}
            chk, noted, restart = checked.get(tid), None, False
            if name in note_sessions:
                if tid not in note_takes:
                    sys.exit(f"{tid} was recorded but notes/{note_sessions[name]} has no note for it: re-run "
                             f"scripts/notes_to_yaml.py --force, or add it to the right move by hand")
                nt, role = note_takes[tid]
                if not mv or nt["move"] != move_code(mv):
                    sys.exit(f"notes/{nt['file']} #{nt['n']} is {nt['move']}, but {tid} asked {move_code(mv) if mv else '?'}")
                restart = role == "restart"
                if not restart:
                    stage = NOTE_STAGE[nt["outcome"]]
                    chk = {"vial": "in_slot" if nt["outcome"] == "placed" else "not_in_slot", "why": nt["note"]}
                    noted = {k: nt[k] for k in ("n", "file", "i", "outcome", "ended", "retried", "note")} | \
                            {"attempts": len(nt["takes"])}
            if stage == "released" and (chk or {}).get("vial") == "not_in_slot":
                stage = "carried"  # the arm let go at the asked slot, but a person saw the vial was not in it: a failure
            takes.append({"id": tid, "take": r["take"], "secs": round(r["secs"], 1), "checked": chk,
                          "move": move_code(mv) if mv else None, "task": r.get("task"),
                          "stage": stage, "short": r["short"], "trained_move": trained_move,
                          "restart": restart, "noted": noted,
                          "flags": r["flags"], "from": r.get("from"), "to": r.get("to"),
                          "grasps": r.get("grasps"), "src_ok": r.get("src_ok"), "dst_ok": r.get("dst_ok"),
                          "lifted": r.get("lifted"), "notes": r.get("notes", []),
                          "holds": [{k: h[k] for k in ("grasp", "release", "at", "put", "empty", "carried")} for h in r["holds"]],
                          "strip": r.get("strip") if assessed else None})
            if stage and not restart and mv:
                robot[run][(s["step"], s["mode"], "_ema_" in name)][stage] += 1
            clips.append({"id": tid, "kind": "take", "day": s["day"], "secs": r["secs"],
                          "cams": {c.split(".")[-1]: video_of(root, row, c) for c in cams},
                          "strip": str(LR / f"outputs/rollout_reports/{s['day']}/{r['strip']}") if assessed and r.get("strip") else None})
        out.append({"name": name, "policy": policy, "run": run, "run_source": how, "day": s["day"],
                    "step": int(s["step"]), "ema": "_ema_" in name, "mode": s["mode"], "mode_inferred": s["inferred"],
                    "assessed": assessed, "cams": [c.split(".")[-1] for c in cams], "takes": takes})
    robot_rows = {run: [{"step": int(step), "mode": mode, "ema": ema, "stages": {k: c[k] for k, _ in WS_STAGES},
                         "takes": sum(c.values())} for (step, mode, ema), c in sorted(by.items())]
                  for run, by in robot.items()}
    write("rollouts", {"stages": [{"key": k, "label": lab} for k, lab in WS_STAGES], "sessions": out})
    return robot_rows


def glob_days():
    return (LR / "outputs/rollout_reports").glob("*/report.json")


# ── datasets ────────────────────────────────────────────────────────────────────────────────────

def hf_json(url, offline):
    cache = BUILD / "cache" / re.sub(r"[^A-Za-z0-9._-]+", "_", url)
    if not offline:
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                cache.parent.mkdir(parents=True, exist_ok=True)
                cache.write_bytes(r.read())
        except Exception as e:
            print(f"  ! {url}: {e} (using the cache)")
    return json.loads(cache.read_text()) if cache.exists() else None


def datasets(offline):
    listing = hf_json(f"https://huggingface.co/api/datasets?author={HF_USER}&limit=200", offline) or []
    by_run = {m["run"]: m for m in MODELS}
    owner = {}  # session name -> model, for the "rollout_<policy>_<session>" repositories
    for s_ in json.loads((OUT / "rollouts.json").read_text())["sessions"]:
        if s_["run"] in by_run:
            owner[s_["name"]] = by_run[s_["run"]]
    out = []
    for d in listing:
        info = hf_json(f"https://huggingface.co/datasets/{d['id']}/resolve/main/meta/info.json", offline) or {}
        cams = [k.split(".")[-1] for k, v in info.get("features", {}).items() if k.startswith("observation.images")]
        out.append({"id": d["id"], "name": d["id"].split("/")[1], "kind": "rollout" if "/rollout_" in d["id"] else "training",
                    "updated": (d.get("lastModified") or "")[:10], "episodes": info.get("total_episodes"),
                    "frames": info.get("total_frames"), "fps": info.get("fps"), "cameras": cams,
                    "format": info.get("codebase_version"), "private": bool(d.get("private")),
                    "model": next((m["name"] for n, m in owner.items() if d["id"].endswith(f"_{n}")), None)})
    out.sort(key=lambda d: (d["kind"], d["updated"]))
    models = hf_json(f"https://huggingface.co/api/models?author={HF_USER}&limit=200", offline) or []
    write("datasets", {"datasets": out, "models": [{"id": m["id"], "name": m["id"].split("/")[1]} for m in models]})


def coverage(scen):
    """Training demos per move (v5 RGB set the deployed π0.5 trained on) beside the eval's moves."""
    eps = pd.read_parquet(LR / "data/vial-sort-v5-ee-rgb/meta/episodes", columns=["tasks"])
    demos = Counter(move_code(parse_move(t[0])) for t in eps["tasks"])
    # every demonstration has its own wording (ee/paraphrase_tasks.py); show the move with the most
    wordings = defaultdict(set)
    for t in eps["tasks"]:
        wordings[move_code(parse_move(t[0]))].add(t[0])
    most = max(wordings, key=lambda m: (len(wordings[m]), m))
    per_src, per_dst = Counter(), Counter()
    for mv, n in demos.items():
        src, dst = mv.split("->")
        per_src[src] += n
        per_dst[dst] += n
    write("coverage", {"dataset": "vial-sort-v5-ee-rgb", "episodes": int(sum(demos.values())),
                       "distinct_prompts": len({t[0] for t in eps["tasks"]}),
                       "wordings": {"move": most, "prompts": sorted(wordings[most])},
                       "demos": dict(sorted(demos.items())), "per_source": dict(sorted(per_src.items())),
                       "per_destination": dict(sorted(per_dst.items())),
                       "eval": {s["move"]: {"n": s["n"], "complete": s["complete"], "demos": demos.get(s["move"], 0),
                                            "demos_from_source": per_src.get(s["src"], 0),
                                            "demos_to_destination": per_dst.get(s["dst"], 0)} for s in scen}})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="answer HF API calls from build/cache")
    ap.add_argument("--rollouts-only", action="store_true",
                    help="only list the recorded takes (src/data/rollouts.json), without the notes: what "
                         "scripts/notes_to_yaml.py matches new notes against (scripts/update_site.py runs this first)")
    a = ap.parse_args()
    clips = []
    print(f"reading {LR}")
    checked = (yaml.safe_load((SITE / "curation.yaml").read_text()) or {}).get("checked") or {}
    import runpy
    runpy.run_path(str(SITE / "scripts/build_ws220.py"))
    if a.rollouts_only:
        rollouts(clips, checked, ({}, {}))
        return
    scen, kpi = evals(clips)
    robot = rollouts(clips, checked, load_notes())
    runs = training(robot)
    october(gate(), runs)
    models(runs, kpi)
    coverage(scen)
    datasets(a.offline)
    BUILD.mkdir(exist_ok=True)
    (BUILD / "clips.json").write_text(json.dumps(clips, indent=1) + "\n")
    print(f"  build/clips.json ({len(clips)} clip sources)")


if __name__ == "__main__":
    main()
