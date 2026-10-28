#!/usr/bin/env python3
"""Cut the site's videos out of the recordings: H.264 (every browser, Safari included), posters,
and src/data/media.json with each clip's size, length and the moments the rack animation needs.

    ~/lerobot/.venv/bin/python scripts/make_clips.py           # after scripts/build_data.py
    ~/lerobot/.venv/bin/python scripts/make_clips.py --force   # re-encode clips that exist

Reads build/clips.json (where every take and capture lives on disk), curation.yaml (which ones
the pages show) and src/data/rollouts.json (grasp and release frames). Writes public/media/.
LeRobot v3 packs many episodes into one AV1 file per camera; a take is the span from its
from_timestamp, as in ~/lerobot/ee/extract_episode_clips.py.
"""

import argparse
import json
import os
import subprocess
from pathlib import Path

import pandas as pd
import yaml

SITE = Path(__file__).resolve().parents[1]
LR = Path(os.environ.get("LEROBOT", Path.home() / "lerobot"))
MEDIA = SITE / "public/media"
FPS = 30
TOP_CROP = "crop=360:360:40:10"  # the table, arm and both racks in the 640x480 top-down view
H264 = ["-c:v", "libx264", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an"]
LEAD, TAIL = 2.5, 2.5  # seconds kept before the first grasp and after the last release

# Every feed a session recorded goes into its clip: five cameras as one large overhead view beside a 2 x 2
# block, two cameras side by side. Each feed carries its name so a reader can tell them apart.
CAM_ORDER = ["top_down", "left_top", "left_bottom", "right", "wrist"]
CAM_NAMES = {"top_down": "Overhead", "left_top": "Across the table", "left_bottom": "Near eye level",
             "right": "From the side", "wrist": "On the gripper", "left": "Across the table, re-aimed", "scene": "Scene"}
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def feed_graph(cams):
    """(ordered cams, filter_complex) putting every feed on one 960 x 360 canvas, inputs numbered in that order."""
    cams = [c for c in CAM_ORDER if c in cams] + [c for c in cams if c not in CAM_ORDER]
    five = len(cams) == 5 and cams[0] == "top_down"
    sizes = [(480, 360)] + [(240, 180)] * 4 if five else [(960 // len(cams), 360)] * len(cams)
    label = lambda c, h: (f"drawtext=fontfile={FONT}:text='{CAM_NAMES.get(c, c)}':x=8:y=h-th-8:fontsize={15 if h > 200 else 12}:"
                          f"fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=4")
    parts = [f"[{k}:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,{label(c, h)}[v{k}]"
             for k, (c, (w, h)) in enumerate(zip(cams, sizes))]
    if five:
        layout = "0_0|480_0|720_0|480_180|720_180"
    else:
        layout = "|".join(f"{sum(w for w, _ in sizes[:k])}_0" for k in range(len(cams)))
    parts.append(f"{''.join(f'[v{k}]' for k in range(len(cams)))}xstack=inputs={len(cams)}:layout={layout}[v]")
    return cams, ";".join(parts)


def ffmpeg(args, out, force):
    if out.exists() and not force:
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, str(out)], check=True)


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height:format=duration", "-of", "json", str(path)],
                       capture_output=True, text=True, check=True)
    j = json.loads(r.stdout)
    return {"w": j["streams"][0]["width"], "h": j["streams"][0]["height"], "secs": round(float(j["format"]["duration"]), 2)}


def rel(path):
    return str(path.relative_to(SITE / "public"))


def window(take):
    """(start, end) in seconds within the take: idle time before the first grasp and after
    the last release is cut, so a clip starts when the arm is about to act."""
    holds = take["holds"]
    if not holds:
        return 0.0, take["secs"]
    first = holds[0]["grasp"] / FPS
    if holds[-1]["release"] is None:  # never let go: the carry is the point, keep it to the end
        return max(0.0, first - LEAD), take["secs"]
    return max(0.0, first - LEAD), min(take["secs"], holds[-1]["release"] / FPS + TAIL)


def crop_filter(c):
    """ffmpeg crop of a fraction of the frame: {x, y, w, h} in 0..1, even pixel sizes."""
    f = lambda v, side: f"trunc(({side}*{v})/2)*2"
    return f"crop={f(c['w'], 'iw')}:{f(c['h'], 'ih')}:{f(c['x'], 'iw')}:{f(c['y'], 'ih')}"


def take_clip(take, src, cams, out, force, crf=26, crop=None, grid=False):
    a, b = window(take)
    if grid:  # every recorded feed on one canvas
        cams, graph = feed_graph(list(src["cams"]))
        ins = []
        for cam in cams:
            video, t0 = src["cams"][cam]
            ins += ["-ss", f"{t0 + a:.3f}", "-t", f"{b - a:.3f}", "-i", video]
        ffmpeg([*ins, "-filter_complex", graph, "-map", "[v]", *H264, "-crf", str(crf)], out, force)
        return a, b, cams
    ins, filt = [], []
    for k, cam in enumerate(cams):
        video, t0 = src["cams"][cam]
        ins += ["-ss", f"{t0 + a:.3f}", "-t", f"{b - a:.3f}", "-i", video]
        # side by side, every camera is 360 px tall; a single camera keeps its own size
        fit = crop_filter(crop) if crop else TOP_CROP if cam == "top_down" else ("scale=480:360" if len(cams) > 1 else "null")
        filt.append(f"[{k}:v]{fit},setsar=1[v{k}]")
    graph = ";".join(filt) + (f";{''.join(f'[v{k}]' for k in range(len(cams)))}hstack=inputs={len(cams)}[v]" if len(cams) > 1 else "")
    ffmpeg([*ins, "-filter_complex", graph, "-map", "[v]" if len(cams) > 1 else "[v0]", *H264, "-crf", str(crf)], out, force)
    return a, b, cams


def dataset_clip(root, episode, cams, out, force, crf=26):
    """A whole episode of a LeRobot v3 dataset with every camera on one canvas."""
    eps = pd.read_parquet(Path(root) / "meta/episodes")
    row = eps[eps.episode_index == episode].iloc[0]
    cams, graph = feed_graph(cams)
    ins = []
    for cam in cams:
        key = f"observation.images.{cam}"
        video = Path(root) / f"videos/{key}/chunk-{int(row[f'videos/{key}/chunk_index']):03d}/file-{int(row[f'videos/{key}/file_index']):03d}.mp4"
        t0, t1 = float(row[f"videos/{key}/from_timestamp"]), float(row[f"videos/{key}/to_timestamp"])
        ins += ["-ss", f"{t0:.3f}", "-t", f"{t1 - t0:.3f}", "-i", str(video)]
    ffmpeg([*ins, "-filter_complex", graph, "-map", "[v]", *H264, "-crf", str(crf)], out, force)


def poster(video, at, out, force):
    ffmpeg(["-ss", f"{at:.2f}", "-i", str(video), "-frames:v", "1", "-q:v", "3"], out, force)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-encode clips that already exist")
    a = ap.parse_args()
    cur = yaml.safe_load((SITE / "curation.yaml").read_text())
    clips = {c["id"]: c for c in json.loads((SITE / "build/clips.json").read_text())}
    sessions = json.loads((SITE / "src/data/rollouts.json").read_text())["sessions"]
    takes = {t["id"]: t for s in sessions for t in s["takes"]}
    session_of = {t["id"]: s for s in sessions for t in s["takes"]}
    by_run = {m["run"]: m for m in yaml.safe_load((SITE / "models.yaml").read_text())["models"]}
    media = {"featured": [], "captures": {}, "gallery": {}}

    def which(take_id):
        """(model, results row key) of a rollout, the same key scripts/build_data.py gives its row."""
        s = session_of[take_id]
        m = by_run[s["run"]]
        return m, f"{m['id']}-{s['step']}-{s['mode']}{'-ema' if s['ema'] else ''}"

    # hero: one camera, real time, cut to the move
    h = cur["hero"]
    take = takes[h["take"]]
    out = MEDIA / "hero.mp4"
    start, end, _ = take_clip(take, clips[h["take"]], [h["cam"]], out, a.force, crf=23, crop=h.get("crop"))
    grasp = take["holds"][0]["grasp"] / FPS - start
    release = (take["holds"][-1]["release"] or take["holds"][-1]["grasp"]) / FPS - start
    poster(out, release + 0.6, MEDIA / "hero.jpg", a.force)
    media["hero"] = {"take": h["take"], "task": take["task"], "move": take["move"], "cam": h["cam"],
                     "caption": h["caption"].format(name=which(h["take"])[0]["name"]), "src": rel(out), "poster": rel(MEDIA / "hero.jpg"), **probe(out),
                     "grasp": round(grasp, 2), "release": round(release, 2)}

    # featured rollouts: every feed the session recorded on one canvas
    for f in cur.get("featured") or []:
        take, out = takes[f["take"]], MEDIA / "takes" / f"{f['take']}.mp4"
        start, _, used = take_clip(take, clips[f["take"]], None, out, a.force, crf=28, grid=True)
        first = take["holds"][0]["grasp"] / FPS - start if take["holds"] else 1.0
        poster(out, first + 0.3, out.with_suffix(".jpg"), a.force)
        m, row = which(f["take"])
        media["featured"].append({"take": f["take"], "model": m["family"], "model_id": m["id"], "row": row, "used": used,
                                  "move": take["move"], "stage": take["stage"], "caption": f["caption"].format(name=m["name"]),
                                  "vial": f.get("vial"), "at": f.get("at"), "miss": f.get("miss"), "src": rel(out),
                                  "poster": rel(out.with_suffix(".jpg")), **probe(out)})

    # v5 eval captures: the referee's 3-camera recording (side | top | wrist) of every scored run
    for cid, c in clips.items():
        if c["kind"] != "capture":
            continue
        out = MEDIA / "v5" / f"{cid[3:]}.mp4"
        ffmpeg(["-i", c["src"], *H264, "-crf", "28"], out, a.force)
        info = probe(out)
        poster(out, info["secs"] * 0.55, out.with_suffix(".jpg"), a.force)
        media["captures"][cid[3:]] = {"src": rel(out), "poster": rel(out.with_suffix(".jpg")), **info}
    # the results gallery: the side camera alone, cut out of the capture (side | top | wrist)
    for stage, cid in (cur.get("gallery") or {}).items():
        src = MEDIA / "v5" / f"{cid[3:]}.mp4"
        out = MEDIA / "gallery" / f"{cid[3:]}.mp4"
        w, h = media["captures"][cid[3:]]["w"], media["captures"][cid[3:]]["h"]
        ffmpeg(["-i", str(src), "-vf", f"crop={w // 3 // 2 * 2}:{h}:0:0", *H264, "-crf", "26"], out, a.force)
        info = probe(out)
        poster(out, info["secs"] * 0.55, out.with_suffix(".jpg"), a.force)
        media["gallery"][stage] = {"capture": cid[3:], "src": rel(out), "poster": rel(out.with_suffix(".jpg")), **info}

    # one teleoperated demonstration for the datasets page
    d = cur.get("demo")
    if d:
        out = MEDIA / "demo.mp4"
        ffmpeg(["-i", str(LR / d["file"]), *H264, "-crf", "26"], out, a.force)
        info = probe(out)
        poster(out, info["secs"] * 0.4, MEDIA / "demo.jpg", a.force)
        media["demo"] = {"caption": d["caption"], "src": rel(out), "poster": rel(MEDIA / "demo.jpg"), **info}

    # one demonstration of the October set, as recorded, all five feeds
    w = cur.get("ws100_demo")
    if w:
        out = MEDIA / "demo_ws100.mp4"
        dataset_clip(LR / "data/vial-sort-ws100", w["episode"], CAM_ORDER, out, a.force)
        info = probe(out)
        poster(out, info["secs"] * 0.5, MEDIA / "demo_ws100.jpg", a.force)
        media["demo_ws100"] = {"caption": w["caption"], "episode": w["episode"], "src": rel(out),
                               "poster": rel(MEDIA / "demo_ws100.jpg"), **info}

    (SITE / "src/data/media.json").write_text(json.dumps(media, indent=1, ensure_ascii=False) + "\n")
    size = sum(p.stat().st_size for p in MEDIA.rglob("*") if p.is_file())
    print(f"public/media: {size / 1e6:.0f} MB in {sum(1 for p in MEDIA.rglob('*.mp4'))} videos; src/data/media.json")


if __name__ == "__main__":
    main()
