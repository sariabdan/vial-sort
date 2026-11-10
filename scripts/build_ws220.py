#!/usr/bin/env python3
"""Coverage of the 220-demonstration set (src/data/ws220.json), read from the local dataset:

    python3 scripts/build_ws220.py            # needs ~/lerobot/data/vial-sort-ws220_canon

Counts demonstrations per move (source -> destination) from the prompts, and per recording batch from
meta/episode_sources.csv. Only counts and dates are written: no paths, no prompts.
"""
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT = Path.home() / "lerobot/data/vial-sort-ws220_canon"
info = json.load(open(ROOT / "meta/info.json"))
rows = list(csv.DictReader(open(ROOT / "meta/episode_sources.csv")))
PAT = re.compile(r"position (\d) of the (left|right) rack to (?:slot (\d) of the (left|right) rack|the bin)")
demos, batches = Counter(), {}
for r in rows:
    m = PAT.search(r["prompt"])
    s = m.group(2)[0].upper() + m.group(1)
    d = (m.group(4)[0].upper() + m.group(3)) if m.group(3) else "bin"
    demos[f"{s}->{d}"] += 1
    b = batches.setdefault(r["batch"], {"episodes": 0, "frames": 0, "dates": []})
    b["episodes"] += 1; b["frames"] += int(r["frames"])
    if r["recorded_at"]: b["dates"].append(r["recorded_at"][:10])
for b in batches.values():
    d = sorted(b.pop("dates")); b["first"], b["last"] = (d[0], d[-1]) if d else (None, None)
per_src, per_dst = Counter(), Counter()
for k, n in demos.items():
    s, d = k.split("->"); per_src[s] += n; per_dst[d] += n
same = sum(n for k, n in demos.items() if k.split("->")[1] != "bin" and k[0] == k.split("->")[1][0])
out = {
    "dataset": "vial-sort-ws220", "episodes": info["total_episodes"], "frames": info["total_frames"], "fps": info["fps"],
    "minutes": round(info["total_frames"] / info["fps"] / 60), "slots": ["L1","L2","L3","L4","L5","L6","R1","R2","R3","R4","R5","R6"],
    "heldout_sources": ["L2", "L5", "R2", "R5"], "heldout_destinations": ["L2", "L4", "L5", "R2", "R4", "R5"],
    "demos": dict(sorted(demos.items())), "moves": len(demos), "same_rack": same, "to_bin": per_dst["bin"],
    "per_source": dict(sorted(per_src.items())), "per_destination": dict(sorted(per_dst.items())), "batches": batches,
}
(Path(__file__).resolve().parents[1] / "src/data/ws220.json").write_text(json.dumps(out, indent=1))
print(out["episodes"], "episodes,", out["moves"], "moves,", same, "same-rack,", per_dst["bin"], "to the bin")
print(json.dumps(batches))
