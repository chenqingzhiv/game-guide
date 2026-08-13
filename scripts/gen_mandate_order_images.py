#!/usr/bin/env python3
"""Generate Mandate Order (烽沙) guide WebP infographics (1280x720) for game-guide.club.

Style: dark ink-wash umber backgrounds with cinnabar-red / bronze-gold / jade accents,
flat rounded panels, bold Arial titles. Mirrors the existing 1280x720 infographic
look. Text is auto-fitted so nothing overflows its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "mandate-order")
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

# Palette - ink-wash umber + warring-states cinnabar / bronze / jade
BG_TOP = (30, 22, 18)
BG_BOTTOM = (54, 32, 22)
CINNABAR = (198, 58, 44)
GOLD = (214, 176, 78)
JADE = (110, 168, 128)
BONE = (230, 224, 208)
MUTED = (168, 150, 132)
PANEL_BG = (50, 38, 30)
PANEL_BG2 = (68, 50, 38)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    # decorative floating blocks (banners / wall blocks / grain sacks)
    blocks = [(80, 90, 46, 46, CINNABAR), (160, 60, 40, 40, GOLD), (250, 100, 34, 34, JADE),
              (980, 70, 46, 46, GOLD), (1060, 100, 40, 40, CINNABAR), (1150, 55, 34, 34, JADE),
              (60, 560, 40, 40, JADE), (150, 600, 34, 34, CINNABAR), (230, 570, 30, 30, GOLD),
              (1040, 590, 38, 38, CINNABAR), (1120, 560, 42, 42, GOLD), (1200, 610, 30, 30, JADE)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    # title
    ctext(d, (W / 2, 200), "MANDATE ORDER", font(120, True), fill=WHITE)
    ctext(d, (W / 2, 315), "The Ultimate Beginner's Guide 2026", font(52, True), fill=GOLD)
    ctext(d, (W / 2, 383), "From a 30-person village to a Warring-State kingdom", font(32), fill=MUTED)
    # fact chips (auto-fit text)
    chips = ["Early Access", "City-Builder + RTS", "Ancient China", "Digital Sky", "UE5"]
    chip_w, gap = 246, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 455 * SS, (x + chip_w) * SS, 505 * SS), 16, fill=PANEL_BG, outline=GOLD, width=2)
        f = fit_font(chip, chip_w - 24, 28, bold=True)
        ctext(d, (x + chip_w / 2, 480), chip, f, fill=BONE)
    ctext(d, (W / 2, 610), "Manor Lords, but in ancient China — where farmers become soldiers",
          fit_font("Manor Lords, but in ancient China — where farmers become soldiers", W - 80, 27, bold=True),
          fill=MUTED)
    save(img, "mandate-order-hero.webp")

# ---------------------------------------------------------------- first hour
def first_hour():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Your First Hour: The 30-Person Village", font(58, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Thirty hands become a stable, growing settlement — in this order", font(29), fill=MUTED)

    steps = [
        ("1", "Worker Housing", "Empty homes pull in new 伍 squads", JADE),
        ("2", "Granary", "Food is the only growth cap that matters", GOLD),
        ("3", "Farmland", "Plant in spring, harvest in autumn", CINNABAR),
        ("4", "Water & Fuel", "Don't stall in the first winter", JADE),
        ("5", "Command Tent", "Start the 爵位 title grind early", GOLD),
        ("6", "A Short Wall", "Buy time before the first raid", CINNABAR),
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
    rrect(d, (x0 * SS, 636 * SS, (W - x0) * SS, 684 * SS), 16, fill=PANEL_BG2, outline=CINNABAR, width=2)
    ctext(d, (W / 2, 660), "Don't conscript yet — with 30 people, every soldier is a missing farmer",
          fit_font("Don't conscript yet — with 30 people, every soldier is a missing farmer", W - 2 * x0 - 40, 29, bold=True),
          fill=CINNABAR)
    save(img, "mandate-order-first-hour.webp")

# ---------------------------------------------------------------- schools
def schools():
    img, d = canvas()
    ctext(d, (W / 2, 76), "The Six Schools of Thought", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Recruit retainers (门客) — each school bends the whole game its way", font(29), fill=MUTED)

    corps = [
        ("CONFUCIAN", CINNABAR, "Best for beginners", "Actively supplies workers"),
        ("DAOIST", JADE, "Gathering", "Replenishes resource nodes"),
        ("MOHIST", GOLD, "Machine swarm", "Logs → siege engine parts"),
        ("LEGALIST", MUTED, "High-skill", "Copper-heavy, complex"),
        ("MILITARY", CINNABAR, "War support", "Double archer range"),
        ("AGRICULTURAL", JADE, "Reliable growth", "Heals every living soldier"),
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
    rrect(d, (x0 * SS, 560 * SS, (W - x0) * SS, 602 * SS), 16, fill=PANEL_BG2, outline=JADE, width=2)
    ctext(d, (W / 2, 581), "First run?  Pick CONFUCIAN  —  the population safety net",
          fit_font("First run?  Pick CONFUCIAN  —  the population safety net", W - 2 * x0 - 40, 25, bold=True),
          fill=JADE)
    rrect(d, (x0 * SS, 618 * SS, (W - x0) * SS, 666 * SS), 16, fill=PANEL_BG2, outline=GOLD, width=2)
    ctext(d, (W / 2, 642), "Branch later into MOHIST (siege economy) or AGRICULTURAL (farming state)",
          fit_font("Branch later into MOHIST (siege economy) or AGRICULTURAL (farming state)", W - 2 * x0 - 40, 27, bold=True),
          fill=GOLD)
    save(img, "mandate-order-schools.webp")

# ---------------------------------------------------------------- warfare
def warfare():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Walls, Armies & Siege Warfare", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Your workers are your army — and your wall design decides sieges", font(29), fill=MUTED)

    stages = [
        ("CONSCRIPT", CINNABAR, "Farmers → infantry, archers, chariots"),
        ("ARMORY", GOLD, "Produce weapons before you levy"),
        ("WALLS", JADE, "Free-form walls, gates & towers"),
        ("SIEGE", CINNABAR, "Ballistae & catapults break walls"),
    ]
    panel_w, panel_h = 262, 250
    gap = 34
    x0 = (W - (panel_w * 4 + gap * 3)) / 2
    y0 = 205
    for i, (label, c, desc) in enumerate(stages):
        x = x0 + i * (panel_w + gap)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + panel_h) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + 56) * SS), 18, fill=c)
        ctext(d, (x + panel_w / 2, y0 + 28), label, font(24, True), fill=WHITE)
        f = fit_font(desc, panel_w - 24, 25, bold=True)
        ctext(d, (x + panel_w / 2, y0 + 130), desc, f, fill=BONE)
        if i < 3:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(42, True), fill=GOLD)
    rrect(d, (x0 * SS, 505 * SS, (W - x0) * SS, 585 * SS), 16, fill=PANEL_BG2, outline=CINNABAR, width=2)
    ctext(d, (W / 2, 530), "Every soldier is a farmer who isn't farming",
          fit_font("Every soldier is a farmer who isn't farming", W - 2 * x0 - 40, 28, bold=True), fill=CINNABAR)
    ctext(d, (W / 2, 570), "Over-conscript and the granary empties ·  Under-conscript and the walls fall", font(25), fill=MUTED)
    save(img, "mandate-order-warfare.webp")

hero()
first_hour()
schools()
warfare()
print("all images generated")
