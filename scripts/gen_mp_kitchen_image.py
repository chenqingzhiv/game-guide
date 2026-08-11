#!/usr/bin/env python3
"""Generate the missing Moonlight Peaks Kitchen Extension infographic (800x400).

Matching the existing MP infographic style: dark night-purple background,
warm cream text, green/gold accent panels.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "moonlight-peaks", "img")
W, H = 800, 400
SS = 2
SW, SH = W * SS, H * SS
FONT_DIR = r"C:\Windows\Fonts"

def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size * SS)

def tlen(text, fnt):
    b = fnt.getbbox(text)
    return (b[2] - b[0]) / SS

def fit(text, max_w, base_size, bold=False):
    for s in range(base_size, 9, -2):
        f = font(s, bold)
        if tlen(text, f) <= max_w:
            return f
    return font(9, bold)

BG = (32, 20, 49)
PANEL = (46, 32, 66)
CARD = (42, 28, 60)
GREEN = (110, 190, 110)
GOLD = (240, 200, 120)
CREAM = (238, 230, 220)
MUTED = (180, 165, 190)

img = Image.new("RGB", (SW, SH), BG)
d = ImageDraw.Draw(img)

# header
d.rectangle((0, 0, SW, 64 * SS), fill=PANEL)
d.text((W / 2 * SS, 32 * SS), "Kitchen Extension Upgrade", font=font(30, True), fill=CREAM, anchor="mm")

# two feature cards
labels = [
    ("2nd Cooking Slot", "Cook two dishes at once", GREEN),
    ("Bulk Cooking (2x-5x)", "Cook large batches fast", GOLD),
]
bw, bh = 340, 210
x0 = (W - (bw * 2 + 40)) // 2
y0 = 110
for i, (title, sub, c) in enumerate(labels):
    x = x0 + i * (bw + 40)
    d.rounded_rectangle((x * SS, y0 * SS, (x + bw) * SS, (y0 + bh) * SS), radius=16, fill=CARD)
    # cauldron icon
    cx, cy = x + bw // 2, y0 + 68
    d.ellipse(((cx - 46) * SS, (cy - 46) * SS, (cx + 46) * SS, (cy + 46) * SS), fill=c)
    d.ellipse(((cx - 30) * SS, (cy - 30) * SS, (cx + 30) * SS, (cy + 30) * SS), fill=CARD)
    f1 = fit(title, bw - 30, 26, True)
    d.text(((x + bw / 2) * SS, (y0 + 148) * SS), title, font=f1, fill=CREAM, anchor="mm")
    f2 = fit(sub, bw - 30, 19, False)
    d.text(((x + bw / 2) * SS, (y0 + 192) * SS), sub, font=f2, fill=MUTED, anchor="mm")

# footer
d.rounded_rectangle((60 * SS, 340 * SS, (W - 60) * SS, 375 * SS), radius=14, fill=PANEL)
f3 = fit("Build: 3,000g + 20 Wood + 10 Iron Bars", W - 140, 20, True)
d.text((W / 2 * SS, 357 * SS), "Build: 3,000g + 20 Wood + 10 Iron Bars", font=f3, fill=GOLD, anchor="mm")

img = img.resize((W, H), Image.LANCZOS)
img.save(os.path.join(OUT, "kitchen-extension.webp"), "WEBP", quality=90, method=6)
print("wrote", os.path.join(OUT, "kitchen-extension.webp"), os.path.getsize(os.path.join(OUT, "kitchen-extension.webp")), "bytes")
