#!/usr/bin/env python3
"""Label the October rig photo (~/lerobot/oct_sep_setup.jpeg) -> public/img/setup_current.webp.

Same style as ~/lerobot/ee/annotate_setup_v5.py. Boxes are (x0, y0, x1, y1) on the 1362x1599 photo.
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SITE = Path(__file__).resolve().parents[1]
SRC = Path(os.environ.get("LEROBOT", Path.home() / "lerobot")) / "oct_sep_setup.jpeg"
im = Image.open(SRC).convert("RGB")
W, H = im.size
d = ImageDraw.Draw(im)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = lambda n: ImageFont.truetype(FONT, n) if os.path.exists(FONT) else ImageFont.load_default()


def box(xyxy, color, label, side="above", sz=34, lw=6):
    d.rectangle(xyxy, outline=color, width=lw)
    f = font(sz)
    tw, th = d.textlength(label, font=f), sz + 10
    x0, y0, x1, y1 = xyxy
    lx = min(max(2, x0), W - tw - 16)
    ly = y0 - th - 2 if side == "above" else y1 + 2
    ly = max(2, min(ly, H - th - 2))
    d.rectangle([lx, ly, lx + tw + 14, ly + th], fill=color)
    d.text((lx + 7, ly + 4), label, fill="white", font=f)


CAM, RACK, BIN, ARM = "#0a8a55", "#e08a29", "#1f6fb2", "#7b5aa6"
box((468, 45, 545, 125), CAM, "camera", "below")
box((650, 112, 805, 208), CAM, "overhead camera", "above")
box((885, 370, 990, 440), CAM, "RealSense camera", "below")
box((1138, 272, 1245, 390), CAM, "camera", "below")
box((250, 950, 345, 1045), CAM, "wrist camera", "below", sz=30)
box((210, 695, 535, 870), RACK, "rack", "above")
box((608, 765, 802, 1092), RACK, "rack", "above")
box((315, 805, 655, 1130), BIN, "bin", "above")
box((130, 865, 415, 1460), ARM, "follower arm", "above")
box((955, 1195, 1305, 1599), "#c1553b", "leader arm (teleop)", "above")

out = SITE / "public/img/setup_current.webp"
im.save(out, "WEBP", quality=84, method=6)
print(out, im.size)
