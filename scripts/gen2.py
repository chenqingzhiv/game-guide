#!/usr/bin/env python3
"""Bulk-generate game guide pages for game-guide.club."""

import os, json
from datetime import datetime

DOCS = "/home/hermes/game-guide/docs"
NOW = datetime.now().strftime("%Y-%m-%d")

def w(path, content):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print(f"  OK {path}")

def page(title, description, tags, sections, faq_items=None):
    tags_str = ", ".join(tags)
    schema = ""
    if faq_items:
        qa = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
              for q, a in faq_items]
        import json
        schema = "\n".join([
            '\n<script type="application/ld+json">',
            json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                       "mainEntity": qa}, indent=2),
            '</script>'])
    sections_str = "\n\n".join(sections)
    return "\n".join(["---",
        'title: "' + title + '"',
        'description: "' + description + '"',
        "date: " + NOW,
        "tags: [" + tags_str + "]",
        "---",
        "",
        schema,
        "",
        sections_str])

print("Generating Phase 1+2 pages...")

# Phase 1: Enshrouded pages + Phase 2 expansions
# (already created by initial write_file, skipping regeneration)

# Phase 3+4+5: New games + news
# Use SIMPLE page() calls to avoid parser issues

def make_guide(path, title, desc, tags, sections):
    w(path, page(title, desc, tags, sections))

# --- Rust Index ---
make_guide("rust/index.md", "Rust Guide Hub", "Complete Rust guide hub.", ["Rust", "guide"], [
    "## What is Rust?\n\nRust is a multiplayer survival game. Start with nothing, gather resources, build bases, survive.",
    "## Quick Navigation\n\n- Beginners Guide: /rust/beginners-guide/\n- Base Building: /rust/base-building/\n- Monuments: /rust/monuments/\n- Farming: /rust/farming/\n- PvP Guide: /rust/pvp-guide/",
    "## Getting Started\n\n1. Pick a 2x or 3x modded server\n2. Spawn away from monuments\n3. Stone tools, 2x1 base, sleeping bag\n4. Day 1 goal: Secure base with door and lock",
])

# --- Rust Beginners ---
make_guide("rust/beginners-guide.md", "Rust Beginners Guide", "First week survival.", ["Rust", "beginner"], [
    "## First Hour\n\n1. Gather 2 stones, craft Rock\n2. Gather 500 wood + 200 stone for tools\n3. Build a 2x1 base\n4. Place sleeping bag\n5. Craft wooden spear for defense",
    "## First Day\n\n- 0-1h: 2x1 base + bag\n- 1-2h: Furnace\n- 2-3h: Code lock\n- 3-5h: Stone walls\n- 5-8h: Bow + arrows\n- 8-12h: Research BPs\n- 12-24h: Expand base",
    "## Scrap & BPs\n\n- Workbench L1: 75 scrap\n- Workbench L2: 500 scrap\n- Workbench L3: 1250 scrap\n- Priority: Code lock, garage door, metal tools, bow, revolver",
    "## How to NOT Get Raided\n\n1. Build away from monuments\n2. Don't look rich\n3. Stone walls (not wood)\n4. Honeycomb\n5. External TCs\n6. Garage doors on outer layer",
])

# --- Rust Base Building ---
make_guide("rust/base-building.md", "Rust Base Building", "Raid-proof designs.", ["Rust", "building"], [
    "## Base Principles\n\nEvery base needs: TC coverage, honeycomb, airlock, stone or better walls.",
    "## Popular Designs\n\n2x1 Starter: 2 foundations, 1 door, TC in triangle. Raid cost: ~4 satchels.\n\n2x2: 4 foundations + honeycomb. Garage door airlock. Raid cost: ~12 satchels.\n\nBunker Base: Drop-down bunker entrance. Raid cost: 16+ rockets.\n\nCompound: Multiple bases inside high walls. External TCs. 30+ rockets.",
    "## Honeycomb\n\nPlace triangle foundations around base. Upgrade to stone. Each layer = 6 walls raiders must breach.",
    "## Doors\n\nGarage doors on outer layer (cheaper). Armored doors on inner core. 5-7 doors between outside and loot.",
])

# --- Rust Monuments ---
make_guide("rust/monuments.md", "Rust Monuments Guide", "All monument walkthroughs.", ["Rust", "monuments"], [
    "## Monument Tiers\n\nTier 1: Gas Station, Supermarket (no rad, low risk)\nTier 2: Harbor, Water Treatment (green rad, medium)\nTier 3: Airfield, Power Plant (blue rad, high)\nTier 4: Military Tunnels, Cargo Ship, Oil Rig (red rad, extreme)",
    "## Puzzle Walkthroughs\n\nHarbor: Green fuse near dock, insert in red switch box.\n\nWater Treatment: Find fuse in main building, insert at control panel.\n\nLaunch Site: Find fuse in red hangar. Keycard in office. Elevator to top.",
    "## Radiation Protection\n\nGreen (0-10): Wood/burlap\nBlue (10-25): Hazmat + rad pills\nRed (25-50): Hazmat + 10+ pills\nExtreme (50+): Hazmat + 20+ pills",
])

# --- Rust Farming ---
make_guide("rust/farming.md", "Rust Farming Guide", "Resource gathering.", ["Rust", "farming"], [
    "## Resource Nodes\n\nStone: 500 HP, 25-40 per hit. Metal: 600 HP, 15-25 per hit. Sulfur: 700 HP, 10-20 per hit. HQM: 300 HP, 3-6 per hit.\n\nBest tool: Jackhammer (2.5x rate).",
    "## Gathering Routes\n\nForest: 5-6 stone nodes, 8-10 trees, 3-4 metal nodes. ~15 min for 3k stone, 5k wood, 1.2k metal.\n\nMountain: 8 sulfur nodes, 4 HQM nodes, 4 metal nodes. ~20 min.",
    "## Farming Base\n\n2x1 stone base with compound. External gates. 4 furnaces. Quarry base placed near mining quarry. Protect with auto-turret.",
])

# --- Rust PvP ---
make_guide("rust/pvp-guide.md", "Rust PvP Guide", "Combat mechanics.", ["Rust", "PvP"], [
    "## Weapon Tiers\n\nPrimitive: Bow, Spear, Eoka (30-50 damage)\nTier 1: Revolver, Nailgun, DB (40-70)\nTier 2: Thompson, Custom SMG, SAP (30-50)\nTier 3: AK-47, LR-300 (40-80)",
    "## Spray Patterns\n\nAK-47: First 5 shots slight pull. 6-15 medium pull. 15-30 aggressive. Practice 10 min daily.\n\nThompson: Very stable, slight upward.\n\nCustom SMG: High fire rate, hard pull.",
    "## Movement\n\nStrafe peeking: peek, shoot, hide. Never peek same spot.\n\nJump peeking: sprint, jump, aim, shoot, land, retreat.\n\nCrouching: press C mid-spray to throw off aim.",
    "## Gear\n\nPrimitive: Wood armor + crossbow + bandages\nRoaming: Roadsign + Thompson + 4 med syringes\nEndgame: Metal + AK + 6 syringes + HV ammo",
])

# --- DST Hub ---
make_guide("dst/index.md", "Don't Starve Together Guide Hub", "Complete survival database.", ["DST", "survival"], [
    "## What is DST?\n\nMultiplayer survival in a dark fantasy world. Manage hunger, sanity, health. Seasonal bosses and challenges. Steam #19 most played, 84K concurrent.",
    "## Quick Navigation\n\nBeginners: /dst/beginners-guide/\nCharacters: /dst/characters/\nBase Building: /dst/base-building/\nFarming: /dst/farming/\nBoss Fights: /dst/boss-fights/",
])

# --- DST Beginners ---
make_guide("dst/beginners-guide.md", "DST Beginners Guide", "Survive first year.", ["DST", "beginner"], [
    "## First 10 Days\n\nDay 1: Collect 30 grass, 30 twigs, flint, logs. Craft tools + torch.\nDay 2: Science machine.\nDay 3-4: Find base location near beefalo.\nDay 5: Fire pit, chest, crock pot.\nDay 5-10: Explore map, collect food.\n\nCritical: Day 15 = first hound attack.",
    "## Season Survival\n\nAutumn (Days 1-20): Mild, explore.\nWinter (21-35): Cold. Thermal stone, winter hat.\nSpring (36-55): Rain. Umbrella, lightning rod.\nSummer (56-70): Overheating. Ice flingo, chilled amulet.",
    "## Sanity\n\nCooked meat: +5. Top hat: +3.3/min. Flowers: +5. Fire at night: +1/min. Darkness: -20/min.\n\nBest sanity food: Cooked green mushrooms (+15 sanity). Taffy: 3 honey + 1 stick (+15 sanity).",
])

# --- DST Characters ---
make_guide("dst/characters.md", "DST Characters Guide", "All characters ranked.", ["DST", "characters"], [
    "## Best for Beginners\n\nWilson: Balanced, grows beard.\nWendy: Ghost sister fights for you.\nWickerbottom: Knows all recipes.\nWolfgang: Strong when full.\nWoodie: Werebeaver form.\n\nWendy is the strongest beginner.",
    "## Intermediate\n\nWigfrid: Only meat. +25% damage, -25% taken.\nWebber: Spider friends.\nWinona: Repair buildings.\nWarly: Chef. 5 food slots.\nWX-78: Robot. Eats gears.",
    "## Advanced\n\nWes: All stats reduced, challenge mode.\nMaxwell: Powerful late-game.\nWurt: Merm allies.\nWormwood: Plant-based.\nWalter: Pet Woby.",
])

# --- DST Base Building ---
make_guide("dst/base-building.md", "DST Base Building", "Mega-base layouts.", ["DST", "building"], [
    "## Location\n\nNear beefalo, central map, near sinkhole, away from spider dens. Deciduous forest is best.",
    "## Layout\n\n18x18 tiles. Farm area, chests, icebox, drying racks, science/alchemy, garden, bee boxes.",
    "## Walls\n\nGrass (300 HP): temporary. Wood (500): standard. Stone (1000): endgame. Thulecite (2000): best.\n\nDouble-wall with 1-tile gap. 20+ tooth traps outside.",
])

# --- DST Farming ---
make_guide("dst/farming.md", "DST Farming Guide", "Crops and cooking.", ["DST", "farming"], [
    "## Crops\n\nCarrot: 10 days, 12.5 hunger. Corn: 15 days, 25. Dragon Fruit: 10 days, 75 (best for Dragon Pie). Pumpkin: 10 days, 37.5.\n\nBest: Dragon Fruit Pie = 75 hunger, 40 health, 5 sanity.",
    "## Giant Crops\n\nSame crop close together + fertilizer + water + talking. Yield: 6-8 per harvest.\n\nBest combo: Dragon Fruit + Tomato + Carrot.",
    "## Bee Boxes\n\n6-8 boxes with 20+ flowers nearby. 1 honey per 3.4 days.\n\nBest recipes: Bacon & Eggs (75 hunger), Honey Ham (75), Meatballs (62.5), Pierogi (37.5+40 health).",
])

# --- DST Boss Fights ---
make_guide("dst/boss-fights.md", "DST Boss Guide", "All bosses.", ["DST", "bosses"], [
    "## Seasonal\n\nDeerclops (Winter): 4000 HP, 75 AoE. Kite 3 hits, dodge.\nBearger (Autumn): 6000 HP, 100. Kite 4-5 hits.\nMoose/Goose (Spring): 4000 HP. Use range.\nDragonfly (Summer): 27500 HP. Use pan flute.",
    "## Raid Bosses\n\nSpider Queen: 2500 HP. Fire staff.\nBee Queen: 22500 HP. Campfire wall + kiting.\nKlaus: 10000 HP. Kill deer first.\nToadstool: 52500 HP. Weather pain.\nFuelweaver: 16000 HP. Don't let him heal.",
    "## Loot Priority\n\nDeerclops Eyebrella: rain protection.\nBearger Fur: insulated pack.\nDragonfly Scales: infinite fuel furnace.\nBee Queen Crown: best head slot.",
])

# --- Stardew Valley Hub ---
make_guide("stardew-valley/index.md", "Stardew Valley Guide Hub", "Complete farming guide.", ["Stardew Valley", "farming"], [
    "## What is Stardew Valley?\n\nFarming and life simulation RPG. Inherit a farm, build relationships, explore mines, fish. 100K+ concurrent players on Steam (#12).",
    "## Quick Navigation\n\nBeginners: /stardew-valley/beginners-guide/\nFarming: /stardew-valley/farming/\nFishing: /stardew-valley/fishing/\nMining: /stardew-valley/mining/\nRelationships: /stardew-valley/relationships/",
])

# --- Stardew Beginners ---
make_guide("stardew-valley/beginners-guide.md", "Stardew Year 1 Walkthrough", "Complete Y1 guide.", ["Stardew Valley", "beginner"], [
    "## Days 1-5\n\nDay 1: Plant 15 parsnips. Visit Pierre. Buy potatoes.\nDays 2-5: Water crops, fish in ocean, forage. Save 50g for backpack upgrade.",
    "## Spring Crops\n\nStrawberry: Best (20.8g/day). Buy at Egg Festival Day 13.\nPotato: 5g/day. Cauliflower: 7.9g/day. Kale: 6.67g/day.\n\nStrawberry strat: Plant on Day 13, harvest twice.",
    "## Community Center\n\nSpring Foraging: Leek, Daffodil, Dandelion - get Spring Seeds.\nSpring Crops: Parsnips x5 - Speed-Gro.\n**Priority:** Quality Crops Bundle for Preserves Jar.",
    "## Energy\n\nEat raw parsnips early. Field snacks: 1 acorn + 1 maple seed + 1 pine cone = 45 energy.\nSalmonberry season (15-18 Spring): Forage 30+ berries.",
])

# --- Stardew Farming ---
make_guide("stardew-valley/farming.md", "Stardew Farming Guide", "Crops and animals.", ["Stardew Valley", "farming"], [
    "## Best Crops\n\nSpring: Strawberry (20.8g/day). Summer: Blueberry (20.8), Starfruit (18.9). Fall: Cranberry (18.9), Pumpkin (16.9).\n\nAll year: Ancient Fruit. Use seed maker to multiply. Coffee: 1 bean harvest every 2 days.",
    "## Keg Empire\n\nAncient Fruit Wine: 1650g. Starfruit Wine: 2250g. Hops Pale Ale: 420g.\n\nCask cellaring: Aged to iridium = 3x value. Ancient Fruit: 4950g per bottle.",
    "## Animals\n\nPigs are best: 8 pigs = ~20 truffles/day = 21,300g/day from truffle oil.\n\nChickens: 285g (gold mayo). Cows: 390g (cheese). Goats: 560g.",
    "## Greenhouse\n\nFill with 116 Ancient Fruit + 4 fruit trees. Output: 191,400g/week from wine.",
])

# --- Stardew Fishing ---
make_guide("stardew-valley/fishing.md", "Stardew Fishing Guide", "All fish locations.", ["Stardew Valley", "fishing"], [
    "## Fishing Basics\n\nCast: hold left click for distance. Reel: keep green bar on fish.\n\nRod upgrades: Bamboo (500g), Fiberglass (1800g + bait), Iridium (7500g + bait + tackle).",
    "## Best Spots\n\nMountain Lake: Largemouth Bass, Sturgeon.\nForest Pond: Catfish, Woodskip.\nOcean: Tuna, Sardine.\nRiver: Sunfish, Pike.",
    "## Most Valuable\n\nLegend (Spring, rain): 5000g. Glacierfish (Winter): 2500g. Lava Eel (Mines L100): 1500g.\n\nScorpion Carp (Desert): 675g. Sturgeon (Mountain): 125g.",
])

# --- Stardew Mining ---
make_guide("stardew-valley/mining.md", "Stardew Mining Guide", "Mines and ores.", ["Stardew Valley", "mining"], [
    "## Mine Floors\n\n1-20: Copper, bats, slimes.\n21-40: Ice, iron, dust sprites.\n41-80: Gold, ghosts, magma sparkers.\n81-120: Gold, iridium, shadow brutes.\nGoal: Floor 100 (Skull Key), Floor 120 (Stardrop).",
    "## Skull Cavern\n\nGo on lucky day. Bring 50+ mega bombs, 50 salads, coffee. Use Desert Warp at 6am. Bomb clusters. Skip ores, only pick iridium.\n\nIridium: 50-100 per hour vs 0-5 in normal mines.",
    "## Adventurers Guild\n\n10 Slimes: Slime Charmer Ring (immune).\n50 Dust Sprites: Burglar Ring (double loot).\n80 Void Spirits: Savage Ring (+1 speed per kill).\n150 Bats: Vampire Ring (+2 HP per kill).",
])

# --- Stardew Relationships ---
make_guide("stardew-valley/relationships.md", "Stardew Relationships", "Marriage and gifts.", ["Stardew Valley", "relationships"], [
    "## Marriage Candidates\n\nEasiest: Abigail (amethyst), Emily (cloth), Leah (salad).\n\nFavorite gifts: Shane (Pepper Poppers), Sebastian (Frozen Tear), Alex (Complete Breakfast), Harvey (Coffee).",
    "## Universal Loves\n\nPrismatic Shard, Rabbit's Foot: +80 points.\n\nArtisan goods, fruits, cooked meals, gems: liked by most.\n\nBirthday gifts give 8x friendship.",
    "## Perks\n\n2-8 hearts: events + recipes.\n10 hearts: bouquet, then mermaid pendant for marriage.\n\nBest spouse: Leah (helps farm) or Abigail (adventures).",
])

print("Rust(6) + DST(6) + Stardew(6) = 18 pages written")

# More games coming in next run...
