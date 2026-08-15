#!/usr/bin/env python3
"""Generate Moonlight Peaks Crop & Farming Guide WebP infographics (800x600).

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

def panel_text(d, box, lines, fnt, fill=CREAM, line_gap=22, start_y=None, x_pad=14):
    x0, y0, x1, y1 = box
    y = start_y if start_y is not None else y0 + 18
    for ln in lines:
        ctext(d, (x0 + x_pad, y), ln, fnt, fill=fill, anchor="lm")
        y += line_gap

# ---------------------------------------------------------------- 1. Seasonal calendar
def crop_calendar():
    img, d = canvas()
    header(d, "CROP SEASON CALENDAR", "Moonlight Peaks — all seeds by season")

    # season columns
    seasons = [
        ("SPRING", GREEN, ["Wild Potato 3n", "Carrot 6n", "Strawberry 7n*", "White/Blood Grape 5n*", "Raspberry 7n*", "Eggplant 6n", "Sugarbone 5n", "Cruelcumber 7n*", "Blueberry 9n*"]),
        ("SUMMER", GOLD, ["Gobbler 6n (magic)", "Drikker 9n (magic)", "Skunktail 9n", "Melon 7n*", "Red Corn 6n", "Sunburst 9n (magic)"]),
        ("AUTUMN", RED, ["Pumpkin 9n", "Mandrake 6n (magic)", "Radish 6n", "Lava Pepper 8n*", "Cranberry 8n*"]),
        ("WINTER", PURPLE, ["Blackberry 8n*", "Blueberry 9n*", "Dark Strawberry 9n*", "Sweet Wicca (magic)", "Black Sun Currant (magic)"]),
    ]
    col_w = (W - 56) / 4
    x = 28
    y_top = 100
    col_h = 404
    for i, (name, col, crops) in enumerate(seasons):
        x0 = x + i * (col_w + 8)
        rrect(d, (x0, y_top, x0 + col_w, y_top + col_h), 14, fill=CARD)
        rrect(d, (x0, y_top, x0 + col_w, y_top + 40), 14, fill=col)
        ctext(d, (x0 + col_w / 2, y_top + 20), name, fit(name, col_w - 12, 18, True), fill=BG)
        y = y_top + 58
        for c in crops:
            f = fit(c, col_w - 16, 15)
            ctext(d, (x0 + 10, y), c, f, fill=CREAM, anchor="lm")
            y += 34

    rrect(d, (28, y_top + col_h + 10, W - 28, H - 16), 14, fill=PANEL)
    note = "* = regrows  |  n = nights to grow  |  magic = needs Aquaflux spell"
    ctext(d, (W / 2, y_top + col_h + 32), note, fit(note, W - 70, 15), fill=MUTED)
    resized = img.resize((W, H), Image.LANCZOS)
    resized.save(os.path.join(OUT, "crop-season-calendar.webp"), "WEBP", quality=90, method=6)
    print("wrote", os.path.join(OUT, "crop-season-calendar.webp"))
    # keep the hub's existing reference accurate too
    resized.save(os.path.join(OUT, "crop_chart.webp"), "WEBP", quality=90, method=6)
    print("wrote", os.path.join(OUT, "crop_chart.webp"))

# ---------------------------------------------------------------- 2. Best crops for profit
def best_crops():
    img, d = canvas()
    header(d, "BEST CROPS FOR PROFIT", "Season profit per plant — magical first")
    rows = [
        ("1", "Gobbler", "Summer", "magic", "~800g", GOLD),
        ("2", "Drikker", "Spring / Summer", "magic", "~660g", CREAM),
        ("3", "Sweet Wicca", "Winter", "magic", "~600g", CREAM),
        ("4", "Happy Mandrake", "Autumn", "magic", "~520g", CREAM),
        ("5", "Black Sun Currant", "Winter", "magic", "~380g", CREAM),
    ]
    y = 104
    for medal, crop, season, tag, profit, accent in rows:
        rrect(d, (28, y, W - 28, y + 72), 14, fill=PANEL)
        rrect(d, (36, y + 12, 78, y + 60), 24, fill=accent)
        ctext(d, (57, y + 36), medal, font(24, True), fill=BG)
        ctext(d, (108, y + 36), crop, font(20, True), fill=CREAM, anchor="lm")
        rrect(d, (330, y + 18, 400, y + 54), 10, fill=PURPLE)
        ctext(d, (365, y + 36), tag, fit(tag, 64, 13, True), fill=BG, anchor="mm")
        ctext(d, (530, y + 36), season, font(15), fill=MUTED, anchor="lm")
        ctext(d, (W - 40, y + 36), profit, font(22, True), fill=GOLD, anchor="rm")
        y += 82
    rrect(d, (28, y + 4, W - 28, H - 14), 14, fill=CARD)
    note = "Best normal-water crops:  Carrot (Spring)  ·  Skunktail (Summer)  ·  Pumpkin (Autumn)"
    ctext(d, (W / 2, y + 32), note, fit(note, W - 70, 15), fill=GREEN)
    save(img, "best-crops-profit.webp")

# ---------------------------------------------------------------- 3. Processing chain
def processing():
    img, d = canvas()
    header(d, "FROM FIELD TO GOLD", "Process everything — never sell raw")

    # Keg chain
    rrect(d, (28, 100, W - 28, 250), 14, fill=CARD)
    ctext(d, (W / 2, 124), "KEG  (10 Wood · from Orlock)", font(18, True), fill=GOLD)
    keg_items = [
        ("Grapes", "4 Blood Grape → Red Wine ~360g"),
        ("", "4 White Grape → White Wine ~460g"),
        ("", "2+2 White & Blood + Mana Essence → Mana Wine ~3×"),
        ("Berries", "Strawberry / Raspberry / Melon → Juice"),
    ]
    y = 152
    for lead, rest in keg_items:
        f1 = font(14, True)
        f2 = fit(rest, 560, 14)
        if lead:
            ctext(d, (60, y), lead, f1, fill=CREAM, anchor="lm")
        ctext(d, (60 + (tlen(lead + "  ", f1) if lead else 0), y), rest, f2, fill=CREAM, anchor="lm")
        y += 24
    ctext(d, (W / 2, y + 2), "Wine sells 8–17× the raw grape value (star quality matters)", fit("Wine sells 8–17× the raw grape value (star quality matters)", W - 80, 14), fill=GREEN)

    # Mill + Jam Maker chain
    rrect(d, (28, 266, W - 28, 400), 14, fill=CARD)
    ctext(d, (W / 2, 290), "MILL + JAM MAKER", font(18, True), fill=GOLD)
    jam_lines = [
        "Mill (8,000g):  Sugarbone → Sugar",
        "Jam Maker (blueprint from Mina):  produce + Sugar → Jam & Jelly",
        "Jams sell far above raw produce — pair both machines together.",
    ]
    panel_text(d, (40, 316, W - 40, 392), jam_lines, font(14), line_gap=26)

    # Cheese Press chain
    rrect(d, (28, 416, W - 28, 556), 14, fill=CARD)
    ctext(d, (W / 2, 440), "CHEESE PRESS  (unlock by milking a dairy animal)", font(18, True), fill=GOLD)
    cheese_lines = [
        "Pig Goat Milk → Hellfeta Cheese",
        "Draculamb Milk → Ghoulembert Cheese",
        "Luna mails the blueprint the morning after your first milking.",
    ]
    panel_text(d, (40, 466, W - 40, 542), cheese_lines, font(14), line_gap=26)
    save(img, "crop-processing-chain.webp")

# ---------------------------------------------------------------- 4. Barn & animals
def animals():
    img, d = canvas()
    header(d, "BARN & ANIMALS", "Barn 4,000g · holds 4 animals · makes fertilizer")

    rrect(d, (28, 100, W - 28, 176), 14, fill=PANEL)
    unlock = "Unlock: Day 2 Spring — Ridge fixes the roof, then Luna's 'Farm Animals for Sale' quest."
    feed = "Feed daily: Refiner (20 Wood + 20 Stone) turns 1 Fiber → 2 Fodder. Pet every night."
    ctext(d, (40, 124), unlock, fit(unlock, W - 70, 15), fill=CREAM, anchor="lm")
    ctext(d, (40, 152), feed, fit(feed, W - 70, 15), fill=CREAM, anchor="lm")

    animals_data = [
        ("Cheeken", "1,200g", "Eggs · Golden Eggs"),
        ("Rabbicula", "2,800g", "Year 2 Spring"),
        ("Pig Goat", "3,500g", "Milk → Hellfeta"),
        ("Draculamb", "4,500g", "Milk + Wool"),
        ("Cowcula", "6,000g", "Cowcula Milk"),
        ("Stoney", "9,000g", "Heart Stone"),
        ("Bumpkin", "12,000g", "Plops"),
    ]
    col_w = (W - 70) / 2
    y0 = 190
    row_h = 52
    for i, (name, cost, prod) in enumerate(animals_data):
        col = i % 2
        row = i // 2
        x0 = 28 + col * (col_w + 14)
        y = y0 + row * (row_h + 12)
        rrect(d, (x0, y, x0 + col_w, y + row_h), 12, fill=CARD)
        ctext(d, (x0 + 12, y + row_h / 2), name, font(16, True), fill=GOLD, anchor="lm")
        ctext(d, (x0 + 130, y + row_h / 2), cost, font(14, True), fill=CREAM, anchor="lm")
        ctext(d, (x0 + 210, y + row_h / 2), prod, fit(prod, col_w - 220, 13), fill=MUTED, anchor="lm")
    tip = "Tip: Draculambs prefer their own kind (no Cowculas) · Pig Goats pair with Stoneys"
    ctext(d, (W / 2, 580), tip, fit(tip, W - 70, 14), fill=GREEN)
    save(img, "barn-animals-guide.webp")

if __name__ == "__main__":
    crop_calendar()
    best_crops()
    processing()
    animals()
    print("all MP crop images generated")
