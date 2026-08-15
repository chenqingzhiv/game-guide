#!/usr/bin/env python3
"""Generate Survival Log guide WebP infographics (1280x720) for game-guide.club.

Style: dark apocalypse slate with hazard-orange / blood-red / survival-green
accents, flat rounded panels, bold Arial titles. Mirrors the existing
1280x720 infographic look. Text is auto-fitted so nothing overflows its panel.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "images", "survival-log")
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

# Palette — apocalypse slate + hazard orange / blood red / survival green
BG_TOP = (48, 54, 62)
BG_BOTTOM = (24, 28, 33)
HAZARD = (232, 131, 62)
BLOOD = (201, 66, 55)
AMBER = (232, 178, 62)
GREEN = (106, 168, 118)
SKY = (106, 152, 182)
BONE = (238, 232, 220)
MUTED = (166, 160, 150)
PANEL_BG = (56, 64, 74)
PANEL_BG2 = (68, 78, 90)
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
    # hazard-stripe accent bar
    for i, x in enumerate(range(0, SW, 40 * SS)):
        if (i // 2) % 2 == 0:
            d.rectangle([x, 0, x + 40 * SS, 10 * SS], fill=HAZARD)
        else:
            d.rectangle([x, 0, x + 40 * SS, 10 * SS], fill=BONE)
    # silhouette skyline blocks
    blocks = [(70, 120, 52, 52, HAZARD), (160, 80, 42, 42, BLOOD), (250, 140, 36, 36, AMBER),
              (970, 90, 50, 50, BLOOD), (1060, 120, 42, 42, HAZARD), (1150, 80, 36, 36, GREEN),
              (70, 570, 42, 42, GREEN), (160, 610, 36, 36, AMBER), (240, 580, 32, 32, BLOOD),
              (1030, 600, 40, 40, AMBER), (1120, 570, 44, 44, HAZARD), (1200, 615, 32, 32, GREEN)]
    for (x, y, w, h, c) in blocks:
        rrect(d, (x * SS, y * SS, (x + w) * SS, (y + h) * SS), 8, fill=c)
    ctext(d, (W / 2, 180), "SURVIVAL LOG", font(118, True), fill=BONE)
    ctext(d, (W / 2, 292), "The Zombie Hoarding Survival Guide 2026", font(48, True), fill=HAZARD)
    ctext(d, (W / 2, 358), "10 hours to prepare. Then the city floods with the dead.", font(33), fill=MUTED)
    chips = ["Zombie Hoarding Sim", "Midnight Workshop", "Lilith Games", "Mostly Positive", "$9.34"]
    chip_w, gap = 258, 14
    total = len(chips) * chip_w + (len(chips) - 1) * gap
    x0 = (W - total) / 2
    for i, chip in enumerate(chips):
        x = x0 + i * (chip_w + gap)
        rrect(d, (x * SS, 428 * SS, (x + chip_w) * SS, 478 * SS), 16, fill=PANEL_BG, outline=HAZARD, width=2)
        f = fit_font(chip, chip_w - 24, 27, bold=True)
        ctext(d, (x + chip_w / 2, 453), chip, f, fill=BONE)
    ctext(d, (W / 2, 600), "Project Zomboid's tension, with a shopping list you'll actually plan",
          fit_font("Project Zomboid's tension, with a shopping list you'll actually plan", W - 80, 27, bold=True),
          fill=GREEN)
    save(img, "survival-log-hero.webp")

# ---------------------------------------------------------------- countdown
def countdown():
    img, d = canvas()
    ctext(d, (W / 2, 76), "The 10-Hour Countdown", font(58, True), fill=BONE)
    ctext(d, (W / 2, 136), "Pre-outbreak prep — buy smart, then fortify, in this order", font(29), fill=MUTED)

    stages = [
        ("HOURS 0–2", "Supermarket Run", "Staple food + bottled water", "Compressed biscuits, canned meat, rice, instant noodles", HAZARD),
        ("HOURS 2–4", "Hardware Store", "Reinforce + melee", "Wood planks, steel plates, screws, hammer, crowbar, fire axe", AMBER),
        ("HOURS 4–6", "Fortify Home", "Board windows, brace doors", "Nail windows shut, reinforce the door, set up obstacles", GREEN),
        ("HOURS 6–10", "Final Sweep", "Radio, fuel, meds, organize", "Radio, gasoline, first-aid kit, iodine, gauze, stash tidy", SKY),
    ]
    panel_w, panel_h = 286, 320
    gap = 22
    x0 = (W - (panel_w * 4 + gap * 3)) / 2
    y0 = 196
    for i, (label, title, sub, desc, c) in enumerate(stages):
        x = x0 + i * (panel_w + gap)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + panel_h) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + 58) * SS), 18, fill=c)
        ctext(d, (x + panel_w / 2, y0 + 29), label, font(23, True), fill=BONE)
        f = fit_font(title, panel_w - 24, 32, bold=True)
        ctext(d, (x + panel_w / 2, y0 + 132), title, f, fill=BONE)
        fs = fit_font(sub, panel_w - 24, 24, bold=True)
        ctext(d, (x + panel_w / 2, y0 + 180), sub, fs, fill=HAZARD)
        f2 = fit_font(desc, panel_w - 28, 20, bold=False)
        ctext(d, (x + panel_w / 2, y0 + 250), desc, f2, fill=MUTED)
        if i < 3:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(40, True), fill=HAZARD)
    rrect(d, (x0 * SS, 548 * SS, (W - x0) * SS, 598 * SS), 16, fill=PANEL_BG2, outline=HAZARD, width=2)
    ctext(d, (W / 2, 573), "Don't buy guns — gunfire pulls the whole horde. Silent melee is the beginner's friend.",
          fit_font("Don't buy guns — gunfire pulls the whole horde. Silent melee is the beginner's friend.", W - 2 * x0 - 40, 26, bold=True),
          fill=HAZARD)
    rrect(d, (x0 * SS, 614 * SS, (W - x0) * SS, 664 * SS), 16, fill=PANEL_BG2, outline=GREEN, width=2)
    ctext(d, (W / 2, 639), "Canned, long-shelf-life food beats fresh produce — it won't rot while the power is off",
          fit_font("Canned, long-shelf-life food beats fresh produce — it won't rot while the power is off", W - 2 * x0 - 40, 26, bold=True),
          fill=GREEN)
    save(img, "survival-log-countdown.webp")

# ---------------------------------------------------------------- safehouse
def safehouse():
    img, d = canvas()
    ctext(d, (W / 2, 76), "Safehouse Survival Checklist", font(58, True), fill=BONE)
    ctext(d, (W / 2, 136), "What keeps you alive after the city falls", font(29), fill=MUTED)

    steps = [
        ("1", "Reinforce Every Entrance", "Board the windows, brace the door", HAZARD),
        ("2", "Balcony Farm", "Potted crops = renewable food", GREEN),
        ("3", "Power & Heat", "Generator + stored fuel for winter", AMBER),
        ("4", "Radio & Intel", "Early horde warnings, rescue routes", SKY),
        ("5", "Medical Kit", "Bandages, iodine, gauze for scratches", BLOOD),
        ("6", "Mind the Mind", "Journal + radio keep anxiety events away", AMBER),
    ]
    bw, bh, gx, gy = 384, 180, 26, 30
    x0 = (W - (bw * 3 + gx * 2)) / 2
    y0 = 196
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
        fs = fit_font(sub, bw - 130, 22, bold=False)
        ctext(d, (tx, y + 118), sub, fs, anchor="lm", fill=MUTED)
    rrect(d, (x0 * SS, 622 * SS, (W - x0) * SS, 674 * SS), 16, fill=PANEL_BG2, outline=HAZARD, width=2)
    ctext(d, (W / 2, 648), "Food is currency — trade it with neighbors and by drone to get anything else",
          fit_font("Food is currency — trade it with neighbors and by drone to get anything else", W - 2 * x0 - 40, 27, bold=True),
          fill=HAZARD)
    save(img, "survival-log-safehouse.webp")

# ---------------------------------------------------------------- loop
def loop():
    img, d = canvas()
    ctext(d, (W / 2, 76), "The Rebirth Loop", font(66, True), fill=BONE)
    ctext(d, (W / 2, 136), "Every failure becomes experience — the game literally writes it in your Survival Log", font(27), fill=MUTED)

    stages = [
        ("PREPARE", "Hoard & fortify", "Supermarket, hardware, home", HAZARD),
        ("OUTBREAK", "The city falls", "10-hour countdown ends", BLOOD),
        ("SURVIVE", "Hold the safehouse", "Farm, trade, scavenge", GREEN),
        ("DIE / LEARN", "Restart smarter", "Points → permanent skills", AMBER),
    ]
    panel_w, panel_h = 266, 230
    gap = 30
    x0 = (W - (panel_w * 4 + gap * 3)) / 2
    y0 = 200
    for i, (label, sub, desc, c) in enumerate(stages):
        x = x0 + i * (panel_w + gap)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + panel_h) * SS), 18, fill=PANEL_BG)
        rrect(d, (x * SS, y0 * SS, (x + panel_w) * SS, (y0 + 56) * SS), 18, fill=c)
        ctext(d, (x + panel_w / 2, y0 + 28), label, font(22, True), fill=WHITE)
        f = fit_font(sub, panel_w - 24, 26, bold=True)
        ctext(d, (x + panel_w / 2, y0 + 112), sub, f, fill=BONE)
        fs = fit_font(desc, panel_w - 24, 20, bold=False)
        ctext(d, (x + panel_w / 2, y0 + 168), desc, fs, fill=MUTED)
        if i < 3:
            ax = x + panel_w
            ctext(d, (ax + gap / 2, y0 + panel_h / 2), "→", font(42, True), fill=HAZARD)
    rrect(d, (x0 * SS, 470 * SS, (W - x0) * SS, 528 * SS), 16, fill=PANEL_BG2, outline=GREEN, width=2)
    ctext(d, (W / 2, 499), "Hidden stash spots & survival tricks from past runs are recorded — and remembered",
          fit_font("Hidden stash spots & survival tricks from past runs are recorded — and remembered", W - 2 * x0 - 40, 26, bold=True),
          fill=GREEN)
    rrect(d, (x0 * SS, 548 * SS, (W - x0) * SS, 606 * SS), 16, fill=PANEL_BG2, outline=AMBER, width=2)
    ctext(d, (W / 2, 577), "Survive 20+ days in Story Mode → unlock Endless Mode",
          fit_font("Survive 20+ days in Story Mode → unlock Endless Mode", W - 2 * x0 - 40, 26, bold=True),
          fill=AMBER)
    rrect(d, (x0 * SS, 626 * SS, (W - x0) * SS, 676 * SS), 16, fill=PANEL_BG2, outline=HAZARD, width=2)
    ctext(d, (W / 2, 651), "The log remembers. You don't start over — you start smarter.",
          fit_font("The log remembers. You don't start over — you start smarter.", W - 2 * x0 - 40, 26, bold=True),
          fill=HAZARD)
    save(img, "survival-log-loop.webp")

hero()
countdown()
safehouse()
loop()
print("all images generated")
