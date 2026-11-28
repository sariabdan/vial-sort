#!/usr/bin/env python3
"""From the operator's notes to the live site in one command, with the checks in between.

    ~/lerobot/.venv/bin/python scripts/update_site.py               # check, rebuild, publish (push to main)
    ~/lerobot/.venv/bin/python scripts/update_site.py --no-deploy   # check and rebuild only

Run it after writing notes in notes/<X>.txt: one line per move as written at the robot, "N: SRC DST: what happened",
with the model's name on the first line ("A 16000: plain bagel"). It stops at the first error:
  1. rollout days whose recordings are newer than their report: ~/lerobot/tools/assess_rollouts.py --day D --json
  2. scripts/build_data.py --rollouts-only: the recorded takes, for the notes to be matched against
  3. every notes/*.txt -> notes/*.yaml (scripts/notes_to_yaml.py). The txt is the source: a yaml is rewritten each run.
     The model is the one the txt's first line names, else the one its yaml already has.
  4. checks. Errors stop the run, warnings are listed and do not:
       error    a line no rule reads, or a note that does not match the recorded takes (from notes_to_yaml)
       warning  a number used twice or skipped, a '# vial in X' line whose moves start somewhere else,
                a note that disagrees with the arm's measured release by more than 0.75 slot (worth a look),
                a noted session that is not on Hugging Face as rollout_<policy>_<session>
  5. scripts/build_data.py, scripts/make_clips.py, astro build, scripts/check_text.py
  6. each noted model's numbers on the site must equal its notes (error otherwise); prints what changed
  7. unless --no-deploy: commits notes/, src/data/ and public/media/ and pushes to main, which redeploys the site.
     It refuses while other files have uncommitted changes, so the live site never gets data its code cannot show.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parents[1]
LR = Path(os.environ.get("LEROBOT", Path.home() / "lerobot"))
PY = sys.executable
SITE_URL = "https://cognitive-software-labs.github.io/vial-sort/"
OUTPUTS = ("notes/", "src/data/", "public/media/")  # what this script writes and publishes
NOTE_STAGE = {"placed": "released", "drop_missed": "carried", "off_slot": "carried", "never_let_go": "carried",  # = build_data.py
              "no_grasp": "no_grasp", "wrong_vial": "no_grasp"}
LINE = re.compile(r"^\s*(\d+)\s*:\s*([LR][1-6]|bin)\s+([LR][1-6]|bin)\s*:", re.I)
warnings = []


def step(title):
    print(f"\n== {title}", flush=True)


def run(cmd, cwd=SITE, env=None, quiet=False):
    """Run a step; on failure print its output and stop the whole pipeline."""
    r = subprocess.run([str(c) for c in cmd], cwd=cwd, env=env, capture_output=True, text=True)
    if r.returncode:
        print((r.stdout + r.stderr)[-3000:])
        sys.exit(f"\nSTOPPED: {' '.join(str(c) for c in cmd[:3])} ... failed (exit {r.returncode}). Nothing was published.")
    if not quiet:
        out = [l for l in r.stdout.splitlines() if l.strip()]
        print("\n".join(out[-12:]))
    return r.stdout


def node_env():
    """astro needs Node 22 or newer; the default node here is older, so use the newest one nvm has."""
    env = dict(os.environ)

    def major(node):
        try:
            return int(subprocess.run([str(node), "--version"], capture_output=True, text=True).stdout.strip().lstrip("v").split(".")[0])
        except (OSError, ValueError):
            return 0

    if shutil.which("node") and major("node") >= 22:
        return env
    for node in sorted(Path.home().glob(".nvm/versions/node/v*/bin/node"), key=major, reverse=True):
        if major(node) >= 22:
            env["PATH"] = f"{node.parent}:{env['PATH']}"
            return env
    sys.exit("STOPPED: astro needs Node 22 or newer, and none was found (nvm install 24)")


# ── 1. recordings -> reports ──────────────────────────────────────────────────────────────────────

def stale_days():
    """Days with recordings newer than their report; new days after the newest report count too. Older days without
    a report are left alone on purpose (the 7 Oct FLUX sessions ran on an earlier layout the assessment cannot read)."""
    reports = LR / "outputs/rollout_reports"
    have = {d.name: (d / "report.json").stat().st_mtime for d in reports.glob("*") if (d / "report.json").exists()}
    newest = {}
    for base in ("pi05_rollouts", "flux_rollouts", "isaac_rollouts"):
        for rec in (LR / "outputs" / base).glob("*"):
            m = re.search(r"_(\d{8})_\d{6}$", rec.name)
            info = rec / "meta/info.json"
            if m and info.exists():
                newest[m.group(1)] = max(newest.get(m.group(1), 0), info.stat().st_mtime)
    last = max(have, default="")
    return sorted(d for d, t in newest.items() if (d in have and have[d] < t) or (d not in have and d > last))


# ── 3. notes -> yaml ──────────────────────────────────────────────────────────────────────────────

def model_of(txt):
    models = yaml.safe_load((SITE / "models.yaml").read_text())["models"]
    first = next((l for l in txt.read_text().splitlines() if l.strip() and not LINE.match(l)), "")
    named = re.sub(r"\s+", " ", first.split(":", 1)[1]).strip().lower() if ":" in first else ""
    for m in models:
        if named and m["name"].lower() == named:
            return m["id"]
    y = txt.with_suffix(".yaml")
    if y.exists():
        return yaml.safe_load(y.read_text())["model"]
    sys.exit(f"STOPPED: {txt.relative_to(SITE)}: put the model's name on the first line, e.g. 'A 16000: plain bagel'")


def check_notes_text(txt):
    nums, cur, bad = [], None, []
    for l in txt.read_text().splitlines():
        v = re.match(r"^# vial in ([LR][1-6])", l)
        if v:
            cur = v.group(1)
            continue
        if l.startswith("# ──"):
            cur = None
        m = LINE.match(l)
        if m:
            nums.append(int(m.group(1)))
            if cur and m.group(2).upper() != cur:
                bad.append(l.strip())
    twice = sorted(n for n, c in Counter(nums).items() if c > 1)
    skipped = sorted(set(range(1, max(nums, default=0) + 1)) - set(nums))
    name = txt.relative_to(SITE)
    if twice:
        warnings.append(f"{name}: numbers used twice {twice} (the second becomes {twice[0]}b, ...)")
    if skipped:
        warnings.append(f"{name}: numbers skipped {skipped}")
    for l in bad:
        warnings.append(f"{name}: under a '# vial in' line but starts elsewhere: {l}")


def check_against_arm(y):
    """Notes whose slot disagrees with where the arm let go (tools/assess_rollouts.py), by more than 0.75 slot."""
    reps = {}
    for day in {s.split("_")[-2] for s in y["sessions"]}:
        p = LR / f"outputs/rollout_reports/{day}/report.json"
        if p.exists():
            for s in json.loads(p.read_text())["sessions"]:
                for r in s["rows"]:
                    reps[f"{s['name']}_t{r['take']}"] = r

    def at(s):
        m = re.search(r"([LR])\d \((\d+(?:\.\d+)?)\)", s or "")
        return (m.group(1), float(m.group(2))) if m else None

    for m in y["moves"]:
        if m["outcome"] not in ("placed", "drop_missed", "off_slot"):
            continue
        r, want = reps.get(m["takes"][-1]), m["ended"]
        if not r or not want:
            continue
        to = r.get("to") or ""
        if want == "bin":
            why = None if to.strip() == "bin" else f"arm: {to or 'no release'}"
        elif "never let go" in to:
            why = "arm: never let go during the take"
        else:
            a = at(to)
            why = f"arm: let go at {a[0]}{a[1]:.1f}" if a and (a[0] != want[0] or abs(a[1] - int(want[1])) > 0.75) else None
        if why:
            warnings.append(f"{y['model']} #{m['n']} {m['move']} '{m['note'][:50]}' read as {m['outcome']} at {want}, but {why}")


def check_hub(yamls):
    try:
        from huggingface_hub import HfApi
        on_hub = {d.id.split("/")[1] for d in HfApi().list_datasets(author="sari-abdan", search="rollout_")}
    except Exception as e:  # no network: say so, do not stop
        warnings.append(f"could not ask Hugging Face which sessions are up ({type(e).__name__})")
        return
    for y in yamls:
        for s in y["sessions"]:
            if not any(f"rollout_{pol}_{s}" in on_hub for pol in ("pi05", "flux", "isaac")):
                warnings.append(f"{s} is not on Hugging Face: in ~/lerobot run  .venv/bin/python tools/upload_session.py "
                                f"outputs/<pi05|flux|isaac>_rollouts/{s}")


# ── 6. the site against the notes ─────────────────────────────────────────────────────────────────

def check_site(yamls):
    rows = json.loads((SITE / "src/data/experiments.json").read_text())["rows"]
    by_model = {}
    for y in yamls:
        by_model.setdefault(y["model"], []).extend(y["moves"])
    for model, moves in by_model.items():
        got = Counter()
        for r in rows:
            if r["model"] == model and r.get("scored_by") == "notes":
                got.update({k: v for k, v in r["stages"].items()})
        want = Counter(NOTE_STAGE[m["outcome"]] for m in moves)
        if +got != +want:
            sys.exit(f"STOPPED: {model} on the site {dict(+got)} does not equal its notes {dict(+want)}. Nothing was published.")
        print(f"  {model}: {len(moves)} noted moves = the site's numbers")


def changes():
    """Per-model row numbers before (the last commit) and after, for the summary and the commit message."""
    try:
        old = json.loads(subprocess.run(["git", "show", "HEAD:src/data/experiments.json"], cwd=SITE, capture_output=True,
                                        text=True, check=True).stdout)["rows"]
    except subprocess.CalledProcessError:
        old = []
    new = json.loads((SITE / "src/data/experiments.json").read_text())["rows"]
    o = {r["key"]: r for r in old}
    out = []
    for r in new:
        a = o.get(r["key"])
        fmt = lambda x: f"n={x['rollouts']}, in the asked slot {x['released']}"
        if a is None:
            out.append(f"{r['label']}: new row, {fmt(r)}")
        elif (a["rollouts"], a["released"], a["seen_in_slot"]) != (r["rollouts"], r["released"], r["seen_in_slot"]):
            out.append(f"{r['label']}: {fmt(a)}  ->  {fmt(r)}")
    return out


# ── 7. publish ─────────────────────────────────────────────────────────────────────────────────────

def git(*args, **kw):
    return subprocess.run(["git", *args], cwd=SITE, capture_output=True, text=True, **kw)


def deploy(summary):
    dirty = [l[3:] for l in git("status", "--porcelain").stdout.splitlines()]
    other = [f for f in dirty if not f.startswith(OUTPUTS)]
    if other:
        sys.exit("STOPPED before publishing: these files have uncommitted changes and are not this script's to commit:\n  "
                 + "\n  ".join(other) + "\nCommit (or undo) them first, then run this again. The site is rebuilt locally.")
    if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != "main":
        sys.exit("STOPPED before publishing: not on main")
    if not dirty:
        print("  nothing changed: the live site is already up to date")
        return
    git("add", "--", *[o.rstrip("/") for o in OUTPUTS], check=True)
    who = ["-c", f"user.name={git('log', '-1', '--format=%an').stdout.strip()}",
           "-c", f"user.email={git('log', '-1', '--format=%ae').stdout.strip()}"] if not git("config", "user.name").stdout.strip() else []
    msg = "Update the site from the operator's notes\n\n" + ("\n".join(summary) if summary else "Notes and data refreshed.")
    if os.environ.get("UPDATE_SITE_TRAILER"):  # e.g. a Co-Authored-By line, when someone else runs it for you
        msg += "\n\n" + os.environ["UPDATE_SITE_TRAILER"]
    r = subprocess.run(["git", *who, "commit", "-q", "-F", "-"], cwd=SITE, input=msg, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"STOPPED: git commit failed:\n{r.stderr}")
    r = git("push", "origin", "main")
    if r.returncode:
        sys.exit(f"STOPPED: the commit is made but the push failed (run 'git push origin main'):\n{r.stderr}")
    print(f"  pushed {git('log', '-1', '--format=%h').stdout.strip()} to main: the site redeploys in about a minute, {SITE_URL}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--no-deploy", action="store_true", help="check and rebuild, but do not commit or push")
    ap.add_argument("--offline", action="store_true", help="answer Hugging Face questions from build/cache, skip the Hub check")
    a = ap.parse_args()
    try:
        import pandas, pyarrow  # noqa: F401  (build_data.py needs them: run this with the lerobot venv's python)
    except ImportError:
        sys.exit("run it with the lerobot venv:  ~/lerobot/.venv/bin/python scripts/update_site.py")

    step("1. new recordings -> reports")
    days = stale_days()
    for day in days:
        print(f"  assessing {day}", flush=True)
        run([LR / ".venv/bin/python", "tools/assess_rollouts.py", "--day", day, "--json"], cwd=LR, quiet=True)
    if not days:
        print("  every rollout day's report is up to date")

    step("2. the recorded takes")
    run([PY, "scripts/build_data.py", "--rollouts-only", *(["--offline"] if a.offline else [])], quiet=True)
    print("  src/data/rollouts.json")

    step("3. notes -> yaml")
    yamls = []
    for txt in sorted((SITE / "notes").glob("*.txt")):
        model = model_of(txt)
        check_notes_text(txt)
        out = run([PY, "scripts/notes_to_yaml.py", txt, "--model", model, "--force"], quiet=True)
        print(f"  {txt.relative_to(SITE)} ({model}): " + next((l for l in out.splitlines() if " moves, " in l), "").strip())
        yamls.append(yaml.safe_load(txt.with_suffix(".yaml").read_text()))

    step("4. checks")
    for y in yamls:
        check_against_arm(y)
    if not a.offline:
        check_hub(yamls)
    print(f"  {len(warnings)} warning(s), listed at the end")

    step("5. rebuild the site")
    run([PY, "scripts/build_data.py", *(["--offline"] if a.offline else [])], quiet=True)
    run([PY, "scripts/make_clips.py"], quiet=True)
    run(["npx", "astro", "build"], env=node_env(), quiet=True)
    run([PY, "scripts/check_text.py", "dist"])

    step("6. the site against the notes")
    check_site(yamls)
    summary = changes()
    print("\n".join(f"  {s}" for s in summary) or "  no model's numbers changed")

    if warnings:
        step("warnings (worth a look; they did not stop anything)")
        print("\n".join(f"  - {w}" for w in warnings))

    step("7. publish")
    if a.no_deploy:
        print("  --no-deploy: rebuilt locally, nothing committed or pushed")
    else:
        deploy(summary)


if __name__ == "__main__":
    main()
