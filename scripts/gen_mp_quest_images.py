#!/usr/bin/env python3
"""Generate Moonlight Peaks Story & Quest Progression Guide WebP infographics (800x600).

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

# ---------------------------------------------------------------- 1. Story flow
def story_flow():
    img, d = canvas()
    header(d, "THE MAIN QUESTLINE", "Moonlight Peaks — story unlocks every system")

    boxes = [
        ("1 · SETTLE", GOLD, [
            "The Need for Herbs",
            "A Roof Over Your Head",
            "Orlock's Wine Scheme",
            "Keg + Refiner blueprints",
        ]),
        ("2 · MAGIC", PURPLE, [
            "The Magic of Crops",
            "Repair your wand (Sabrina)",
            "Aquaflux I · Cauldron",
            "Cooking — Hungry Heart",
        ]),
        ("3 · MINE", GREEN, [
            "A Bridge Too Far",
            "Open Misty Shores",
            "Cave of Echoes · Furnace",
            "Coastal Access — beach",
        ]),
        ("4 · COVEN", CREAM, [
            "Maturio → Tears → Hoist",
            "Webb Crest earned",
            "Advanced spells unlock",
        ]),
        ("5 · FORMS", RED, [
            "Hellkitten · Mermaid · Bat",
            "Each has its own quest",
            "Open gold ore & caves",
        ]),
    ]
    box_w = 128
    gap = 12
    x0 = 22
    y0, y1 = 100, 360
    for i, (name, col, lines) in enumerate(boxes):
        bx = x0 + i * (box_w + gap)
        rrect(d, (bx, y0, bx + box_w, y1), 12, fill=CARD)
        rrect(d, (bx, y0, bx + box_w, y0 + 38), 12, fill=col)
        ctext(d, (bx + box_w / 2, y0 + 19), name, fit(name, box_w - 10, 15, True), fill=BG)
        y = y0 + 52
        for ln in lines:
            f = fit(ln, box_w - 16, 12)
            for wl in wrap_lines(ln, f, box_w - 16):
                ctext(d, (bx + 8, y), wl, f, fill=CREAM, anchor="lm")
                y += 20
    # arrows between boxes
    for i in range(4):
        ax = x0 + box_w + gap + i * (box_w + gap) - 8
        ay = (y0 + y1) // 2
        d.polygon([(ax * SS, (ay - 9) * SS), (ax * SS, (ay + 9) * SS), ((ax + 12) * SS, ay * SS)], fill=GOLD)

    rrect(d, (26, 382, W - 26, H - 18), 14, fill=CARD)
    ctext(d, (W / 2, 416), "MONEY NEVER SKIPS A STORY BEAT", font(18, True), fill=GREEN)
    ctext(d, (W / 2, 452), "Follow the map sparkles · read the mailbox · keep 1–2 of everything",
          fit("Follow the map sparkles · read the mailbox · keep 1–2 of everything", W - 70, 15), fill=CREAM)
    ctext(d, (W / 2, 492), "Night 1 tutorial → Spring magic → Early-Spring mine → Coven → Autumn forms",
          fit("Night 1 tutorial → Spring magic → Early-Spring mine → Coven → Autumn forms", W - 70, 14), fill=MUTED)
    save(img, "story-flow.webp")

# ---------------------------------------------------------------- 2. Quest timeline
def quest_timeline():
    img, d = canvas()
    header(d, "YEAR 1 QUEST TIMELINE", "What unlocks and when")

    seasons = [
        ("SPRING", GREEN, [
            "Nights 4–6 · The Need for Herbs",
            "Nights 4–6 · Orlock's Wine Scheme",
            "Early · A Roof Over Your Head",
            "Early · A Bridge Too Far → mine",
            "Early · Coastal Access → beach",
            "Spring · The Magic of Crops",
            "Spring 11 · Greenhouse contest",
            "Spring 24 · Scythe + Mana Extractor",
        ]),
        ("SUMMER", GOLD, [
            "Early · The Hungry Heart → cooking",
            "Summer 14 · Solstice Soirée (Love Potion)",
            "Summer 28 · Enchanted Rod / Bug Net",
            "Build the Mana Extractor",
            "Start the Mermaid quest chain",
        ]),
        ("AUTUMN", PURPLE, [
            "Fall 16 · Harvest Festival wins",
            "Fall 27 · Spirit's Eve unlocks",
            "Mermaid form usually lands",
            "Gold tools → wait 6 days",
            "Master of the Night → Bat form",
        ]),
        ("WINTER", CREAM, [
            "Winter 13 · Mana Shards (×3)",
            "Winter 28 · +10 Max Stamina",
            "Enchant your tools",
            "Greenhouse = winter crops",
            "Antique Clock if 100 Soul Blobs",
        ]),
    ]
    panel_w = (W - 52 - 3 * 14) / 4
    y0, y1 = 100, 480
    for i, (title, col, lines) in enumerate(seasons):
        px = 26 + i * (panel_w + 14)
        rrect(d, (px, y0, px + panel_w, y1), 14, fill=CARD)
        rrect(d, (px, y0, px + panel_w, y0 + 36), 14, fill=col)
        ctext(d, (px + panel_w / 2, y0 + 18), title, fit(title, panel_w - 10, 16, True), fill=BG)
        panel_lines(d, px + 12, y0 + 52, lines, font(12), gap=19, max_w=panel_w - 24)

    rrect(d, (26, 494, W - 26, H - 16), 14, fill=PANEL)
    tip = "Rule: quest first, money second — every unlock above is story-gated"
    ctext(d, (W / 2, 548), tip, fit(tip, W - 70, 17, True), fill=GOLD)
    save(img, "quest-timeline.webp")

# ---------------------------------------------------------------- 3. Form unlock chains
def form_chains():
    img, d = canvas()
    header(d, "FORM UNLOCK CHAINS", "Three transformations, three questlines")

    forms = [
        ("HELLKITTEN (CAT)", GOLD, "The Dinner Party", [
            "A stray spell from Brook",
            "turns you into a cat",
            "Nights 7–8, right after",
            "the wand is repaired",
        ], [
            "Faster movement",
            "Less stamina drain",
            "Squeeze into small holes",
            "Dig swirls — no shovel",
        ]),
        ("MERMAID (AQUA)", PURPLE, "4-quest chain", [
            "A Curious Passage (Ludo)",
            "The Mysterious Bay (Samuel)",
            "Ludo's Plan (bridge repair)",
            "A Mermaid's Wish (potion)",
        ], [
            "Swim to eastern gold ore",
            "Dive sparkly water ripples",
            "Usually lands Autumn Y1",
            "Samuel proposes to Kim",
        ]),
        ("BAT", CREAM, "Master of the Night", [
            "Restore the Moon",
            "Help drunk Orlock rebuild",
            "his Chalice",
            "Late-game transformation",
        ], [
            "Fly to northern gold ore",
            "Reach northern ledges",
            "Interact with glowing",
            "windows for items",
        ]),
    ]
    panel_w = (W - 52 - 2 * 14) / 3
    y0, y1 = 100, 470
    for i, (name, col, qname, chain, perks) in enumerate(forms):
        px = 26 + i * (panel_w + 14)
        rrect(d, (px, y0, px + panel_w, y1), 14, fill=CARD)
        rrect(d, (px, y0, px + panel_w, y0 + 40), 14, fill=col)
        ctext(d, (px + panel_w / 2, y0 + 20), name, fit(name, panel_w - 12, 15, True), fill=BG)
        # quest label
        rrect(d, (px + 10, y0 + 52, px + panel_w - 10, y0 + 80), 10, fill=PANEL)
        ctext(d, (px + panel_w / 2, y0 + 66), qname, fit(qname, panel_w - 24, 13, True), fill=GOLD)
        # chain lines
        y = y0 + 96
        for ln in chain:
            f = fit(ln, panel_w - 24, 12)
            for wl in wrap_lines(ln, f, panel_w - 24):
                ctext(d, (px + 14, y), "•  " + wl, f, fill=CREAM, anchor="lm")
                y += 18
        # divider
        y += 6
        rrect(d, (px + 10, y, px + panel_w - 10, y + 2), 1, fill=GOLD)
        y += 12
        for ln in perks:
            f = fit(ln, panel_w - 24, 12)
            for wl in wrap_lines(ln, f, panel_w - 24):
                ctext(d, (px + 14, y), "»  " + wl, f, fill=GREEN, anchor="lm")
                y += 18

    rrect(d, (26, 486, W - 26, H - 16), 14, fill=PANEL)
    tip = "Forms + pickaxe tiers together unlock gold ore, rose quartz and the deepest caves"
    ctext(d, (W / 2, 542), tip, fit(tip, W - 70, 17, True), fill=GOLD)
    save(img, "form-unlock-chains.webp")

# ---------------------------------------------------------------- 4. Unlock checklist
def unlock_checklist():
    img, d = canvas()
    header(d, "UNLOCK CHECKLIST", "Locked content & how to open it")

    rows = [
        ("MAGIC + AQUAFLUX", "Finish \"The Magic of Crops\" → repair your wand at Webb of Wonders", GOLD),
        ("POTIONS + COOKING", "\"Mend it with Magic\" (Cauldron) → \"The Hungry Heart\" (cooking)", PURPLE),
        ("THE MINE", "Finish \"A Bridge Too Far\" → Misty Shores + Cave of Echoes", GREEN),
        ("THE BEACH", "Complete \"Coastal Access\" — do it before Summer 14", CREAM),
        ("ADVANCED SPELLS", "Moonlit Coven: Maturio I → Tomorrow's Tears → Hoisthaven", PURPLE),
        ("GOLD ORE", "Mermaid form (east lake) + Bat form (north ledge) + Iron Pickaxe", GOLD),
        ("LONGER NIGHTS", "100 Soul Blobs → Death → Antique Clock (25-min nights)", CREAM),
        ("ZERO-STAMINA TOOLS", "Gold tool + wait 6 days + 48,000g + 5 Mana Essence → Enchanted", GREEN),
        ("WINTER FARMING", "Win Spring 11 Crop Display Contest → Greenhouse blueprint", GOLD),
        ("MANA ESSENCE", "Score 200+ at Spring 24 Blood Grape Stomping → Mana Extractor", PURPLE),
    ]
    y = 96
    row_h = 40
    for name, how, accent in rows:
        rrect(d, (26, y, W - 26, y + row_h), 10, fill=CARD)
        rrect(d, (36, y + 7, 226, y + row_h - 7), 8, fill=PANEL)
        ctext(d, (44, y + row_h / 2), name, fit(name, 176, 12, True), fill=accent, anchor="lm")
        f = fit(how, W - 250 - 40, 12)
        ctext(d, (240, y + row_h / 2), how, f, fill=CREAM, anchor="lm")
        y += row_h + 4

    rrect(d, (26, y + 4, W - 26, H - 14), 14, fill=PANEL)
    ctext(d, (W / 2, y + 30), "Tip: keep 1–2 of every item — quests, recipes and the museum all want them",
          fit("Tip: keep 1–2 of every item — quests, recipes and the museum all want them", W - 70, 15, True), fill=GREEN)
    save(img, "unlock-checklist.webp")

if __name__ == "__main__":
    story_flow()
    quest_timeline()
    form_chains()
    unlock_checklist()
