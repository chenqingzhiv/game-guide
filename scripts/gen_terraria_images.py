#!/usr/bin/env python3
"""Generate Terraria guide WebP infographics (1280x720) for game-guide.club.

Style: dark navy backgrounds, teal/green accents, flat rounded panels,
bold Arial titles. Mirrors the existing 1280x720 infographic look.
Text is auto-fitted so nothing overflows its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "terraria")
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

# Palette
BG_TOP = (14, 22, 40)
BG_BOTTOM = (20, 34, 58)
TEAL = (58, 200, 178)
GREEN = (110, 210, 120)
GOLD = (240, 200, 90)
RED = (235, 110, 100)
PURPLE = (170, 130, 235)
BLUE = (90, 160, 235)
ORANGE = (240, 150, 80)
PANEL_BG = (30, 46, 74)
PANEL_BG2 = (38, 56, 88)
TEXT = (235, 240, 248)
MUTED = (150, 168, 190)
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

def ctext(d, xy, text, fnt, fill=TEXT, anchor="mm"):
    d.text((xy[0] * SS, xy[1] * SS), text, font=fnt, fill=fill, anchor=anchor)

def save(img, name):
    img = img.resize((W, H), Image.LANCZOS)
    img.save(os.path.join(OUT, name), "WEBP", quality=90, method=6)
    print("wrote", os.path.join(OUT, name))

# ---------------------------------------------------------------- hero
def hero():
    img, d = canvas()
    # decorative floating blocks
    blocks = [(80, 90, 46, 46, GREEN), (160, 60, 40, 40, TEAL), (250, 100, 34, 34, GOLD),
              (980, 70, 46, 46, PURPLE), (1060, 100, 40, 40, ORANGE), (1150, 55, 34, 34, BLUE),
              (60, 560, 40, 40, BLUE), (150, 600, 34, 34, RED), (230, 570, 30, 30, TEAL),
              (1040, 590, 38, 38, GOLD), (1120, 560, 42, 42, GREEN), (1200, 610, 30, 30, PURPLE)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    # title
    ctext(d, (W / 2, 210), "TERRARIA", font(150, True), fill=WHITE)
    ctext(d, (W / 2, 330), "The Ultimate Beginner's Guide 2026", font(56, True), fill=TEAL)
    ctext(d, (W / 2, 400), "First Night  ·  Four Classes  ·  Full Boss Order  ·  1.4.5 Bigger & Boulder",
          font(34), fill=MUTED)
    # fact chips (auto-fit text)
    chips = ["15 Years", "1.4.5 Update", "4 Classes", "30+ Bosses", "6,000+ Items"]
    chip_w, gap = 240, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 470 * SS, (x + chip_w) * SS, 520 * SS), 16, fill=PANEL_BG, outline=TEAL, width=2)
        f = fit_font(chip, chip_w - 24, 28, bold=True)
        ctext(d, (x + chip_w / 2, 495), chip, f, fill=TEXT)
    ctext(d, (W / 2, 620), "Re-Logic  ·  Available on PC, Console, Switch & Mobile", font(26), fill=MUTED)
    save(img, "terraria-beginners-hero.webp")

# ---------------------------------------------------------------- first night
def first_night():
    img, d = canvas()
    ctext(d, (W / 2, 80), "Your First Night: Survive or Die", font(62, True), fill=WHITE)
    ctext(d, (W / 2, 140), "A full day is 15 minutes — night falls at 7:30 PM", font(30), fill=MUTED)

    steps = [
        ("1", "Chop Wood", "20-40 with your axe", GREEN),
        ("2", "Craft Workbench", "Unlocks every early recipe", TEAL),
        ("3", "Sword & Bow", "Zombies hit hard at night", ORANGE),
        ("4", "Mine Stone", "Furnace + mortar materials", BLUE),
        ("5", "Build a Shelter", "Walls, door, background walls", PURPLE),
        ("6", "Torches + Bed", "Light stops spawns; bed = spawn", GOLD),
    ]
    bw, bh, gx, gy = 384, 180, 26, 30
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 205
    for i, (num, title, sub, c) in enumerate(steps):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        # number badge (left, vertically centered)
        rrect(d, (x * SS, y * SS, (x + 84) * SS, (y + bh) * SS), 18, fill=c)
        rrect(d, ((x + 84 - 18) * SS, y * SS, (x + 84) * SS, (y + bh) * SS), 0, fill=PANEL_BG)
        ctext(d, (x + 42, y + bh / 2), num, font(50, True), fill=WHITE)
        # title + sub to the right
        tx = x + 112
        f = fit_font(title, bw - 130, 32, bold=True)
        ctext(d, (tx, y + 62), title, f, anchor="lm")
        fs = fit_font(sub, bw - 130, 22, bold=False)
        ctext(d, (tx, y + 118), sub, fs, anchor="lm", fill=MUTED)
    rrect(d, (x0 * SS, 640 * SS, (W - x0) * SS, 686 * SS), 16, fill=PANEL_BG2, outline=GOLD, width=2)
    ctext(d, (W / 2, 663), "Stay inside from 7:30 PM to 4:30 AM — fight from your doorway",
          fit_font("Stay inside from 7:30 PM to 4:30 AM — fight from your doorway", W - 2 * x0 - 40, 30, bold=True),
          fill=GOLD)
    save(img, "terraria-first-night.webp")

# ---------------------------------------------------------------- boss progression
def boss_prog():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Full Boss Order", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Pre-Hardmode  →  Wall of Flesh  →  Hardmode  →  Moon Lord", font(30), fill=MUTED)

    stages = [
        ("PRE-HARDMODE", GREEN, ["King Slime", "Eye of Cthulhu", "EoW / Brain", "Queen Bee", "Skeletron"]),
        ("HARDMODE", ORANGE, ["The Twins", "The Destroyer", "Skeletron Prime", "Plantera", "Golem"]),
        ("ENDGAME", PURPLE, ["Lunatic Cultist", "Celestial Pillars", "MOON LORD"]),
    ]
    panel_w, panel_h = 334, 330
    gap = 40
    x0 = (W - (panel_w * 3 + gap * 2)) / 2
    y0 = 200
    for i, (label, c, bosses) in enumerate(stages):
        x = x0 + i * (panel_w + gap)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + panel_h) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + 58) * SS), 18, fill=c)
        ctext(d, (x + panel_w / 2, y0 + 29), label, font(28, True), fill=WHITE)
        for j, b in enumerate(bosses):
            f = fit_font(b, panel_w - 24, 27, bold=True)
            ctext(d, (x + panel_w / 2, y0 + 112 + j * 44), b, f, fill=TEXT)
        if i < 2:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(44, True), fill=GOLD)
    rrect(d, (x0 * SS, 585 * SS, (W - x0) * SS, 650 * SS), 16, fill=PANEL_BG2, outline=GOLD, width=2)
    ctext(d, (W / 2, 600), "GATE:  Wall of Flesh  —  throw a Guide Voodoo Doll into lava",
          fit_font("GATE:  Wall of Flesh  —  throw a Guide Voodoo Doll into lava", W - 2 * x0 - 40, 28, bold=True),
          fill=GOLD)
    ctext(d, (W / 2, 640), "Beating it corrupts the world and unlocks Hardmode", font(24), fill=MUTED)
    save(img, "terraria-boss-progression.webp")

# ---------------------------------------------------------------- 1.4.5 update
def update():
    img, d = canvas()
    ctext(d, (W / 2, 78), "Terraria 1.4.5  ·  Bigger & Boulder", font(58, True), fill=WHITE)
    ctext(d, (W / 2, 138), "The biggest patch in years — out January 27, 2026", font(30), fill=MUTED)

    feats = [
        ("Crafting Overhaul", "New searchable, tabbed crafting UI", TEAL),
        ("Craft from Chests", "Use nearby storage automatically", GREEN),
        ("Skyblock Seed", "Tiny floating island challenge", BLUE),
        ("Dead Cells Crossover", "Flint, Barrel Launcher & more", RED),
        ("Palworld Crossover", "Cattiva, Chillet mounts, Digtoise", ORANGE),
        ("Crossplay Rollout", "PC + Mobile + servers in 2026", PURPLE),
    ]
    bw, bh, gx, gy = 384, 160, 26, 30
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 200
    for i, (title, sub, c) in enumerate(feats):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + 12) * SS, (y + bh) * SS), 18, fill=c)
        f = fit_font(title, bw - 44, 31, bold=True)
        ctext(d, (x + bw / 2, y + 50), title, f, fill=TEXT)
        fs = fit_font(sub, bw - 44, 24, bold=False)
        ctext(d, (x + bw / 2, y + 106), sub, fs, fill=MUTED)
    rrect(d, (x0 * SS, 585 * SS, (W - x0) * SS, 646 * SS), 16, fill=PANEL_BG2, outline=GOLD, width=2)
    ctext(d, (W / 2, 600), "Start a NEW world — most 1.4.5 items only appear there",
          fit_font("Start a NEW world — most 1.4.5 items only appear there", W - 2 * x0 - 40, 28, bold=True),
          fill=GOLD)
    ctext(d, (W / 2, 638), "650+ new items  ·  new slimes & whips  ·  bat / rat transformations", font(24), fill=MUTED)
    save(img, "terraria-1-4-5-update.webp")

hero()
first_night()
boss_prog()
update()
print("all images generated")
