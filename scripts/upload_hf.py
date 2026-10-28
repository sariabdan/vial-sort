#!/usr/bin/env python3
"""Publish the October checkpoints and robot sessions to Hugging Face (user sari-abdan).

    ~/lerobot/.venv/bin/python scripts/upload_hf.py --dry-run            # print the plan, touch nothing
    ~/lerobot/.venv/bin/python scripts/upload_hf.py --only models        # 3 model repos
    ~/lerobot/.venv/bin/python scripts/upload_hf.py --only rollouts      # every session not yet public

Every repo is created PRIVATE, filled, checked against the local sizes, and only then made public, so
a failed upload never leaves a half-empty public repo. Re-running skips repos that are already public.
Needs a Hugging Face token with write access (hf auth login). Cards state only what the logs, configs and
src/data/*.json say; the numbers come from src/data/october.json, written by scripts/build_data.py.

Not uploaded, on purpose:
  * the prepared FLUX base (a copy of Black Forest Labs' weights under the FLUX Kommunity License)
  * optimizer / training state, intermediate checkpoints
  * the 5 rollout sessions already public (their public copies hold only the first five takes)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from huggingface_hub import HfApi

SITE = Path(__file__).resolve().parents[1]
LR = Path(os.environ.get("LEROBOT", Path.home() / "lerobot"))
USER = "sari-abdan"
OUT = LR / "outputs"
FLUX_LICENSE = next((LR.parent / ".cache/huggingface/hub/models--black-forest-labs--flux-3-action-so101/snapshots").glob("*/LICENSE.md"))

october = json.loads((SITE / "src/data/october.json").read_text())
sessions = {s["name"]: s for s in json.loads((SITE / "src/data/rollouts.json").read_text())["sessions"]}
runs = {r["id"]: r for r in october["runs"]}
training = {r["id"]: r for r in json.loads((SITE / "src/data/training.json").read_text())["runs"]}
STAGE = {s["key"]: s["label"] for s in october["stages"]}


def mb(n):
    return f"{n / 1e6:,.0f} MB" if n < 1e9 else f"{n / 1e9:.1f} GB"


def size(path):
    return sum(f.stat().st_size for f in Path(path).rglob("*") if f.is_file())


# ── model cards ─────────────────────────────────────────────────────────────────────────────────

PROMPT = """The prompt grammar, which the policy was trained on:

> Move the vial from position 3 of the right rack to slot 6 of the left rack.
> Move the vial from position 4 of the left rack to the bin.

Left and right are read from the follower arm: the left rack is the rack to the left of the arm, which is the
top rack in the overhead camera. Source slots in training are 1, 3, 4 and 6; destination slots 1, 3 and 6, or
the bin. Slots 2 and 5 appear in no training prompt, on purpose."""

HOW = """These checkpoints were written by LeRobot's `lerobot-train` and are loaded with LeRobot's policy classes.
The rollouts used LeRobot's `lerobot-rollout`; the project's rollout and assessment scripts are not published yet."""


def results_block(run_id, step, what):
    """Whole-run counts, and the counts of this checkpoint alone (the run's other checkpoints were tested too)."""
    r = runs[run_id]
    right = r["takes"] - r["stages"]["no_grasp"]
    here = [x for x in training[run_id]["robot"] if x["step"] == step]
    n = sum(x["takes"] for x in here)
    right_here = n - sum(x["stages"]["no_grasp"] for x in here)
    placed_here = sum(x["stages"]["released"] for x in here)
    return f"""## What it did on the robot

Across every tested checkpoint of this run ({what}), October 2026, there are {r["takes"]} scored takes: the right vial was
gripped in **{right}** and let go at the asked slot in **{r["stages"]["released"]}**. At {step:,} steps alone: {n} takes, the right
vial gripped in {right_here} and let go at the asked slot in {placed_here}. The takes were scored by a script that reads the
arm's joint poses; it cannot see the vial, so "let go at the asked slot" means the arm opened there, which is the project's
"right destination". Some of these takes were also watched on video and had the vial in the hole. They were test runs during development,
not a planned evaluation, and the numbers are small. The recordings are in the `rollout_*` datasets of this account (a few later
takes of five sessions are not public)."""


def pi05_card(run_id, repo, ckpt, train, dataset_note, extra):
    t = json.loads(train.read_text())
    steps, batch, lr = t["steps"], t["batch_size"], t["optimizer"]["lr"]
    return f"""---
license: gemma
library_name: lerobot
pipeline_tag: robotics
base_model: lerobot/pi05_base
datasets:
- {USER}/vial-sort-slots-100
tags:
- lerobot
- robotics
- vision-language-action
- pi05
- so101
---

# π0.5 on 100 vial-sorting demonstrations, {extra["title"]}

A full fine-tune of π0.5 ([`lerobot/pi05_base`](https://huggingface.co/lerobot/pi05_base)) that moves a vial from one
named slot to another, or into a bin, with a low-cost SO-101 arm. It is a research checkpoint, not a product.
**It does not reliably complete the task.**

## Training

| | |
|---|---|
| Base | `lerobot/pi05_base`, vision encoder and the whole vision–language model trained (not frozen) |
| Data | {dataset_note} |
| Steps | {steps:,} at batch size {batch}, AdamW, learning rate {lr}, bfloat16 |
| Inputs | five 640×480 colour cameras (top_down, left_top, left_bottom, right, wrist), the 6 joint positions, the prompt |
| Output | 6 joint targets in chunks of 50 steps; we ran it with `n_action_steps=15` |
| Hardware | one RTX PRO 6000 Blackwell, about {extra["hours"]} hours |

{extra["recipe"]}

{PROMPT}

{results_block(run_id, 12000, extra["what"])}

{extra["limits"]}

{HOW}

## License

π0.5 is built on PaliGemma and Gemma. Use of this model is subject to the
[Gemma Terms of Use](https://ai.google.dev/gemma/terms). See `NOTICE`.
"""


def flux_card(run_id, ckpt_step, train):
    t = json.loads(train.read_text())
    return f"""---
license: other
license_name: flux-kommunity-license
license_link: LICENSE.md
library_name: lerobot
pipeline_tag: robotics
base_model: black-forest-labs/flux-3-action-so101
datasets:
- {USER}/vial-sort-slots-100
tags:
- lerobot
- robotics
- lora
- flux3
- so101
---

# FLUX 3 Action LoRA on 100 vial-sorting demonstrations, {ckpt_step:,} steps

A LoRA adapter for [`black-forest-labs/flux-3-action-so101`](https://huggingface.co/black-forest-labs/flux-3-action-so101)
that moves a vial from one named slot to another, or into a bin, with a low-cost SO-101 arm. It is a research
checkpoint, not a product. **It does not reliably complete the task**: see below.

**This repository holds only the adapter and its normalisation files, not the base model.** The base weights are
Black Forest Labs' and are used under the FLUX Kommunity License, which this adapter, as a Derivative, also falls
under: see `LICENSE.md` and `NOTICE`. This adapter is a modified version of the FLUX model.

## Training

| | |
|---|---|
| Base | `flux-3-action-so101`, with its three normalisation files rewritten using this dataset's 1st and 99th percentiles (`prepare_base.py` shows how) |
| Adapter | LoRA, rank {json.loads((OUT / "flux3_lora_vial-sort-ws100_top_down/checkpoints/030000/pretrained_model/adapter_config.json").read_text())["r"]}, on the attention and MLP projections |
| Data | the 100 demonstrations of [`{USER}/vial-sort-slots-100`](https://huggingface.co/datasets/{USER}/vial-sort-slots-100), as a copy with only the top-down camera (as `scene`) and the wrist camera |
| Steps | {t["steps"]:,} micro-steps (batch {t["batch_size"]} with gradient accumulation 4), AdamW, learning rate {t["optimizer"]["lr"]}, bfloat16, one RTX PRO 6000 Blackwell, about 17 hours in two sessions (one resumed) |
| Inputs | two 256×256 colour views, the 6 joint positions, the prompt |
| Output | 6 joint targets in chunks of 42 steps; we ran it with `n_action_steps=32` |

The top-level files are the adapter; `ema/` holds the same adapter with exponential-moving-average weights.

{PROMPT}

{results_block(run_id, ckpt_step, "10k to 30k steps, with and without EMA weights")}

In the one session whose rate was logged (the 10k checkpoint, 16 October) the policy ran at 15.5 Hz against a 30 Hz
target, which on its own could hurt its takes.

{HOW}

## License

FLUX Kommunity License v1.0, Black Forest Labs Inc. See `LICENSE.md` and `NOTICE`. Commercial use is limited as that
license describes.
"""


FLUX_NOTICE = """This FLUX Model is licensed by Black Forest Labs Inc. under the FLUX Kommunity License. Copyright Black Forest Labs Inc. IN NO EVENT SHALL BLACK FOREST LABS INC. BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH USE OF THIS MODEL.

This is a modified version of the FLUX Model: a LoRA adapter, fine-tuned by Sari Abdan, with normalisation files rewritten for the vial-sorting dataset. Black Forest Labs Inc. did not make or endorse it.
"""
GEMMA_NOTICE = """Gemma is provided under and subject to the Gemma Terms of Use found at https://ai.google.dev/gemma/terms

This is a modified version of π0.5 (lerobot/pi05_base, itself built on PaliGemma and Gemma): a full fine-tune, trained by Sari Abdan on 100 vial-sorting demonstrations. It is not made or endorsed by Google or Physical Intelligence.
"""


def models():
    pi = OUT / "pi05_full_vial-sort-ws100_canon_base12k/checkpoints/012000/pretrained_model"
    al = OUT / "pi05_full_vial-sort-ws100_allcams/checkpoints/012000/pretrained_model"
    fx = OUT / "flux3_lora_vial-sort-ws100_top_down/checkpoints/030000"
    canon_run, all_run = runs["pi05-canon"], runs["pi05-allcams"]
    out = []
    out.append({
        "repo": f"{USER}/vial-sort-pi05-ws100-canon-12000", "kind": "model",
        "folders": [(pi, "")], "ignore": [],
        "files": {"NOTICE": GEMMA_NOTICE, "README.md": pi05_card(
            "pi05-canon", "", pi, pi / "train_config.json",
            "100 demonstrations, idle start and end trimmed (46,361 of 58,650 frames), one fixed sentence per move "
            "(32 sentences). A derived copy of `vial-sort-slots-100` that is not published",
            {"title": "trimmed, canonical prompts, 12k steps", "hours": "11.6", "what": "10k and 12k steps",
             "recipe": "The idle start and end of each demonstration were cut, because the arm standing still at home was both the cue to go "
                       "and the cue to stay. In the first frames of each demonstration, where the operator leans over the robot, the wrist and "
                       "left_bottom views were swapped for views of the arm at home with nobody there (taken from other demonstrations and "
                       "from rollout recordings).",
             "limits": "## Limits\n\nAn offline test of this run's checkpoints found that, from 5k steps on, its reach follows the source slot "
                       "named in the prompt, but at no checkpoint did it follow the destination slot (0 of 7 test frames passed at every "
                       "checkpoint from 1k to 12k). The cause, found on 21 October, is a shortcut in the data: the 100 demonstrations were "
                       "recorded one destination per sitting, with the bin and the light changing between sittings, so the camera pictures "
                       "give the destination away. A prompt naming another destination was followed 19% of the time, while swapping all five "
                       "camera images from another demonstration steered it 81% of the time. Most takes started from one source slot, and "
                       "nine takes are a small sample."})},
        "expect": {"model.safetensors": (pi / "model.safetensors").stat().st_size}})
    out.append({
        "repo": f"{USER}/vial-sort-pi05-ws100-allcams-12000", "kind": "model",
        "folders": [(al, "")], "ignore": [],
        "files": {"NOTICE": GEMMA_NOTICE, "README.md": pi05_card(
            "pi05-allcams", "", al, al / "train_config.json",
            "the 100 demonstrations of [`" + USER + "/vial-sort-slots-100`](https://huggingface.co/datasets/" + USER + "/vial-sort-slots-100), all frames, "
            "wording varied (100 different sentences)",
            {"title": "all frames, 12k steps", "hours": "11.8", "what": "7k, 9k and 12k steps",
             "recipe": "This was the first full fine-tune, trained on every frame including the idle start of each demonstration. On the real table "
                       "the 12k checkpoint often stayed at its start pose: according to the training notes it did so in 9 of 11 takes on 19 October. "
                       "The later trimmed run (see this account's other π0.5 checkpoint) was made to test why.",
             "limits": "## Limits\n\nMost of its takes never gripped the right vial. It was trained on data in which the camera pictures give "
                       "the destination away (one destination per recording sitting), so it also does not follow the destination in the "
                       "prompt. Use the trimmed run's checkpoint, not this one, unless you want to reproduce the comparison."})},
        "expect": {"model.safetensors": (al / "model.safetensors").stat().st_size}})
    out.append({
        "repo": f"{USER}/vial-sort-flux3-ws100-30000", "kind": "model",
        "folders": [(fx / "pretrained_model", ""), (fx / "pretrained_model_ema", "ema")], "ignore": ["README.md"],
        "files": {"NOTICE": FLUX_NOTICE, "LICENSE.md": FLUX_LICENSE.read_text(),
                  "prepare_base.py": (LR / "tools/flux/prepare_base.py").read_text(),
                  "README.md": flux_card("flux-ws100", 30000, fx / "pretrained_model/train_config.json")},
        "expect": {"adapter_model.safetensors": (fx / "pretrained_model/adapter_model.safetensors").stat().st_size}})
    return out


# ── rollout sessions ────────────────────────────────────────────────────────────────────────────

NAME = re.compile(r"^(\d+)(_ema)?_(\d{8})_(\d{6})$")
HF_NAME = re.compile(r"^rollout_(pi05|flux)_(\d+)(_ema)?_(\d{8})_(\d{6})$")


def stamp(d, t):
    return datetime.strptime(d + t, "%Y%m%d%H%M%S")


def session_card(repo, name, s):
    takes = s["takes"]
    run = s["run"]
    def how(t):
        if t["short"]:
            return "under 3 s, not scored"
        if not t["stage"]:
            return "not scored"
        return STAGE[t["stage"]] + ("" if t["trained_move"] else " (a move no demonstration contains)")

    rows = "\n".join(f"| {t['take']} | {(t['move'] or '').replace('->', ' → ') or 'unreadable'} | {t['secs']:.0f} s | {how(t)} |"
                     for t in takes)
    layout = ("\nThis session was recorded on an earlier layout of the table (left and wrist cameras only), before the racks moved; "
              "the assessment script cannot read it.\n" if run == "flux-flux25" else "")
    return f"""---
license: apache-2.0
task_categories:
- robotics
tags:
- LeRobot
configs:
- config_name: default
  data_files: data/*/*.parquet
---

# Rollout: {s["policy"]} {s["step"]:,} steps{" (EMA weights)" if s["ema"] else ""}, {name}

Autonomous rollouts of a vial-sorting policy on an SO-101 arm, recorded by `lerobot-rollout`: **{len(takes)} take{'' if len(takes) == 1 else 's'}**
(one episode each), five cameras (`{", ".join(s["cams"])}`), 30 frames a second. These are the policy's attempts, not
demonstrations, and most of them fail.

- **Policy:** {"π0.5" if s["policy"] == "pi05" else "FLUX 3 Action"}, checkpoint at {s["step"]:,} steps, training run `{run}` ({s["run_source"]}).
- **Inference mode:** {"sync (FLUX has no RTC)" if s["policy"] == "flux" else s["mode"] + (" (inferred from the actions: the session wrote no log)" if s["mode_inferred"] else "")}.
{layout}
| Take | Asked move | Length | How far it got (a script reading the arm, not the vial; the last rung is "right destination") |
|---|---|---|---|
{rows}

Moves are source → destination: `R3` is slot 3 of the right rack. Left and right are read from the follower arm (the left
rack is the top rack in the overhead camera). People are visible in some camera views. The training data is
[`{USER}/vial-sort-slots-100`](https://huggingface.co/datasets/{USER}/vial-sort-slots-100).
"""


def plan_rollouts(api):
    public = [d.id.split("/")[1] for d in api.list_datasets(author=USER) if d.id.split("/")[1].startswith("rollout_")]
    local = []
    for pol, base in (("pi05", OUT / "pi05_rollouts"), ("flux", OUT / "flux_rollouts")):
        for d in sorted(base.iterdir()):
            m = NAME.match(d.name)
            if d.is_dir() and m:
                local.append((pol, d, *m.groups()))
    # A public repo is named when its session finished loading the policy, 30 to 100 s after the local folder.
    # Each public repo is the twin of the ONE local session just before it; neighbours are different sessions.
    twin = {}
    for name in public:
        m = HF_NAME.match(name)
        if not m:
            continue
        pol, step, ema, day, tm = m.groups()
        near = [(( stamp(day, tm) - stamp(l[4], l[5])).total_seconds(), l[1].name) for l in local
                if l[0] == pol and l[2] == step and bool(l[3]) == bool(ema) and l[4] == day
                and 0 <= (stamp(day, tm) - stamp(l[4], l[5])).total_seconds() <= 600]
        if near:
            twin[min(near)[1]] = name
    todo, skipped = [], []
    for pol, d, *_ in local:
        if not ((d / "meta/info.json").exists() and list(d.glob("data/*/*.parquet")) and (d / "videos").exists()):
            skipped.append((d.name, "no recorded data (session died or still open)"))
        elif d.name in twin:
            skipped.append((d.name, f"already public as {twin[d.name]} (first five takes)"))
        elif d.name not in sessions:
            skipped.append((d.name, "not in src/data/rollouts.json: run scripts/build_data.py"))
        else:
            todo.append({"repo": f"{USER}/rollout_{pol}_{d.name}", "kind": "dataset", "folder": d, "name": d.name, "session": sessions[d.name]})
    return todo, skipped


# ── upload ──────────────────────────────────────────────────────────────────────────────────────

def publish(api, item, dry):
    repo, kind = item["repo"], item["kind"]
    print(f"\n== {repo}", flush=True)
    if dry:
        return
    existing = None
    try:
        existing = api.repo_info(repo, repo_type=kind)
    except Exception:
        pass
    if existing is not None and not existing.private:
        print("   already public, skipping")
        return
    api.create_repo(repo, repo_type=kind, private=True, exist_ok=True)
    if kind == "model":
        for folder, sub in item["folders"]:
            api.upload_folder(folder_path=str(folder), path_in_repo=sub or None, repo_id=repo, repo_type=kind,
                              ignore_patterns=item["ignore"], commit_message=f"Add {sub or 'checkpoint'}")
        for fname, text in item["files"].items():
            api.upload_file(path_or_fileobj=text.encode(), path_in_repo=fname, repo_id=repo, repo_type=kind, commit_message=f"Add {fname}")
    else:
        api.upload_folder(folder_path=str(item["folder"]), repo_id=repo, repo_type=kind, commit_message="Add session")
        api.upload_file(path_or_fileobj=session_card(repo, item["name"], item["session"]).encode(), path_in_repo="README.md",
                        repo_id=repo, repo_type=kind, commit_message="Add card")
        api.create_tag(repo, tag="v3.0", repo_type=kind, exist_ok=True)  # LeRobot loads datasets by this version tag
    # check what landed against what is on disk, then and only then go public
    remote = {f.rfilename: f.size for f in api.model_info(repo, files_metadata=True).siblings} if kind == "model" else \
        {f.rfilename: f.size for f in api.dataset_info(repo, files_metadata=True).siblings}
    for fname, want in item.get("expect", {}).items():
        got = remote.get(fname)
        assert got == want, f"{repo}: {fname} is {got} bytes on the Hub, {want} on disk"
    if kind == "dataset":
        local = sum(1 for f in Path(item["folder"]).rglob("*") if f.is_file())
        assert len(remote) >= local, f"{repo}: {len(remote)} files on the Hub, {local} on disk"
    api.update_repo_settings(repo, repo_type=kind, private=False)
    print(f"   public: https://huggingface.co/{'datasets/' if kind == 'dataset' else ''}{repo}  ({len(remote)} files)", flush=True)


def refresh_cards(api):
    """Re-push the README of every repo this script owns that is already public (after a card fix)."""
    for item in models():
        api.upload_file(path_or_fileobj=item["files"]["README.md"].encode(), path_in_repo="README.md",
                        repo_id=item["repo"], repo_type="model", commit_message="Correct the results numbers")
        print("card refreshed:", item["repo"], flush=True)
    todo, _ = plan_rollouts(api)
    public = {d.id for d in api.list_datasets(author=USER) if not d.private}
    for it in todo:
        if it["repo"] in public:
            api.upload_file(path_or_fileobj=session_card(it["repo"], it["name"], it["session"]).encode(), path_in_repo="README.md",
                            repo_id=it["repo"], repo_type="dataset", commit_message="Correct the card")
            print("card refreshed:", it["repo"], flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cards-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", choices=("models", "rollouts"))
    a = ap.parse_args()
    api = HfApi()
    print(f"user: {api.whoami()['name']}")
    if a.cards_only:
        return refresh_cards(api)
    items = []
    if a.only in (None, "models"):
        items += models()
    todo, skipped = ([], [])
    if a.only in (None, "rollouts"):
        todo, skipped = plan_rollouts(api)
        items += todo
    total = 0
    for it in items:
        s = sum(size(f) for f, _ in it["folders"]) if it["kind"] == "model" else size(it["folder"])
        total += s
        print(f"  {it['repo']:<72} {mb(s)}")
    print(f"\n{len(items)} repos, {mb(total)}, public once verified")
    for n, why in skipped:
        print(f"  skip {n}: {why}")
    for it in items:
        publish(api, it, a.dry_run)
    if a.dry_run:
        print("\n(dry run: nothing was created or uploaded)")


if __name__ == "__main__":
    sys.exit(main())
