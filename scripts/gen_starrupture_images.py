#!/usr/bin/env python3
"""Generate StarRupture guide WebP infographics (1280x720) for game-guide.club.

Style: deep-space navy backgrounds with amber/orange "Ruptura star" accents,
flat rounded panels, bold Arial titles. Mirrors the existing 1280x720
infographic look. Text is auto-fitted so nothing overflows its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "starrupture")
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

# Palette — deep space navy + Ruptura amber/orange
BG_TOP = (12, 14, 30)
BG_BOTTOM = (24, 20, 40)
AMBER = (255, 176, 64)
ORANGE = (245, 130, 50)
RED = (235, 105, 90)
TEAL = (90, 210, 200)
GREEN = (120, 215, 130)
BLUE = (100, 165, 240)
PURPLE = (180, 140, 235)
PANEL_BG = (30, 28, 52)
PANEL_BG2 = (40, 36, 64)
TEXT = (236, 238, 246)
MUTED = (160, 165, 190)
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
    # decorative floating blocks (factory pods / ore chunks)
    blocks = [(80, 90, 46, 46, GREEN), (160, 60, 40, 40, TEAL), (250, 100, 34, 34, AMBER),
              (980, 70, 46, 46, PURPLE), (1060, 100, 40, 40, ORANGE), (1150, 55, 34, 34, BLUE),
              (60, 560, 40, 40, BLUE), (150, 600, 34, 34, RED), (230, 570, 30, 30, TEAL),
              (1040, 590, 38, 38, AMBER), (1120, 560, 42, 42, GREEN), (1200, 610, 30, 30, PURPLE)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    # title
    ctext(d, (W / 2, 205), "STARRUPTURE", font(140, True), fill=WHITE)
    ctext(d, (W / 2, 322), "The Ultimate Beginner's Guide 2026", font(54, True), fill=AMBER)
    ctext(d, (W / 2, 390), "Survive the Ruptures  ·  Automate Your First Factory  ·  Arcadia-7",
          font(33), fill=MUTED)
    # fact chips (auto-fit text)
    chips = ["Early Access", "Factory + Survival", "4P Co-op", "Arcadia-7", "Creepy Jar"]
    chip_w, gap = 246, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 460 * SS, (x + chip_w) * SS, 510 * SS), 16, fill=PANEL_BG, outline=AMBER, width=2)
        f = fit_font(chip, chip_w - 24, 28, bold=True)
        ctext(d, (x + chip_w / 2, 485), chip, f, fill=TEXT)
    ctext(d, (W / 2, 612), "Satisfactory meets Factorio on a hostile alien planet — out now on Steam",
          fit_font("Satisfactory meets Factorio on a hostile alien planet — out now on Steam", W - 80, 27, bold=True),
          fill=MUTED)
    save(img, "starrupture-beginners-hero.webp")

# ---------------------------------------------------------------- first hour
def first_hour():
    img, d = canvas()
    ctext(d, (W / 2, 80), "Your First Hour: Base, Power & Ore", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 140), "The goal is one working automation loop before the first big wave", font(29), fill=MUTED)

    steps = [
        ("1", "Drop Your Base Core", "Expand build range early", GREEN),
        ("2", "Solar Generator v.1", "Power = everything works", AMBER),
        ("3", "Mine Titanium & Wolfram", "Clear Training Level 2", TEAL),
        ("4", "Ore Excavator Loop", "Excavator → Rail → Storage", BLUE),
        ("5", "Smelter Line", "2 ore → 2 bars, 60/min", PURPLE),
        ("6", "Push Selenian Lv2", "Unlock the Fabricator", ORANGE),
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
    rrect(d, (x0 * SS, 636 * SS, (W - x0) * SS, 684 * SS), 16, fill=PANEL_BG2, outline=AMBER, width=2)
    ctext(d, (W / 2, 660), "Carry an emergency kit: 1 Meteor Heart + 100 Basic Building Materials",
          fit_font("Carry an emergency kit: 1 Meteor Heart + 100 Basic Building Materials", W - 2 * x0 - 40, 29, bold=True),
          fill=AMBER)
    save(img, "starrupture-first-hour.webp")

# ---------------------------------------------------------------- corporations
def corporations():
    img, d = canvas()
    ctext(d, (W / 2, 76), "The 5 Corporations", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Level them by exporting materials — don't burn Data Points here", font(29), fill=MUTED)

    corps = [
        ("MOON ENERGY", AMBER, "Power + Map", "Recipe Station, Map (Lv3)"),
        ("SELENIAN", ORANGE, "Materials", "Fabricator (Lv2), Furnace"),
        ("CLEVER ROBOTICS", BLUE, "Logistics", "OCL, Rails, Building Drone"),
        ("GRIFFITS BLUE", RED, "Combat", "Pistol (Lv2), Turrets"),
        ("FUTURE HEALTH", TEAL, "Survival", "Regen Chamber, Food Station"),
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
        ctext(d, (x + bw / 2, y + 23), label, font(26, True), fill=WHITE)
        f = fit_font(sub, bw - 24, 27, bold=True)
        ctext(d, (x + bw / 2, y + 78), sub, f, fill=TEXT)
        fs = fit_font(extra, bw - 24, 21, bold=False)
        ctext(d, (x + bw / 2, y + 122), extra, fs, fill=MUTED)
    # Training is the tutorial track (separate from the five main corporations)
    rrect(d, (x0 * SS, 560 * SS, (W - x0) * SS, 602 * SS), 16, fill=PANEL_BG2, outline=GREEN, width=2)
    ctext(d, (W / 2, 581), "Tutorial:  Training  unlocks Solar Generator v.1, Ore Excavator & Smelter (first hour only)",
          fit_font("Tutorial:  Training  unlocks Solar Generator v.1, Ore Excavator & Smelter (first hour only)", W - 2 * x0 - 40, 25, bold=True),
          fill=GREEN)
    rrect(d, (x0 * SS, 618 * SS, (W - x0) * SS, 666 * SS), 16, fill=PANEL_BG2, outline=AMBER, width=2)
    ctext(d, (W / 2, 642), "First targets:  Moon Energy Lv3 (Map)  →  Selenian Lv2 (Fabricator)  →  Griffits Blue Lv2 (Pistol)",
          fit_font("First targets:  Moon Energy Lv3 (Map)  →  Selenian Lv2 (Fabricator)  →  Griffits Blue Lv2 (Pistol)", W - 2 * x0 - 40, 27, bold=True),
          fill=AMBER)
    save(img, "starrupture-corporations.webp")

# ---------------------------------------------------------------- automation loop
def automation_loop():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Automation 101: The Core Loop", font(60, True), fill=WHITE)
    ctext(d, (W / 2, 136), "Ore Excavator  →  Rails  →  Smelter  →  Rails  →  Fabricator  →  Storage / OCL", font(29), fill=MUTED)

    stages = [
        ("ORE EXCAVATOR", GREEN, "Auto-mines Titanium, Wolfram & Calcium"),
        ("SMELTER", AMBER, "2 ore → 2 bars · 60/min"),
        ("FABRICATOR", ORANGE, "1 Ti + 1 W → 10 BBM"),
        ("ORBITAL LAUNCHER", BLUE, "Ship goods to corporations"),
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
        ctext(d, (x + panel_w / 2, y0 + 130), desc, f, fill=TEXT)
        if i < 3:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(42, True), fill=AMBER)
    rrect(d, (x0 * SS, 505 * SS, (W - x0) * SS, 585 * SS), 16, fill=PANEL_BG2, outline=GREEN, width=2)
    ctext(d, (W / 2, 530), "Power is the real bottleneck",
          fit_font("Power is the real bottleneck", W - 2 * x0 - 40, 28, bold=True), fill=GREEN)
    ctext(d, (W / 2, 570), "Red lights = underpowered grid ·  Yellow = config issue ·  Blue = running fine", font(25), fill=MUTED)
    save(img, "starrupture-automation-loop.webp")

hero()
first_hour()
corporations()
automation_loop()
print("all images generated")
