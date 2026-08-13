#!/usr/bin/env python3
"""Generate Valheim beginner's guide WebP infographics (1280x720) for game-guide.club.

Style: Norse storm palette — deep green-to-bronze gradient, gold/bronze accents,
torch-orange highlights, ice-blue Deep North accents. Flat rounded panels, bold
Arial titles, auto-fitted text. Mirrors the existing 1280x720 infographic look.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "valheim")
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

# ── Valheim Norse palette ──
BG_TOP = (16, 24, 20)          # deep storm green
BG_BOTTOM = (42, 32, 22)       # bronze-brown
GOLD = (222, 180, 106)
ORANGE = (230, 130, 60)        # torch
ICE = (140, 205, 230)          # deep north ice
GREEN = (105, 180, 112)
RED = (215, 90, 80)
PURPLE = (168, 140, 235)
BLUE = (110, 160, 235)
PANEL_BG = (34, 34, 30)
PANEL_BG2 = (46, 42, 34)
TEXT = (236, 238, 246)
MUTED = (162, 168, 168)
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

# ── decorative Viking rune chips / banners ──
def nordic_marks(d):
    """Scatter small 'rune' blocks across the canvas for texture."""
    marks = [
        (70, 90, 40, 40, GREEN), (170, 60, 34, 34, ICE), (260, 110, 30, 30, GOLD),
        (980, 70, 40, 40, RED), (1060, 110, 34, 34, ORANGE), (1150, 55, 30, 30, BLUE),
        (60, 580, 34, 34, BLUE), (150, 620, 30, 30, GOLD), (230, 570, 28, 28, ICE),
        (1030, 600, 34, 34, PURPLE), (1120, 560, 36, 36, GREEN), (1200, 615, 28, 28, ORANGE),
    ]
    for (x, y, w, h, c) in marks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)

def chips(d, chips, y, chip_w=250, gap=14, height=50, fill=PANEL_BG, outline=GOLD):
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
    nordic_marks(d)
    ctext(d, (W / 2, 210), "VALHEIM", font(150, True), fill=WHITE)
    ctext(d, (W / 2, 330), "The Ultimate Beginner's Guide 2026", font(54, True), fill=GOLD)
    ctext(d, (W / 2, 400), "Survive Your First Day  ·  Kill the Forsaken  ·  Eight Biomes",
          font(33), fill=MUTED)
    chips(d, ["8 Biomes", "8 Bosses", "1-10 Co-op", "Deep North", "Sept 9: 1.0"], 460, chip_w=230)
    ctext(d, (W / 2, 615),
          "From the Meadows to the Deep North — a Viking purgatory worth every death",
          fit_font("From the Meadows to the Deep North — a Viking purgatory worth every death", W - 80, 27, bold=True),
          fill=MUTED)
    save(img, "valheim-beginners-hero.webp")

# ---------------------------------------------------------------- first day
def first_day():
    img, d = canvas()
    ctext(d, (W / 2, 80), "Your First Day: The 15-Step Launch Plan", font(56, True), fill=WHITE)
    ctext(d, (W / 2, 140), "Before nightfall: a fire, a bed, and a workbench", font(29), fill=MUTED)

    steps = [
        ("1", "Punch Trees + Stone", "First tools: axe, hammer", GREEN),
        ("2", "Build a Workbench", "Shelter it from rain", GOLD),
        ("3", "Campfire + Bed", "Rested bonus, respawn point", ORANGE),
        ("4", "Eat 3 Foods", "Berries, mushroom, meat", RED),
        ("5", "Hunt Boar & Deer", "Leather gear, bow", ICE),
        ("6", "Sleep Before Night", "Skip the Graydwarf waves", PURPLE),
    ]
    bw, bh, gx, gy = 384, 180, 26, 30
    positions = [
        (40, 200), (448, 200), (856, 200),
        (40, 410), (448, 410), (856, 410),
    ]
    for i, step in enumerate(steps):
        x, y = positions[i]
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG)
        num, title, sub, c = step
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 52) * SS), 18, fill=c)
        f = fit_font("STEP " + num, bw - 24, 28, bold=True)
        ctext(d, (x + bw / 2, y + 26), "STEP " + num, f, fill=WHITE)
        ctext(d, (x + bw / 2, y + 92), title, fit_font(title, bw - 24, 34, bold=True), fill=TEXT)
        ctext(d, (x + bw / 2, y + 138), sub, fit_font(sub, bw - 24, 25), fill=MUTED)
    ctext(d, (W / 2, 652), "21 real minutes decide your first week — use them well",
          fit_font("21 real minutes decide your first week — use them well", W - 80, 27, bold=True), fill=MUTED)
    save(img, "valheim-first-day.webp")

# ---------------------------------------------------------------- biome progression
def biome_progression():
    img, d = canvas()
    ctext(d, (W / 2, 70), "The Eight Biomes — In Order", font(58, True), fill=WHITE)
    ctext(d, (W / 2, 130), "Each biome is gated by the boss before it. Respect the order.", font(29), fill=MUTED)

    biomes = [
        ("1", "Meadows", "Eikthyr", GREEN),
        ("2", "Black Forest", "The Elder", BLUE),
        ("3", "Swamp", "Bonemass", (120, 150, 90)),
        ("4", "Mountains", "Moder", (190, 200, 215)),
        ("5", "Plains", "Yagluth", GOLD),
        ("6", "Mistlands", "The Queen", PURPLE),
        ("7", "Ashlands", "Fader", ORANGE),
        ("8", "Deep North", "Frost King", ICE),
    ]
    bw, bh, gx, gy = 285, 120, 18, 24
    x0, y0 = 24, 200
    for i, b in enumerate(biomes):
        col = i % 4
        row = i // 4
        x = x0 + col * (bw + gx)
        y = y0 + row * (bh + gy)
        num, name, boss, c = b
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 14, fill=PANEL_BG)
        rrect(d, (x * SS, y * SS, (x + 64) * SS, (y + bh) * SS), 14, fill=c)
        ctext(d, (x + 32, y + bh / 2), num, font(36, True), fill=WHITE)
        ctext(d, (x + 88, y + 40), name, fit_font(name, bw - 110, 30, bold=True), fill=TEXT)
        ctext(d, (x + 88, y + 84), "Boss: " + boss, fit_font("Boss: " + boss, bw - 110, 23), fill=MUTED)

    ctext(d, (W / 2, 560), "Gear-gate rule:", font(30, True), fill=GOLD)
    ctext(d, (W / 2, 608),
          "If the biome name shows red, you're under-geared — farm the previous tier and come back",
          fit_font("If the biome name shows red, you're under-geared — farm the previous tier and come back", W - 80, 28, bold=True),
          fill=MUTED)
    save(img, "valheim-biome-progression.webp")

# ---------------------------------------------------------------- combat basics
def combat_basics():
    img, d = canvas()
    ctext(d, (W / 2, 80), "Combat Basics: Block, Parry, Dodge", font(58, True), fill=WHITE)
    ctext(d, (W / 2, 140), "Three defensive tools decide whether you survive a Graydwarf fight", font(29), fill=MUTED)

    tools = [
        ("BLOCK", "Hold right-click with a shield", "Reduces damage by the shield's block value", (110, 160, 235)),
        ("PARRY", "Tap block as the attack lands", "Staggers the enemy · double damage on the counter", (222, 180, 106)),
        ("DODGE", "Block + jump while moving", "Invulnerability frames — untouchable mid-roll", (105, 180, 112)),
    ]
    bw, bh, gx = 384, 220, 26
    x0 = (W - (len(tools) * bw + (len(tools) - 1) * gx)) / 2
    y = 210
    for i, t in enumerate(tools):
        x = x0 + i * (bw + gx)
        label, desc, note, c = t
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + bh) * SS), 18, fill=PANEL_BG, outline=c, width=3)
        rrect(d, (x * SS, y * SS, (x + bw) * SS, (y + 58) * SS), 18, fill=c)
        ctext(d, (x + bw / 2, y + 29), label, fit_font(label, bw - 24, 30, bold=True), fill=WHITE)
        ctext(d, (x + bw / 2, y + 100), desc, fit_font(desc, bw - 32, 26, bold=True), fill=TEXT)
        ctext(d, (x + bw / 2, y + 172), note, fit_font(note, bw - 32, 23), fill=MUTED)

    ctext(d, (W / 2, 492), "Early enemies to respect", font(30, True), fill=GOLD)
    enemies = ["Boars (parry them)", "Graydwarves (night)", "Skeletons", "Trolls (run!)"]
    chips(d, enemies, 532, chip_w=270, height=46, fill=PANEL_BG2, outline=ORANGE)
    ctext(d, (W / 2, 655),
          "The parry is the skill worth practicing — stagger + double damage wins every early fight",
          fit_font("The parry is the skill worth practicing — stagger + double damage wins every early fight", W - 80, 25, bold=True),
          fill=MUTED)
    save(img, "valheim-combat-basics.webp")

if __name__ == "__main__":
    hero()
    first_day()
    biome_progression()
    combat_basics()
