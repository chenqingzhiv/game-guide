#!/usr/bin/env python3
"""Generate Project Zomboid beginner's guide WebP infographics (1280x720) for game-guide.club.

Style: apocalypse palette — dark charcoal-to-olive gradient, blood-red accents,
sickly zombie-green highlights, bone-white text, hazard-orange chips. Flat rounded
panels, bold Arial titles, auto-fitted text. Mirrors the existing 1280x720
infographic look used across the site.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "project-zomboid")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
SS = 2  # supersample factor
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
    for s in range(base_size, 10, -2):
        f = font(s, bold)
        if tlen(text, f) <= max_w:
            return f
    return font(10, bold)

# ── Project Zomboid apocalypse palette ──
BG_TOP = (22, 24, 20)          # dark charcoal-olive
BG_BOTTOM = (52, 38, 24)       # decayed earth
BLOOD = (196, 52, 48)          # blood red
ZOMBIE = (126, 156, 92)        # sickly green
BONE = (228, 222, 210)         # bone white
ORANGE = (232, 152, 64)        # hazard orange
RED = (214, 80, 72)
GREEN = (120, 170, 96)
BLUE = (110, 160, 210)
PURPLE = (168, 140, 235)
PANEL_BG = (32, 32, 28)
PANEL_BG2 = (46, 42, 34)
TEXT = (236, 238, 246)
MUTED = (162, 162, 158)
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

# ── decorative hazard marks ──
def hazard_marks(d):
    marks = [
        (70, 90, 40, 40, ZOMBIE), (170, 60, 34, 34, BLOOD), (260, 110, 30, 30, ORANGE),
        (980, 70, 40, 40, BLOOD), (1060, 110, 34, 34, ZOMBIE), (1150, 55, 30, 30, BLUE),
        (60, 580, 34, 34, BLUE), (150, 620, 30, 30, ORANGE), (230, 570, 28, 28, ZOMBIE),
        (1030, 600, 34, 34, PURPLE), (1120, 560, 36, 36, BLOOD), (1200, 615, 28, 28, ZOMBIE),
    ]
    for (x, y, w, h, c) in marks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)

def chips(d, chips, y, chip_w=250, gap=14, height=50, fill=PANEL_BG, outline=ORANGE):
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, y * SS, (x + chip_w) * SS, (y + height) * SS), 16, fill=fill, outline=outline, width=2)
        f = fit_font(chip, chip_w - 20, 26, bold=True)
        ctext(d, (x + chip_w / 2, y + height / 2), chip, f, fill=TEXT)

# ---------------------------------------------------------------- hero
def hero():
    img, d = canvas()
    hazard_marks(d)
    ctext(d, (W / 2, 180), "PROJECT ZOMBOID", font(120, True), fill=WHITE)
    ctext(d, (W / 2, 300), "The Ultimate Beginner's Guide 2026", font(54, True), fill=ORANGE)
    ctext(d, (W / 2, 370), "Survive the Knox Infection  ·  Build 42.20  ·  Outlast the End",
          font(32), fill=MUTED)
    chips(d, ["Build 42.20", "121K Players", "Bites = Death", "Co-op", "No Cure"], 440, chip_w=235)
    ctext(d, (W / 2, 615),
          "A quarantined county. A virus with no cure. Your only goal is to keep living.",
          fit_font("A quarantined county. A virus with no cure. Your only goal is to keep living.", W - 80, 27, bold=True),
          fill=MUTED)
    save(img, "zomboid-beginners-hero.webp")

# ---------------------------------------------------------------- first week
def first_week():
    img, d = canvas()
    ctext(d, (W / 2, 80), "Your First Week: The Survival Plan", font(56, True), fill=WHITE)
    ctext(d, (W / 2, 140), "Before the power cuts and the taps run dry", font(29), fill=MUTED)

    steps = [
        ("1", "Loot Quietly", "Bag, weapon, food, water bottles", BLOOD),
        ("2", "Sheet the Windows", "Stop zombies spotting you inside", ZOMBIE),
        ("3", "Watch Life & Living", "6am Cooking · 12pm Carpentry · 6pm Survival", ORANGE),
        ("4", "Fill Every Container", "Water shuts off within the first month", BLUE),
        ("5", "Sleep Upstairs", "Locked door, second floor, safe room", GREEN),
        ("6", "Burpees Daily", "Fitness is the stat that saves your life", PURPLE),
    ]
    bw, bh = 384, 180
    positions = [
        (40, 200), (448, 200), (856, 200),
        (40, 410), (448, 410), (856, 410),
    ]
    for i, step in enumerate(steps):
        x, y = positions[i]
        num, title, sub, c = step
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 52) * SS), 18, fill=c)
        f = fit_font("STEP " + num, bw - 24, 28, bold=True)
        ctext(d, (x + bw / 2, y + 26), "STEP " + num, f, fill=WHITE)
        ctext(d, (x + bw / 2, y + 92), title, fit_font(title, bw - 24, 34, bold=True), fill=TEXT)
        ctext(d, (x + bw / 2, y + 140), sub, fit_font(sub, bw - 24, 24), fill=MUTED)
    ctext(d, (W / 2, 652), "Survive day one and you've beaten the hardest day in the game",
          fit_font("Survive day one and you've beaten the hardest day in the game", W - 80, 27, bold=True), fill=MUTED)
    save(img, "zomboid-first-week.webp")

# ---------------------------------------------------------------- infection
def infection():
    img, d = canvas()
    ctext(d, (W / 2, 70), "The Knox Infection: Know Your Odds", font(58, True), fill=WHITE)
    ctext(d, (W / 2, 132), "There is no cure. Every zombie contact is a roll of the dice.", font(29), fill=MUTED)

    rows = [
        ("BITE", "100% Infected", "Guaranteed death sentence", BLOOD),
        ("LACERATION", "25% Infected", "Serious wound — treat and pray", ORANGE),
        ("SCRATCH", "7% Infected", "Minor wound — still a roll", ZOMBIE),
    ]
    bw, bh, gx = 384, 190, 26
    x0 = (W - (len(rows) * bw + (len(rows) - 1) * gx)) / 2
    y = 210
    for i, r in enumerate(rows):
        x = x0 + i * (bw + gx)
        label, pct, note, c = r
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG, outline=c, width=3)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 56) * SS), 18, fill=c)
        ctext(d, (x + bw / 2, y + 28), label, fit_font(label, bw - 24, 30, bold=True), fill=WHITE)
        ctext(d, (x + bw / 2, y + 108), pct, fit_font(pct, bw - 24, 40, bold=True), fill=TEXT)
        ctext(d, (x + bw / 2, y + 158), note, fit_font(note, bw - 32, 22), fill=MUTED)

    ctext(d, (W / 2, 462), "The 48–72 hour countdown", font(30, True), fill=ORANGE)
    timeline = ["Feels fine", "Queasy (6-12h)", "Nauseous", "Sick + Fever", "Death & Reanimate"]
    chips(d, timeline, 512, chip_w=225, height=46, fill=PANEL_BG2, outline=RED)
    ctext(d, (W / 2, 655),
          "The 'Infected' wound label is just a normal infection — the sickness moodles are the real alarm",
          fit_font("The 'Infected' wound label is just a normal infection — the sickness moodles are the real alarm", W - 80, 24, bold=True),
          fill=MUTED)
    save(img, "zomboid-infection-chart.webp")

# ---------------------------------------------------------------- build 42
def build42():
    img, d = canvas()
    ctext(d, (W / 2, 70), "Build 42.20: The Biggest Update Yet", font(56, True), fill=WHITE)
    ctext(d, (W / 2, 132), "Stable July 29, 2026 · record 121,603 players · the map doubled, the animals arrived",
          fit_font("Stable July 29, 2026 · record 121,603 players · the map doubled, the animals arrived", W - 80, 28, bold=True),
          fill=ORANGE)

    left = [
        ("🐄 Animals", "Cows, sheep, chickens, pigs, turkeys"),
        ("🧬 Animal Husbandry", "Breed, milk, shear, hatch, butcher"),
        ("🗺️ Map Doubled", "4 new towns, 1,400+ buildings"),
        ("🏙️ Vertical World", "Basements, bunkers, 32-floor towers"),
    ]
    right = [
        ("🔨 Crafting Overhaul", "12 disciplines from knapping to forging"),
        ("⚒️ Blacksmithing", "Primitive forges to medieval weapon smithing"),
        ("🎯 New Challenge Modes", "'28 Minutes Later' + 'Top of the World'"),
        ("💾 Fresh Start", "B41 saves & mods don't carry over"),
    ]
    bw, bh, gx, gy = 585, 116, 20, 16
    y0 = 196
    for i, (title, sub) in enumerate(left):
        y = y0 + i * (bh + gy)
        rrect(d, (24 * SS, y * SS, (24 + bw) * SS, (y + bh) * SS), 14, fill=PANEL_BG, outline=ZOMBIE, width=2)
        ctext(d, (24 + bw / 2, y + 42), title, fit_font(title, bw - 28, 30, bold=True), fill=TEXT)
        ctext(d, (24 + bw / 2, y + 88), sub, fit_font(sub, bw - 28, 23), fill=MUTED)
    for i, (title, sub) in enumerate(right):
        y = y0 + i * (bh + gy)
        rrect(d, ((24 + bw + gx) * SS, y * SS, (24 + 2 * bw + gx) * SS, (y + bh) * SS), 14, fill=PANEL_BG, outline=BLOOD, width=2)
        ctext(d, (24 + bw + gx + bw / 2, y + 42), title, fit_font(title, bw - 28, 30, bold=True), fill=TEXT)
        ctext(d, (24 + bw + gx + bw / 2, y + 88), sub, fit_font(sub, bw - 28, 23), fill=MUTED)

    save(img, "zomboid-build42-crafting-animals.webp")

if __name__ == "__main__":
    hero()
    first_week()
    infection()
    build42()
