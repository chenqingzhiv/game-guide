#!/usr/bin/env python3
"""Generate Moonlight Peaks Money Making Guide WebP infographics (800x600).

Matches the existing MP infographic style: dark night-purple background,
warm cream text, green/gold accent panels.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "moonlight-peaks", "img")
os.makedirs(OUT, exist_ok=True)

W, H = 800, 600
SS = 2
SW, SH = W * SS, H * SS
FONT_DIR = r"C:\Windows\Fonts"

# Moonlight Peaks palette
BG = (32, 20, 49)
BG2 = (24, 14, 38)
PANEL = (46, 32, 66)
CARD = (42, 28, 60)
GREEN = (110, 190, 110)
GOLD = (240, 200, 120)
CREAM = (238, 230, 220)
MUTED = (180, 165, 190)
PURPLE = (168, 128, 218)
RED = (214, 108, 118)
BONE = (240, 234, 226)

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

def fit(text, max_w, base_size, bold=False):
    for s in range(base_size, 9, -1):
        f = font(s, bold)
        if tlen(text, f) <= max_w:
            return f
    return font(9, bold)

def canvas():
    img = Image.new("RGB", (SW, SH), BG)
    d = ImageDraw.Draw(img)
    for y in range(SH):
        t = y / SH
        c = tuple(int(BG[i] + (BG2[i] - BG[i]) * t) for i in range(3))
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

def header(d, title, subtitle=None):
    rrect(d, (20, 16, W - 20, 84), 16, fill=PANEL)
    ctext(d, (W / 2, 34), title, font(26, True), fill=GOLD)
    if subtitle:
        ctext(d, (W / 2, 62), subtitle, fit(subtitle, W - 80, 16), fill=CREAM)

def panel_lines(d, x0, y0, lines, fnt=None, fill=CREAM, gap=21, max_w=None):
    """Draw bullet lines starting at (x0, y0). Returns final y."""
    f = fnt or font(14)
    y = y0
    for ln in lines:
        bullet = "•  "
        rest = ln
        if ln.startswith("> "):
            bullet = "»  "
            rest = ln[2:]
        if max_w:
            wrapped = wrap_lines(rest, f, max_w)
        else:
            wrapped = [rest]
        for wi, wl in enumerate(wrapped):
            lead = bullet if wi == 0 else "   "
            ctext(d, (x0, y), lead + wl, f, fill=fill, anchor="lm")
            y += gap
    return y

def wrap_lines(text, fnt, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tlen(t, fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---------------------------------------------------------------- 1. Money loop hero
def money_loop():
    img, d = canvas()
    header(d, "THE MONEY LOOP", "Moonlight Peaks — from field to gold")

    # Flow row: FIELD -> MACHINES -> COINS
    boxes = [
        ("FIELD", GOLD, ["Grapes · Wheat", "Strawberries", "Magical crops"]),
        ("MACHINES", PURPLE, ["Keg · Jam Maker", "Mill · Cheese Press", "Cauldron"]),
        ("COINS", GREEN, ["Upgrades", "Animals · Trees", "More seeds"]),
    ]
    box_w = 220
    gap = 26
    x0 = 26
    y0, y1 = 100, 210
    for i, (name, col, lines) in enumerate(boxes):
        bx = x0 + i * (box_w + gap)
        rrect(d, (bx, y0, bx + box_w, y1), 14, fill=CARD)
        rrect(d, (bx, y0, bx + box_w, y0 + 38), 14, fill=col)
        ctext(d, (bx + box_w / 2, y0 + 19), name, fit(name, box_w - 12, 18, True), fill=BG)
        y = y0 + 54
        for ln in lines:
            f = fit(ln, box_w - 20, 14)
            ctext(d, (bx + 12, y), ln, f, fill=CREAM, anchor="lm")
            y += 26
    # arrows between boxes
    for i in range(2):
        ax = x0 + box_w + gap + i * (box_w + gap) - 12
        ay = (y0 + y1) // 2
        d.polygon([(ax * SS, (ay - 10) * SS), (ax * SS, (ay + 10) * SS), ((ax + 14) * SS, ay * SS)], fill=GOLD)

    # Side income grid 2x2
    side = [
        ("BARN & ANIMALS", "Eggs → dishes · milk → cheese"),
        ("FRUIT TREES", "No upkeep · fruit every 6–8 nights"),
        ("MINING", "Ore respawns · bars fund tools"),
        ("FESTIVALS", "Prizes worth 2k–15k+ gold"),
    ]
    grid_x = 26
    grid_y = 232
    cell_w = (W - 52 - 14) / 2
    cell_h = 58
    for i, (title, sub) in enumerate(side):
        cx = grid_x + (i % 2) * (cell_w + 14)
        cy = grid_y + (i // 2) * (cell_h + 12)
        rrect(d, (cx, cy, cx + cell_w, cy + cell_h), 12, fill=PANEL)
        ctext(d, (cx + 14, cy + 19), title, fit(title, cell_w - 20, 15, True), fill=GOLD, anchor="lm")
        ctext(d, (cx + 14, cy + 39), sub, fit(sub, cell_w - 20, 13), fill=MUTED, anchor="lm")

    # Footer golden-rule note
    rrect(d, (26, 474, W - 26, H - 18), 14, fill=CARD)
    ctext(d, (W / 2, 504), "PROCESS EVERYTHING — NEVER SELL RAW", font(18, True), fill=GREEN)
    ctext(d, (W / 2, 540), "Wine pays 8–17× the raw grape value · keep 1–2 of every item", fit("Wine pays 8–17× the raw grape value · keep 1–2 of every item", W - 70, 15), fill=CREAM)
    save(img, "money-flow-overview.webp")

# ---------------------------------------------------------------- 2. Early game cash
def early_game():
    img, d = canvas()
    header(d, "EARLY GAME CASH", "Your first ten nights")

    panels = [
        ("NIGHTS 1–3", GREEN, [
            "Plant Wild Potatoes (3n)",
            "Forage flowers & mushrooms",
            "Dig every sparkly swirl —",
            "   Diamonds sell for 2,000g",
            "Follow the starter quests",
        ]),
        ("NIGHTS 4–6", GOLD, [
            "Finish Orlock's Wine Scheme",
            "Unlock the Keg (20 Wood)",
            "Copper tool upgrades",
            "Pickaxe → Axe → Watering Can",
            "Start planting grapes",
        ]),
        ("NIGHTS 7–10", PURPLE, [
            "Build 3 Kegs, make wine",
            "Process before selling",
            "Save for the Barn (4,000g)",
            "Feed your Gobbler goal",
            "Check quest board nightly",
        ]),
    ]
    panel_w = (W - 52 - 2 * 14) / 3
    y0, y1 = 100, 452
    for i, (title, col, lines) in enumerate(panels):
        px = 26 + i * (panel_w + 14)
        rrect(d, (px, y0, px + panel_w, y1), 14, fill=CARD)
        rrect(d, (px, y0, px + panel_w, y0 + 40), 14, fill=col)
        ctext(d, (px + panel_w / 2, y0 + 20), title, fit(title, panel_w - 12, 17, True), fill=BG)
        panel_lines(d, px + 14, y0 + 58, lines, font(13), max_w=panel_w - 28)

    rrect(d, (26, 468, W - 26, H - 18), 14, fill=PANEL)
    target = "TARGET BY NIGHT 10:  5,000–10,000g  ·  3 Kegs  ·  Copper Pickaxe"
    ctext(d, (W / 2, 534), target, fit(target, W - 70, 20, True), fill=GOLD)
    save(img, "early-game-cash.webp")

# ---------------------------------------------------------------- 3. Keg & processing profit
def keg_profit():
    img, d = canvas()
    header(d, "KEG & PROCESSING PROFIT", "Wine · Beer · Jam · Cheese")

    rows = [
        ("WHITE WINE", "4 White Grapes", "~460g", "8–17× raw", GOLD),
        ("RED WINE", "4 Blood Grapes", "~360g", "8–17× raw", CREAM),
        ("BEER", "3 Wily Wheat", "~420g", "8–17× raw", CREAM),
        ("MANA WINE", "2 White + 2 Blood + 1 Mana Essence", "~3× Red Wine", "late-game king", PURPLE),
        ("JAM / JELLY", "Fruit + Sugar (Mill)", "far above raw", "needs Jam Maker", CREAM),
        ("CHEESE", "Pig Goat / Draculamb milk", "big jump", "Cheese Press", CREAM),
    ]
    y = 100
    row_h = 62
    for name, mats, value, note, accent in rows:
        rrect(d, (26, y, W - 26, y + row_h), 12, fill=CARD)
        rrect(d, (36, y + 10, 210, y + row_h - 10), 10, fill=PANEL)
        ctext(d, (42, y + row_h / 2), name, fit(name, 160, 15, True), fill=accent, anchor="lm")
        ctext(d, (222, y + row_h / 2), mats, fit(mats, 330, 13), fill=CREAM, anchor="lm")
        ctext(d, (592, y + row_h / 2), value, fit(value, 110, 14, True), fill=GOLD, anchor="rm")
        ctext(d, (W - 36, y + row_h / 2), note, fit(note, 120, 11), fill=MUTED, anchor="rm")
        y += row_h + 8

    rrect(d, (26, y + 4, W - 26, H - 16), 14, fill=PANEL)
    ctext(d, (W / 2, y + 28), "Cooking margins: Cheeken Pot Pie +175% · Draculamb Roast +190%", fit("Cooking margins: Cheeken Pot Pie +175% · Draculamb Roast +190%", W - 70, 15, True), fill=GREEN)
    ctext(d, (W / 2, y + 54), "Grilled Wild Potato sells for LESS than raw potatoes — skip it", fit("Grilled Wild Potato sells for LESS than raw potatoes — skip it", W - 70, 13), fill=CREAM)
    save(img, "keg-wine-economy.webp")

# ---------------------------------------------------------------- 4. Milestones & budgets
def milestones():
    img, d = canvas()
    header(d, "MONEY MILESTONES", "Know your upgrade costs")

    rows = [
        ("3 Kegs", "20 Wood each", "Night 7+", GOLD),
        ("Copper tool", "1,000g + 3 Copper Bars", "Night 4+", CREAM),
        ("Barn", "4,000g", "Week 1–2", GOLD),
        ("Cheeken", "1,200g", "After Barn", CREAM),
        ("Pig Goat / Draculamb", "3,500g / 4,500g", "Spring–Summer", CREAM),
        ("Iron tool", "4,000g + 3–4 Iron Bars", "Spring", CREAM),
        ("Kitchen Extension", "3,000g + 20 Wood + 10 Iron Bars", "Summer", CREAM),
        ("Jam Maker", "40 Wood + 20 Stone + 10 Iron Bars", "Summer", CREAM),
        ("Mill", "8,000g", "Summer–Autumn", GOLD),
        ("Fruit tree", "2,000–6,000g", "Any", CREAM),
        ("Gold tool", "16,000g + 3 Gold Bars", "Autumn", CREAM),
        ("Enchanted tool", "48,000g + gold tool + 5 Mana Essence", "Winter Y1", PURPLE),
    ]
    y = 96
    row_h = 34
    for name, cost, when, accent in rows:
        rrect(d, (26, y, W - 26, y + row_h), 10, fill=CARD)
        ctext(d, (40, y + row_h / 2), name, fit(name, 240, 14, True), fill=accent, anchor="lm")
        ctext(d, (330, y + row_h / 2), cost, fit(cost, 300, 13), fill=CREAM, anchor="lm")
        ctext(d, (W - 40, y + row_h / 2), when, fit(when, 100, 12), fill=MUTED, anchor="rm")
        y += row_h + 4

    tip = "Order: Kegs → Copper Pickaxe → Barn + Cheeken → Iron Pickaxe → Jam Maker + Mill → Trees → Gold → Enchanted"
    f = fit(tip, W - 70, 13)
    ctext(d, (W / 2, y + 14), tip, f, fill=GREEN)
    save(img, "milestone-budget.webp")

if __name__ == "__main__":
    money_loop()
    early_game()
    keg_profit()
    milestones()
