#!/usr/bin/env python3
"""Generate Fields of Mistria guide WebP infographics (1280x720) for game-guide.club.

Style: pastel 90s-anime cream/lavender background with mauve-pink / misty-purple /
mint / gold accents, flat rounded panels, bold Arial titles. Mirrors the existing
1280x720 infographic look (gen_spiritstead_images.py). Text auto-fits its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "fields-of-mistria")
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

# Palette — Fields of Mistria pastel: cream / lavender / mauve-pink / mint / gold
BG_TOP = (253, 246, 242)
BG_BOTTOM = (222, 214, 236)   # soft lavender
MAUVE = (211, 128, 151)       # 90s-anime pink
PURPLE = (138, 110, 176)      # Essence purple
MINT = (116, 170, 152)
GOLD = (222, 168, 84)
BONE = (64, 54, 62)
MUTED = (132, 120, 130)
PANEL_BG = (255, 252, 247)
PANEL_BG2 = (243, 234, 220)
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
    # decorative pastel blocks (orbs / crops / star sparkles)
    blocks = [(80, 90, 46, 46, MAUVE), (165, 58, 40, 40, GOLD), (255, 98, 34, 34, PURPLE),
              (975, 68, 46, 46, MINT), (1060, 100, 40, 40, PURPLE), (1150, 55, 34, 34, GOLD),
              (60, 560, 40, 40, MINT), (150, 600, 34, 34, MAUVE), (230, 566, 30, 30, PURPLE),
              (1040, 590, 38, 38, MINT), (1120, 556, 42, 42, MAUVE), (1200, 612, 30, 30, GOLD)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    ctext(d, (W / 2, 185), "FIELDS OF MISTRIA", font(104, True), fill=BONE)
    ctext(d, (W / 2, 292), "The Complete Beginner's Guide 2026", font(52, True), fill=MAUVE)
    ctext(d, (W / 2, 360), "A pastel farm, a 90-floor dungeon, and a dragon teaching you magic", font(32), fill=MUTED)
    chips = ["Full 1.0 Release", "Cozy Farm Life-Sim", "90s Retro Anime", "NPC Studio", "$13.99"]
    chip_w, gap = 240, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 430 * SS, (x + chip_w) * SS, 480 * SS), 16, fill=PANEL_BG, outline=PURPLE, width=2)
        f = fit_font(chip, chip_w - 24, 27, bold=True)
        ctext(d, (x + chip_w / 2, 455), chip, f, fill=BONE)
    ctext(d, (W / 2, 595), "Stardew's calm, with a dungeon that actually fights back",
          fit_font("Stardew's calm, with a dungeon that actually fights back", W - 80, 28, bold=True),
          fill=PURPLE)
    save(img, "fields-of-mistria-hero.webp")

# ---------------------------------------------------------------- first week
def first_week():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Your First Spring: The Priority Order", font(56, True), fill=BONE)
    ctext(d, (W / 2, 136), "28-day seasons, a draining stamina bar, and no time to waste", font(29), fill=MUTED)

    steps = [
        ("1", "Water Crops First", "Unwatered crops skip a day — every morning", MAUVE),
        ("2", "Fish & Forage", "Beach + Eastern Road: 30–45 T per fish", MINT),
        ("3", "Hit the Request Board", "Money, materials, and Renown — free progress", PURPLE),
        ("4", "Turnips → Regrowers", "Turnips first, then Strawberries & Peas", GOLD),
        ("5", "Free Soup + Fountains", "Inn soup (20), bathhouse, roadside fountains", MINT),
        ("6", "Don't Overplant", "What you can't water is sunk cost", MAUVE),
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
        f = fit_font(title, bw - 130, 31, bold=True)
        ctext(d, (tx, y + 62), title, f, anchor="lm")
        fs = fit_font(sub, bw - 130, 21, bold=False)
        ctext(d, (tx, y + 118), sub, fs, anchor="lm", fill=MUTED)
    rrect(d, (x0 * SS, 636 * SS, (W - x0) * SS, 684 * SS), 16, fill=PANEL_BG2, outline=MAUVE, width=2)
    ctext(d, (W / 2, 660), "Stamina is the real game in Spring — every free refill counts",
          fit_font("Stamina is the real game in Spring — every free refill counts", W - 2 * x0 - 40, 29, bold=True),
          fill=MAUVE)
    save(img, "fields-of-mistria-first-week.webp")

# ---------------------------------------------------------------- mines
def mines():
    img, d = canvas()
    ctext(d, (W / 2, 70), "The Mines: 90 Floors of Ore", font(62, True), fill=BONE)
    ctext(d, (W / 2, 128), "Elevator checkpoint every 5 floors · seal floors 20 / 40 / 60 teach you magic", font(27), fill=MUTED)

    zones = [
        ("UPPER MINES", "Floors 1–19", "Copper Ore · Ruby", MAUVE),
        ("TIDE CAVERNS", "Floors 21–39", "Iron Ore · Sapphire · Coral", MINT),
        ("DEEP EARTH", "Floors 41–59", "Silver Ore · Emerald", GOLD),
        ("LAVA CAVES", "Floors 61–79", "Gold Ore", PURPLE),
        ("ANCIENT RUINS", "Floors 81–99", "Mistril Ore", MAUVE),
        ("THE SEALS", "Floors 20 · 40 · 60", "Rain · Growth · Dragon's Breath", PURPLE),
    ]
    bw, bh, gx, gy = 384, 175, 26, 24
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 175
    for i, (label, floors, ores, c) in enumerate(zones):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 46) * SS), 18, fill=c)
        rrect(d, (x * SS, (y + 46 - 18) * SS, (x + bw) * SS, (y + 46) * SS), 0, fill=PANEL_BG)
        ctext(d, (x + bw / 2, y + 23), label, font(23, True), fill=WHITE)
        f = fit_font(floors, bw - 24, 28, bold=True)
        ctext(d, (x + bw / 2, y + 82), floors, f, fill=BONE)
        fs = fit_font(ores, bw - 24, 22, bold=False)
        ctext(d, (x + bw / 2, y + 128), ores, fs, fill=MUTED)
    rrect(d, (x0 * SS, 592 * SS, (W - x0) * SS, 638 * SS), 16, fill=PANEL_BG2, outline=MINT, width=2)
    ctext(d, (W / 2, 615), "Silver Pickaxe: charged strike breaks a 3×6 area — the mid-game gear check",
          fit_font("Silver Pickaxe: charged strike breaks a 3×6 area — the mid-game gear check", W - 2 * x0 - 40, 27, bold=True),
          fill=MINT)
    rrect(d, (x0 * SS, 650 * SS, (W - x0) * SS, 692 * SS), 16, fill=PANEL_BG2, outline=PURPLE, width=2)
    ctext(d, (W / 2, 671), "Smelt 10 ore → 1 ingot, or 9 with the Blacksmithing perk",
          fit_font("Smelt 10 ore → 1 ingot, or 9 with the Blacksmithing perk", W - 2 * x0 - 40, 26, bold=True),
          fill=PURPLE)
    save(img, "fields-of-mistria-mines.webp")

# ---------------------------------------------------------------- romance
def romance():
    img, d = canvas()
    ctext(d, (W / 2, 68), "12 Marriage Candidates", font(66, True), fill=BONE)
    ctext(d, (W / 2, 128), "Any gender, any heart — 10 hearts unlocks the proposal event", font(29), fill=MUTED)

    names = ["Adeline", "Balor", "Caldarus", "Celine", "Eiland", "Hayden",
             "Juniper", "March", "Reina", "Ryis", "Seridia", "Valen"]
    bw, bh, gx, gy = 260, 76, 26, 22
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 185
    for i, name in enumerate(names):
        col, row = i % 3, i // 3
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 16, fill=PANEL_BG, outline=MAUVE, width=2)
        f = fit_font(name, bw - 40, 33, bold=True)
        ctext(d, (x + bw / 2, y + bh / 2), name, f, fill=BONE)
    # footer: romance path
    rrect(d, (x0 * SS, 518 * SS, (W - x0) * SS, 560 * SS), 16, fill=PANEL_BG2, outline=MAUVE, width=2)
    ctext(d, (W / 2, 539), "Gift & chat daily → pick the romantic route → hit 10 hearts → craft the ring",
          fit_font("Gift & chat daily → pick the romantic route → hit 10 hearts → craft the ring", W - 2 * x0 - 40, 26, bold=True),
          fill=MAUVE)
    rrect(d, (x0 * SS, 574 * SS, (W - x0) * SS, 616 * SS), 16, fill=PANEL_BG2, outline=PURPLE, width=2)
    ctext(d, (W / 2, 595), "Caldarus & Seridia were hidden during Early Access — fully romanceable in 1.0",
          fit_font("Caldarus & Seridia were hidden during Early Access — fully romanceable in 1.0", W - 2 * x0 - 40, 26, bold=True),
          fill=PURPLE)
    rrect(d, (x0 * SS, 630 * SS, (W - x0) * SS, 674 * SS), 16, fill=PANEL_BG2, outline=MINT, width=2)
    ctext(d, (W / 2, 652), "Custom wedding · then a Mystical Feather unlocks the family path",
          fit_font("Custom wedding · then a Mystical Feather unlocks the family path", W - 2 * x0 - 40, 26, bold=True),
          fill=MINT)
    save(img, "fields-of-mistria-romance.webp")

hero()
first_week()
mines()
romance()
print("all images generated")
