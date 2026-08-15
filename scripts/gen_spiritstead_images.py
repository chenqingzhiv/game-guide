#!/usr/bin/env python3
"""Generate Spiritstead guide WebP infographics (1280x720) for game-guide.club.

Style: warm cozy cream/sage background with forest-green / sky-blue / terracotta /
amber accents, flat rounded panels, bold Arial titles. Mirrors the existing
1280x720 infographic look. Text is auto-fitted so nothing overflows its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "spiritstead")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
SS = 2  # supersample factor for smooth edges
SW, SH = W * SS, H * SS

FONT_DIR = r"C:\Windows\Fonts"
_FONT_CACHE = {}

def font(size, bold=False):
    key = (size, bold)
    if key not in _FONT_CACHE:
        name = "arialbd.ttf" if bold else "arial.ttf"
        _FONT_CACHE[key] = ImageFont.truetype(os.path.join(FONT_DIR, name), size * SS)
    return _FONT_CACHE[key]

def tlen(text, fnt):
    b = fnt.getbbox(text)
    return (b[2] - b[0]) / SS

def fit_font(text, max_w, base_size, bold=False):
    """Return a font no larger than base_size whose text fits max_w."""
    for s in range(base_size, 10, -2):
        f = font(s, bold)
        if tlen(text, f) <= max_w:
            return f
    return font(10, bold)

# Palette — cozy cream/sage + forest / sky / terracotta / amber
BG_TOP = (253, 246, 232)
BG_BOTTOM = (212, 226, 202)
FOREST = (86, 130, 100)
SKY = (106, 152, 182)
TERRA = (214, 116, 82)
AMBER = (222, 168, 84)
BONE = (58, 52, 44)
MUTED = (122, 112, 96)
PANEL_BG = (255, 252, 244)
PANEL_BG2 = (240, 232, 214)
WHITE = (255, 255, 255)

def canvas():
    img = Image.new("RGB", (SW, SH), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(SH):
        t = y / SH
        c = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (SW, y)], fill=c)
    return img, d

def rrect(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=int(r * SS), fill=fill, outline=outline, width=width * SS)

def ctext(d, xy, text, fnt, fill=BONE, anchor="mm"):
    d.text((xy[0] * SS, xy[1] * SS), text, font=fnt, fill=fill, anchor=anchor)

def save(img, name):
    img = img.resize((W, H), Image.LANCZOS)
    img.save(os.path.join(OUT, name), "WEBP", quality=90, method=6)
    print("wrote", os.path.join(OUT, name))

# ---------------------------------------------------------------- hero
def hero():
    img, d = canvas()
    # decorative floating blocks (homes / flower beds / spirit orbs)
    blocks = [(80, 90, 46, 46, FOREST), (160, 60, 40, 40, AMBER), (250, 100, 34, 34, TERRA),
              (980, 70, 46, 46, SKY), (1060, 100, 40, 40, AMBER), (1150, 55, 34, 34, FOREST),
              (60, 560, 40, 40, SKY), (150, 600, 34, 34, TERRA), (230, 570, 30, 30, FOREST),
              (1040, 590, 38, 38, SKY), (1120, 560, 42, 42, AMBER), (1200, 610, 30, 30, TERRA)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    # title
    ctext(d, (W / 2, 195), "SPIRITSTEAD", font(118, True), fill=BONE)
    ctext(d, (W / 2, 310), "The Cozy Beginner's Guide 2026", font(50, True), fill=TERRA)
    ctext(d, (W / 2, 378), "35 hidden spirits slowly turn your village into a machine", font(32), fill=MUTED)
    # fact chips (auto-fit text)
    chips = ["Full Release", "Cozy City-Builder", "Hand-Drawn", "Turbo Dog Games", "$9.99"]
    chip_w, gap = 246, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 450 * SS, (x + chip_w) * SS, 500 * SS), 16, fill=PANEL_BG, outline=FOREST, width=2)
        f = fit_font(chip, chip_w - 24, 28, bold=True)
        ctext(d, (x + chip_w / 2, 475), chip, f, fill=BONE)
    ctext(d, (W / 2, 610), "Stardew's calm, with a tiny automation puzzle at the heart",
          fit_font("Stardew's calm, with a tiny automation puzzle at the heart", W - 80, 27, bold=True),
          fill=FOREST)
    save(img, "spiritstead-hero.webp")

# ---------------------------------------------------------------- first hour
def first_hour():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Your First Hour: The Cozy Priority Order", font(56, True), fill=BONE)
    ctext(d, (W / 2, 136), "Build, assign, stockpile, and summon your first spirit — in this order", font(29), fill=MUTED)

    steps = [
        ("1", "Homes First", "Sleeping villagers grow your population", FOREST),
        ("2", "Everyone to Work", "Farming plots + sawmill = food & wood", SKY),
        ("3", "Stockpile Food", "Build fences, eggs pile up fast", TERRA),
        ("4", "Happiness Boosters", "Bonfire, bench, flowers — cheap to build", AMBER),
        ("5", "Summon Peppok", "Hold a chicken over a lit bonfire", FOREST),
        ("6", "Don't Over-Manage", "Early pace is slow — trust the loop", SKY),
    ]
    bw, bh, gx, gy = 384, 180, 26, 30
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 205
    for i, (num, title, sub, c) in enumerate(steps):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + 84) * SS, (y + bh) * SS), 18, fill=c)
        rrect(d, ((x + 84 - 18) * SS, y * SS, (x + 84) * SS, (y + bh) * SS), 0, fill=PANEL_BG)
        ctext(d, (x + 42, y + bh / 2), num, font(50, True), fill=WHITE)
        tx = x + 112
        f = fit_font(title, bw - 130, 32, bold=True)
        ctext(d, (tx, y + 62), title, f, anchor="lm")
        fs = fit_font(sub, bw - 130, 22, bold=False)
        ctext(d, (tx, y + 118), sub, fs, anchor="lm", fill=MUTED)
    rrect(d, (x0 * SS, 636 * SS, (W - x0) * SS, 684 * SS), 16, fill=PANEL_BG2, outline=TERRA, width=2)
    ctext(d, (W / 2, 660), "The slow first hour is the setup — spirits are the reward",
          fit_font("The slow first hour is the setup — spirits are the reward", W - 2 * x0 - 40, 29, bold=True),
          fill=TERRA)
    save(img, "spiritstead-first-hour.webp")

# ---------------------------------------------------------------- spirits
def spirits():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Summon the Spirits", font(62, True), fill=BONE)
    ctext(d, (W / 2, 136), "35 hidden helpers — each has a strange ritual. Assign them right and your town runs itself", font(28), fill=MUTED)

    corps = [
        ("PEPPOK", TERRA, "Chicken over a bonfire", "First spirit · fire friend"),
        ("NIBBIN", SKY, "Reach the Spirit Temple", "Collects resources"),
        ("WOOLY", AMBER, "Sheep into the portal", "Auto-collects wool"),
        ("YOLKOS", FOREST, "Chicken into the pantry", "Auto-collects eggs"),
        ("BLUJI", SKY, "Plant 5 Grim Trees", "Auto-collects eggs"),
        ("PLOP", FOREST, "3 Swamp Reliefs", "Cleans up the village"),
    ]
    bw, bh, gx, gy = 384, 150, 26, 26
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 190
    for i, (label, c, sub, extra) in enumerate(corps):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 46) * SS), 18, fill=c)
        rrect(d, (x * SS, (y + 46 - 18) * SS, (x + bw) * SS, (y + 46) * SS), 0, fill=PANEL_BG)
        ctext(d, (x + bw / 2, y + 23), label, font(24, True), fill=WHITE)
        f = fit_font(sub, bw - 24, 27, bold=True)
        ctext(d, (x + bw / 2, y + 78), sub, f, fill=BONE)
        fs = fit_font(extra, bw - 24, 21, bold=False)
        ctext(d, (x + bw / 2, y + 122), extra, fs, fill=MUTED)
    rrect(d, (x0 * SS, 560 * SS, (W - x0) * SS, 602 * SS), 16, fill=PANEL_BG2, outline=FOREST, width=2)
    ctext(d, (W / 2, 581), "Most spirits also mine Mushies, Moonstones & Crystals — or staff a Wizard Tower",
          fit_font("Most spirits also mine Mushies, Moonstones & Crystals — or staff a Wizard Tower", W - 2 * x0 - 40, 25, bold=True),
          fill=FOREST)
    rrect(d, (x0 * SS, 618 * SS, (W - x0) * SS, 666 * SS), 16, fill=PANEL_BG2, outline=AMBER, width=2)
    ctext(d, (W / 2, 642), "Collect them all — assigning the right spirits makes your town run itself",
          fit_font("Collect them all — assigning the right spirits makes your town run itself", W - 2 * x0 - 40, 27, bold=True),
          fill=AMBER)
    save(img, "spiritstead-spirits.webp")

# ---------------------------------------------------------------- biomes
def biomes():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Three Biomes, One Sanctuary", font(60, True), fill=BONE)
    ctext(d, (W / 2, 136), "Expand through the portals to restore the Grand Spirit Sanctuary", font(29), fill=MUTED)

    stages = [
        ("GREEN FOREST", FOREST, "Your starting home — first spirits & temples"),
        ("SNOW", SKY, "Winter Portal · new buildings, spirits, resources"),
        ("SWAMP", TERRA, "Swamp Portal · frogs, Grim Trees, Plop"),
        ("SANCTUARY", AMBER, "Restore it to rebalance spirits & humans"),
    ]
    panel_w, panel_h = 262, 250
    gap = 34
    x0 = (W - (panel_w * 4 + gap * 3)) / 2
    y0 = 205
    for i, (label, c, desc) in enumerate(stages):
        x = x0 + i * (panel_w + gap)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + panel_h) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + 56) * SS), 18, fill=c)
        ctext(d, (x + panel_w / 2, y0 + 28), label, font(22, True), fill=WHITE)
        f = fit_font(desc, panel_w - 24, 24, bold=True)
        ctext(d, (x + panel_w / 2, y0 + 130), desc, f, fill=BONE)
        if i < 3:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(42, True), fill=TERRA)
    rrect(d, (x0 * SS, 505 * SS, (W - x0) * SS, 585 * SS), 16, fill=PANEL_BG2, outline=FOREST, width=2)
    ctext(d, (W / 2, 530), "Adventure Mode is a tight 3–8 hours; Creative Mode is where you stay",
          fit_font("Adventure Mode is a tight 3–8 hours; Creative Mode is where you stay", W - 2 * x0 - 40, 28, bold=True), fill=FOREST)
    ctext(d, (W / 2, 570), "No diplomacy · No tech tree · No war — just a cozy village that learns to live", font(25), fill=MUTED)
    save(img, "spiritstead-biomes.webp")

hero()
first_hour()
spirits()
biomes()
print("all images generated")
