#!/usr/bin/env python3
"""One frame from each of the five cameras at the same instant of a demonstration.

    ~/lerobot/.venv/bin/python scripts/make_cams.py [--episode 10] [--at 0.55]

Reads the WS100 dataset (~/lerobot/data/vial-sort-ws100, LeRobot v3: many episodes per AV1 file,
cut by from_timestamp) and writes public/img/cams/<camera>.webp. `--at` is the fraction of the
episode; the default catches the vial in the gripper. The captions live in the page, not the image.
"""

import argparse
import os
import subprocess
from pathlib import Path

import pandas as pd
from PIL import Image

SITE = Path(__file__).resolve().parents[1]
LR = Path(os.environ.get("LEROBOT", Path.home() / "lerobot"))
ROOT = LR / "data/vial-sort-ws100"
OUT = SITE / "public/img/cams"
CAMS = ["top_down", "left_top", "left_bottom", "right", "wrist"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episode", type=int, default=10)
    ap.add_argument("--at", type=float, default=0.55)
    a = ap.parse_args()
    eps = pd.read_parquet(ROOT / "meta/episodes")
    row = eps[eps.episode_index == a.episode].iloc[0]
    OUT.mkdir(parents=True, exist_ok=True)
    for cam in CAMS:
        k = f"observation.images.{cam}"
        video = ROOT / f"videos/{k}/chunk-{int(row[f'videos/{k}/chunk_index']):03d}/file-{int(row[f'videos/{k}/file_index']):03d}.mp4"
        t0, t1 = float(row[f"videos/{k}/from_timestamp"]), float(row[f"videos/{k}/to_timestamp"])
        png = OUT / f"{cam}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0 + a.at * (t1 - t0):.3f}", "-i", str(video),
                        "-frames:v", "1", str(png)], check=True)
        Image.open(png).convert("RGB").save(OUT / f"{cam}.webp", "WEBP", quality=80, method=6)
        png.unlink()
        print(f"  public/img/cams/{cam}.webp")


if __name__ == "__main__":
    main()
