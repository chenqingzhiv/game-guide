#!/usr/bin/env python3
"""Generate Moonlight Peaks Winter Guide WebP infographics (800x600).

Matches the established MP infographic style: dark night-purple background,
warm cream text, green/gold/purple accent panels.
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
ICE = (150, 200, 230)

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

# ---------------------------------------------------------------- 1. Winter crops
def winter_crops():
    img, d = canvas()
    header(d, "WINTER CROP ROSTER", "Survive the cold, profit anyway")

    rows = [
        ("SWEET WICCA", "Magical · plant near Hold-Me-Close", "~600g", GREEN),
        ("BLACK SUN CURRANT", "Magical · regrows · Mana crop", "~380g", PURPLE),
        ("BLACKBERRY", "Normal water · regrows every 2", "best normal", CREAM),
        ("DARK STRAWBERRY", "Magical · regrows · Keg it", "Keg = profit", ICE),
        ("BLUEBERRY", "Spring + Winter · regrows", "Keg it", MUTED),
    ]
    y = 100
    row_h = 62
    for name, desc, profit, accent in rows:
        rrect(d, (26, y, W - 26, y + row_h), 12, fill=CARD)
        rrect(d, (36, y + 8, 300, y + row_h - 8), 8, fill=PANEL)
        ctext(d, (44, y + 24), name, fit(name, 252, 15, True), fill=accent, anchor="lm")
        ctext(d, (44, y + 45), desc, fit(desc, 252, 11), fill=CREAM, anchor="lm")
        rrect(d, (314, y + 10, 482, y + row_h - 10), 8, fill=CARD)
        ctext(d, (398, y + row_h / 2), profit, fit(profit, 156, 14, True), fill=GOLD, anchor="lm")
        ctext(d, (500, y + row_h / 2), "⚡ = needs Aquaflux to water", fit("⚡ = needs Aquaflux to water", 250, 11), fill=MUTED, anchor="lm")
        y += row_h + 6

    rrect(d, (26, y + 2, W - 26, H - 14), 14, fill=PANEL)
    tip = "Priority: Sweet Wicca → Black Sun Currant → Blackberry · Greenhouse (Spring 11) unlocks year-round"
    ctext(d, (W / 2, y + 32), tip, fit(tip, W - 70, 15, True), fill=GREEN)
    save(img, "winter-crops.webp")

# ---------------------------------------------------------------- 2. Winter festivals
def winter_festivals():
    img, d = canvas()
    header(d, "WINTER FESTIVALS", "Two permanent boosts — don't skip them")

    panels = [
        ("FESTIVAL OF ETERNAL NIGHT · WINTER 13", ICE, [
            "Night Market — Mana Shard ×3",
            "(+10 Max Mana each, limit 3)",
            "Secret Gift Exchange — double hearts",
            "Ice Sculpture — Ice Crystal / 5,000g",
            "Fireworks 11 PM — +3 hearts",
            "Save 15,000–20,000g beforehand",
        ]),
        ("NEW YEAR'S DAWN VIGIL · WINTER 28", GOLD, [
            "Midnight Toast — +10 Max Stamina",
            "Resolution Letter — +5% one skill",
            "Year in Review — +1 heart all NPCs",
            "Dawn Vigil — Sunrise Painting (15,000g)",
            "Ends Year 1 → Year 2 begins",
            "Do NOT sleep through it",
        ]),
    ]
    panel_w = (W - 52 - 14) / 2
    y0, y1 = 100, 470
    for i, (title, col, lines) in enumerate(panels):
        px = 26 + i * (panel_w + 14)
        rrect(d, (px, y0, px + panel_w, y1), 14, fill=CARD)
        rrect(d, (px, y0, px + panel_w, y0 + 40), 14, fill=col)
        ctext(d, (px + panel_w / 2, y0 + 20), title, fit(title, panel_w - 16, 14, True), fill=BG)
        panel_lines(d, px + 16, y0 + 60, lines, font(13), gap=23, max_w=panel_w - 32)

    rrect(d, (26, 486, W - 26, H - 16), 14, fill=PANEL)
    tip = "Both are permanent-stat events — the only +Max Mana and +Max Stamina in the game"
    ctext(d, (W / 2, 542), tip, fit(tip, W - 70, 17, True), fill=GOLD)
    save(img, "winter-festivals.webp")

# ---------------------------------------------------------------- 3. Winter prep checklist
def winter_checklist():
    img, d = canvas()
    header(d, "WINTER PREP CHECKLIST", "Do this before Winter 1 — the season runs itself")

    items = [
        ("WIN THE GREENHOUSE", "Spring 11 Crop Display Contest — or stock magic crops", GREEN),
        ("SAVE 15–20K", "Funds all 3 Mana Shards at the Winter 13 Night Market", GOLD),
        ("HOARD SOUL BLOBS", "100 total → Antique Clock (25-minute nights)", CREAM),
        ("STOCK WINTER SEEDS", "Blackberry, Blueberry + magic-crop materials", PURPLE),
        ("KEEP 1–2 OF EVERYTHING", "Winter quests & recipes want the items you'd sell", MUTED),
        ("BUY GOLD TOOL IN AUTUMN", "6-day wait ends in time to Enchant during winter", ICE),
        ("DON'T SKIP WINTER 28", "Midnight Toast = permanent +10 Max Stamina", GOLD),
    ]
    y = 98
    row_h = 52
    for name, desc, accent in items:
        rrect(d, (26, y, W - 26, y + row_h), 10, fill=CARD)
        rrect(d, (36, y + 6, 58, y + row_h - 6), 6, fill=PANEL)
        ctext(d, (47, y + row_h / 2), "✔", font(18, True), fill=GREEN, anchor="mm")
        rrect(d, (70, y + 6, 290, y + row_h - 6), 8, fill=PANEL)
        ctext(d, (78, y + row_h / 2), name, fit(name, 206, 12, True), fill=accent, anchor="lm")
        f = fit(desc, W - 306 - 36, 11)
        ctext(d, (304, y + row_h / 2), desc, f, fill=CREAM, anchor="lm")
        y += row_h + 4

    rrect(d, (26, y + 4, W - 26, H - 14), 14, fill=PANEL)
    tip = "Prep right and Winter turns into the endgame: Greenhouse + Enchanted tools + Antique Clock"
    ctext(d, (W / 2, y + 30), tip, fit(tip, W - 70, 15, True), fill=GOLD)
    save(img, "winter-checklist.webp")

if __name__ == "__main__":
    winter_crops()
    winter_festivals()
    winter_checklist()
