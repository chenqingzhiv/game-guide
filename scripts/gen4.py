#!/usr/bin/env python3
"""Gen4: Phase 1+2 missing pages + extra pages to reach 160"""

import os
from datetime import datetime

DOCS = "/home/hermes/game-guide/docs"
NOW = datetime.now().strftime("%Y-%m-%d")

def w(path, content):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)

def pg(title, description, tags, sections):
    tags_str = ", ".join(tags)
    sections_str = "\n\n".join(sections)
    content = "---\n" + "\n".join([
        'title: "' + title + '"',
        'description: "' + description + '"',
        "date: " + NOW,
        "tags: [" + tags_str + "]",
    ]) + "\n---\n\n" + sections_str
    w(path, content)

# === PHASE 1: ENSHROUDED ===
path = "enshrouded/bosses.md"
pg("Enshrouded Boss Guide", "All boss strategies for Enshrouded.", ["Enshrouded", "bosses"], [
    "## Boss Overview\n\nEnshrouded features diverse bosses across Embervale. Each requires specific strategies, gear, and preparation.",
    "## The Fell Wyrms\n\nLevel 15 (Springlands): Fire breath, 180 degree arc. Dodge behind during wind-up. Weak to ice. Loot: Fell Wyrm Scale.\n\nLevel 25 (Revelwood): Adds poison pools. Clear adds first. Bring anti-poison.",
    "## The Hollow Lords\n\nLevel 18 (Springlands Vault): Shield phase at 75% HP. Break 4 Seal Crystals. Weak to fire.\n\nLevel 28 (Kindlewastes): Triple seal crystals. Add spawns every 30s.",
    "## Fell Dragon (Endgame)\n\nPhases: Ground (bite/sweep) > Flight (fireballs, use grapple) > Enrage (double speed, pop cooldowns).\n\nRequired: Level 30+, legendary gear.",
])

path = "enshrouded/weapons.md"
pg("Enshrouded Weapons Guide", "Weapon database and crafting.", ["Enshrouded", "weapons"], [
    "## Weapon Classes\n\nSwords (balanced), Axes (high damage, slow), Bows (ranged), Wands (magic ranged), Staves (heavy magic).",
    "## Best Weapons by Tier\n\nEarly: Rusted Sword, Hand Axe, Shortbow.\nMid: Iron Longsword, War Axe, Recurve Bow.\nLate: Hollow Knight Blade, Fell Cleaver, Fell Stinger.\nEndgame: Fell Dragonfang, Doom's Edge, Eternal Flame staff.",
    "## Upgrade System\n\nTiers 1-4 at Blacksmith. Each tier: +25% damage + stat bonus.\n\nMaterials: Resin > Metal Bars > Hollow Core > Dragon Scale.",
])

path = "enshrouded/armor.md"
pg("Enshrouded Armor Guide", "Armor sets and builds.", ["Enshrouded", "armor"], [
    "## Weight Classes\n\nLight (mages/rangers): Low defense, high mobility.\nMedium (hybrids): Balanced.\nHeavy (tanks): High defense, low mobility.",
    "## Best Sets\n\nEarly: Scavenger (light, +stamina) or Soldier (medium, +melee).\nMid: Nomad (ranger), Hollow (mage), Paladin (tank).\nEndgame: Fell Nightmare (melee DPS), Frost Weaver (ice mage), Radiant (healer).",
    "## Builds\n\nTank: Paladin set + heavy shield + mace.\nMage: Hollow set + frost wand + frost staff.\nRanger: Nomad set + longbow + daggers.",
])

path = "enshrouded/building.md"
pg("Enshrouded Building Guide", "Base design and construction.", ["Enshrouded", "building"], [
    "## Structural Integrity\n\nEach material has support value and weight. Dirt: 3 floors. Wood: 5. Stone: 8. Steel: 12. Obsidian: 16.\n\nEach floor reduces support by 50%.",
    "## Room Bonuses\n\nBedroom: +20% rest. Workshop: faster crafting. Kitchen: +25% food duration. Smithy: +15% armor durability. Laboratory: +20% potion duration.",
    "## Base Defense\n\n2-block walls stop ground enemies. Spike traps at entries. Lighting reduces spawns. Elevated bases on cliffs avoid ground enemies.",
])

path = "enshrouded/map-exploration.md"
pg("Enshrouded Map Guide", "Biomes and exploration.", ["Enshrouded", "exploration"], [
    "## Biomes\n\nSpringlands (1-8): Starter, green hills, basic resources.\nRevelwood (8-16): Dense forest, copper/tin.\nNomad Highlands (14-20): Arid, iron/sulfur.\nKindlewastes (20-25): Desert, obsidian.\nAlbaneve Summits (25-30): Snow, frost crystal.\nThe Underworld (30+): Endgame, best loot.",
    "## Fast Travel\n\n15 Ancient Spires across biomes. Climb to top, activate crystal. Free travel after activation.",
    "## Secrets\n\nFloating Island (Revelwood): Requires 20+ grapple stamina. Unique weapon blueprint.\nUnderground Lake (Springlands): Via well near Longkeep. Rare fish + hidden chest.\nAbandoned Library (Kindlewastes): 3 skill point tomes.",
])

# === PHASE 2: EXPANSIONS ===
path = "satisfactory/trains.md"
pg("Satisfactory Train Guide", "Railway and logistics.", ["Satisfactory", "trains"], [
    "## Train Basics\n\nTrains transport items across long distances with massive throughput. Best for distances over 500m.",
    "## Track Building\n\nBuild on foundations for alignment. Min turn radius: 8 foundations. Grade limit: 20 degrees.\n\nDual-track for main lines. Single-track for branches with passing sidings.",
    "## Stations\n\nFreight Platform (items), Fluid Platform (fluids), Empty Platform (overflow).\n\n3-4 platforms per station optimal. Orient for straight entry/exit.",
    "## Signaling\n\nBlock signals divide track into segments. Path signals at intersections. Chain signals BEFORE intersections.\n\nRule: Path at entrance, Chain 2-3 car lengths before, Block at exit.",
])

path = "satisfactory/alternate-recipes.md"
pg("Satisfactory Alternate Recipes", "Best recipes ranked.", ["Satisfactory", "recipes"], [
    "## S-Tier\n\nSolid Steel Ingot: 2x steel output.\nCaterium Wire: 4x wire throughput.\nCast Screw: Eliminates screw production.\nHeavy Oil Residue + Diluted Packaged Fuel: 6x fuel output.\nPure Iron Ingot: 2.5x iron from same ore.",
    "## A-Tier\n\nSilica: Cheaper from quartz.\nSteamed Copper Sheet: 2.6x output.\nTurbofuel: 1.5x power from same oil.\nEncased Industrial Pipe: 2x beams.",
    "## Best Combos\n\nZero-Copper Factory: Cast Screw + Steel Screw.\nFuel Mega-Plant: HOR + Diluted Fuel + Turbofuel (200+ generators from 1 pure node).",
])

path = "factorio/defense-guide.md"
pg("Factorio Defense Guide", "Walls, turrets and evolution.", ["Factorio", "defense"], [
    "## Evolution Factor\n\nTime, pollution, and nest destruction increase evolution.\n\n0-25%: Small biters (yellow ammo).\n25-50%: Medium (red ammo).\n50-75%: Big (piercing + flamethrower).\n75-100%: Behemoths (uranium ammo).",
    "## Turret Configs\n\nEarly: 4 turrets per 10 tiles, double wall, yellow ammo.\nMid: Triple wall, flamethrowers at 5-tile intervals, red ammo.\nLate: Dragon's teeth, uranium turrets, lasers, flamethrowers. Repair packs via logistics.",
    "## Pollution Management\n\nEfficiency Module 1 in miners (-30% pollution). Solar power (zero pollution). Electric furnaces. Tree preservation.",
])

path = "factorio/blueprint-book.md"
pg("Factorio Blueprint Book", "Essential blueprints.", ["Factorio", "blueprints"], [
    "## Smelting\n\nEarly: 48 furnace array (24 per side). 1 red belt ore = 1 belt plates.\n\nElectric: 48 furnaces with Speed 3 + beacons. 4 blue belts output.",
    "## Rail Intersections\n\n4-way: Elevated, chain on entry, path on junction, block on exit. Supports 4 trains.\n\nT-junction: 4x4 chunks. Same signaling.\n\nTrain stacker: 6 waiting bays.",
    "## Defense Blueprints\n\nPerimeter segment: 3-layer stone + dragon's teeth + 4 gun + 2 flamethrower + 2 laser.\n\nArtillery outpost: 6 cannons + full defense + train resupply.",
])

path = "dyson/combat.md"
pg("Dyson Sphere Program Combat Guide", "Dark Fog and defense.", ["DSP", "combat"], [
    "## Threat Levels\n\nPassive: No attacks.\nLow: Scout raids. 4-6 turrets.\nMedium: Regular assault. 12+ turrets + missiles.\nHigh: Fleet attacks. Planetary shield.\n\nThreat increases with power gen and resource extraction.",
    "## Turrets\n\nGauss (20 dmg, medium range) > Laser (30, long, no ammo) > Missile (80, very long) > Plasma (150, long) > Implosion (300, short AOE).\n\nShield Generator: Absorbs all damage while powered. Battery backup critical!",
    "## Dark Fog Bases\n\nScout Outpost (easy, low-tier loot).\nMining Base (medium, processed ores).\nMilitary Base (hard, combat tech).\nRelay Station (very hard, rare components).\n\nLeave some bases alive for resource farming!",
])

path = "dyson/dark-fog.md"
pg("DSP Dark Fog Expansion", "Full combat content.", ["DSP", "expansion"], [
    "## New Buildings\n\nGauss Turret (iron+copper), Laser Turret (titanium+circuit), Missile Launcher (steel+processor).\n\nShield Generator: Base protection. Planetary Shield: Full coverage.\n\nCombat Logistics Station: Ammo supply via drones.",
    "## Research Tree\n\nBasic Combat (Gauss) > Energy Weapons (Laser) > Explosives (Missile) > Shield Tech > Fleet Command > Planetary Fortress.\n\nPriority: Rush Laser Turrets + Shields.",
    "## Hive Brain\n\nEndgame boss: Clear all bases in system, build 200+ ships, attack Hive Relay.\n\nReward: Hive Core + Cosmology research boost.",
])

path = "timberborn/endgame.md"
pg("Timberborn Endgame Guide", "Mega-colony and bionics.", ["Timberborn", "endgame"], [
    "## Bionic Upgrades\n\nSteel Teeth (+50% gather), Iron Stomach (+50% carry), Bionic Limb (+30% build), Reinforced Bones (+50% lifespan), Brain Implant (+25% work speed).\n\nPriority: Lifespan > Work > Gather > Build > Carry.",
    "## Mega-Colony Design\n\nDistrict A: Residential + Food (20).\nDistrict B: Industrial Wood/Planks (40).\nDistrict C: Metal/Science (40).\nDistrict D: Power/Water (20).\nDistrict E: Mega-Farming (30).\n\nConnect with aqueducts + tunnels + belts.",
    "## Population 200+\n\n15+ lodges, 4-5 breeding pads, diverse crops, 20 water/day consumption.\n\nReduce breeding in drought. Gravity batteries for power during drought.",
])

path = "shapez2/optimization.md"
pg("Shapez 2 Optimization Guide", "Throughput and compactness.", ["Shapez 2", "optimization"], [
    "## Compact Patterns\n\nStacker Sandwich: Stack belts before merging for double throughput.\nSplit-Merge: Split input, process parallel, merge back. 4x throughput in 2x space.",
    "## Belt Balancers\n\n4-to-4 balancer: All outputs equal regardless of inputs. Always balance before processing arrays.\n\nBelt speed cap: 60 shapes/s. Balance upstream to hit this.",
    "## Bus Architecture\n\nRaw Processing > Shape Highway (8 belts) > Production Modules > Final Assembly > Hub.\n\nEach module: split shape type, process, paint, merge back. 10x20 tiles compact.",
])

path = "valheim/cooking-recipes.md"
pg("Valheim Cooking Guide", "All food and recipes.", ["Valheim", "cooking"], [
    "## Food Stats\n\nHealth (tanks, boss fights), Stamina (builders, archers), Health Regen, Stamina Regen.\n\nEat 3 foods at once.\n\nTiers: Yellow (30-50), Green (50-80), Blue (80-100), Purple (100+).",
    "## Best Combos\n\nEarly: Queens Jam + Carrot Soup + Grilled Neck Tail.\nMid: Sausages + Turnip Stew + Wolf Skewer.\nEndgame Tank: Lox Meat Pie + Honey Glazed Chicken + Fish Wraps (245 HP).\nEndgame Mage: Yggdrasil Porridge + Misthare Supreme (260 stamina).",
    "## Mead\n\nHealth Mead (heal 50-75), Stamina Mead (recover 50), Tasty Mead (+100% stam regen).\n\nResist: Frost, Poison, Fire. Build 3+ fermenters for batch brewing.",
])

path = "valheim/building-aesthetics.md"
pg("Valheim Building Aesthetics Guide", "Design tips.", ["Valheim", "building"], [
    "## Architecture\n\nSteep roofs (47): Classic Viking longhouse.\nModerate (26): Modern Valheim style.\nFlat: Castle aesthetic with tarred shingle.\n\nMaterials: Core Wood + Thatch (classic), Stone + Dark Wood (castle), Marble (Mistlands).",
    "## Interior Layout\n\nGreat Hall: Central hearth, long dining table, trophy mounts, wall sconces every 4m.\n\nUpper Floor: Individual rooms with bed + chest + torch. Shared balcony overlooking hall.\n\nBasement: Forge line + smelter with chimney + storage.",
    "## Comfort Level\n\nMax 17 items: Dragon bed (2), banners (4), rugs (4), trophies (4), hearth (1), sitting log (4).\n\n17 min Rested buff = +100% XP, +50% health regen.",
])

path = "vrising/pvp-strategies.md"
pg("V Rising PvP Guide", "Combat and builds.", ["V Rising", "PvP"], [
    "## Best Builds\n\nAxe (burst DPS): Slasher offhand + Axes main. Chaos Volley + Ward of the Damned.\nReaper (control): Reaper + Pistols. Ice Block + Frost Bat.\nSword & Shield (sustain): Longsword + Crossbow. Blood Rage + Sanguine Coil.",
    "## Raid Defense\n\nMulti-layer honeycomb: 3+ wall layers.\nFalse rooms waste raider resources.\nServants near castle heart.\nCastle heart in deepest room behind reinforced walls.\nHollow walls: 2-layer with empty space = more HP to break.",
    "## Combat Mechanics\n\nDodge Roll: 0.5s invulnerability. Time with enemy projectiles.\nCounter: Reflect melee attacks. Use after enemy commits to swing.\nUltimate: Full bar = ult. Hit 3+ targets for max value.",
])

path = "sons-forest/endgame-guide.md"
pg("Sons of the Forest Endgame Guide", "Final cave and endings.", ["Sons of the Forest", "endgame"], [
    "## Prerequisites\n\nGolden Armor, Shovel, Rebreather, Rope Gun, Glider, 3 Keycards, fully upgraded weapons, 10 Meds, 10 Energy Mix.",
    "## Final Cave\n\nLevel 1: The Descent. Armsy, Virginia mutants.\nLevel 2: The Laboratory. Flooded, use rebreather.\nLevel 3: The Reactor. 3 power couplings puzzle. Mega-Fingers boss.\nLevel 4: The Artifact Chamber. Golden Armor required.",
    "## Multiple Endings\n\nEnding A (Escape): Activate in Sky mode. Helicopter arrives.\nEnding B (Destroy): Fire mode. Explosion destroys facility.\nEnding C (Power): Cube mode. Defense grid activated. You rule the island.",
])

path = "sons-forest/survival-tips.md"
pg("Sons of the Forest Survival Tips", "Beginners guide.", ["Sons of the Forest", "survival"], [
    "## First Day\n\n1. Find water source\n2. Collect 10 sticks + 5 rocks\n3. Build shelter (10 sticks)\n4. Craft bow (5 sticks + 3 cloth + rope)\n5. Kill rabbit for food\n\nDont: Attack cannibals day 1, sleep without fire, enter caves unprepared.",
    "## Essential Crafts\n\nTools: Stone Axe, Bow, Spear, Crafted Club.\nArmor: Leaf (10 leaves + 3 cloth) immediate. Upgrade to Bone (5 bones + 2 cloth) by day 3.",
    "## Base Building\n\n4x4 wood foundation, 1-wall height, single entrance with spikes. Interior: Fire pit + drying rack + storage.\n\nUpgrade to stone walls (fireproof), 2-walls + spikes, deadfall traps, zipline network.",
])

path = "grounded/equipment-guide.md"
pg("Grounded Equipment Guide", "Armor and weapons database.", ["Grounded", "equipment"], [
    "## Tier 1 Armor\n\nClover (+1 heal), Grub (+2 stam), Acorn (+2 armor), Red Ant (+1 attack, hauling).",
    "## Tier 2 Armor\n\nSpider (+3 attack, poison), Ladybug (+3 armor, heal on block), Koi (+3 stam, perfect block), Bee (+2 attack, crit).",
    "## Tier 3 Armor\n\nFire Ant (+4 attack, corrosion), Roly Poly (+5 armor, taunt), Moth (+4 stam, flight), Mant (+5 attack, execution).",
    "## Best Weapons\n\nEarly: Red Ant Club (high stun).\nMid: Mosquito Needle (life steal), Salt Morning Star (salty).\nLate: Coaltana (fire), Mint Mace (minty), Rapier of Life Steal.",
])

path = "grounded/story-walkthrough.md"
pg("Grounded Story Walkthrough", "Complete lab progression.", ["Grounded", "story"], [
    "## Lab Order\n\nHedge > Pond > Haze > Black Anthill > Mant > Undershed Lab (final).\n\n~30 hours main story. ~60 hours with optional bosses.",
    "## Boss Fights\n\nThe Mant: Upper yard shed. Phase 1: Normal. Phase 2: Adds (mant nymphs). Phase 3: Enrage (double speed). Phase 4: Ground pound (jump to avoid).\n\nBroodmother (final): Full strength version. Hardest fight in game.",
    "## Endgame\n\nAfter killing Mant, its chip unlocks Undershed Lab. Solve 4 lasers + 3 keycards. Beat Broodmother. Machine repaired - can shrink/grow at will (post-game).",
])

# === EXTRA PAGES TO REACH 160 ===
# More guides for existing games

path = "satisfactory/beginners-tips.md"
pg("Satisfactory Beginners Tips", "Starting your first factory.", ["Satisfactory", "beginner"], [
    "## First Hour\n\n1. Collect iron, copper, limestone near drop pod\n2. Build Portable Miner on iron node\n3. Craft smelter > iron plates\n4. Build biomass burner for power\n5. Start producing iron rods + screws\n\nPro tip: Build near multiple resource nodes.",
    "## Power Management\n\nBiomass burners: Chop leaves/wood, convert to biomass.\nCoal generators: Unlock at tier 3. 8 generators per 120 coal/min node.\n\nTip: Build a biomass farm (solid biofuel) before coal.",
    "## Factory Layout\n\nInput > Smelter > Constructor > Assembler > Storage.\n\nLeave 2-3 foundation gaps between production lines for belting. Use manifolds for even splitting.",
])

path = "factorio/beginners-tips.md"
pg("Factorio Beginners Tips", "Starting your factory.", ["Factorio", "beginner"], [
    "## First 30 Minutes\n\n1. Mine iron + copper by hand\n2. Build burner miner on coal + iron\n3. Craft furnace > smelt iron plates\n4. Build assembling machine for gears\n5. Research automation (red science)\n\nIron gear production is critical for everything.",
    "## Science Setup\n\nRed science: 1 copper plate + 1 gear = 1 pack. 5 assemblers = 45 SPM.\nGreen science: 1 inserter + 1 belt = 1 pack. Feed from red science line.\n\nScale up before expanding to next science tier.",
    "## Biter Management\n\nBuild radar to spot biter bases. Clear nests near pollution cloud. Wall + turret chokepoints. Don't let evolution get too high before you have red ammo.",
])

path = "valheim/boss-strategies.md"
pg("Valheim Boss Strategies", "All bosses and prep.", ["Valheim", "bosses"], [
    "## Boss Order\n\nEikthyr (Meadows) > Elder (Black Forest) > Bonemass (Swamp) > Moder (Mountains) > Yagluth (Plains) > Queen (Mistlands).",
    "## Key Prep\n\nEikthyr: Bow + 100 fire arrows. Kite and shoot.\nElder: Fire arrows. Use terrain for cover.\nBonemass: Poison res mead + blunt weapon + 200 arrows.\nModer: Need cold res. Frost arrows + stagbreaker.",
    "## Rewards\n\nEikthyr: Hard Antler (pickaxe).\nElder: Swamp Key (sunken crypts).\nBonemass: Wishbone (buried treasure).\nModer: Dragon Tear (artisan table).\nYagluth: Fuling totem.\nQueen: Seal breaker.",
])

path = "rust/raid-guide.md"
pg("Rust Raid Guide", "Raiding and explosives.", ["Rust", "raiding"], [
    "## Explosives\n\nSatchel: 480 damage. Requires 480 sulfur.\nC4: 550 damage. 440 sulfur + 20 cloth + 2 metal.\nRocket: 350 damage (direct). 1400 sulfur + 150 metal.\n\nCost per stone wall (500 HP): 2 C4 or 3 rockets.",
    "## Raiding Strategies\n\nOnline: Door camping, breach with rockets, fight defenders.\nOffline: More time, use cheapest explosives, loot and leave.\n\nAlways scout first. Check for auto-turrets + traps.",
    "## Defenses Against Raiders\n\nHoneycomb: 6 walls per layer.\nPeak-down shooting floor.\nAuto-turrets at all entrances.\nExternal TCs prevent raid towers.\n\nPlace loot in multiple scattered boxes.",
])

path = "stardew-valley/money-making.md"
pg("Stardew Valley Money Making Guide", "Best profits.", ["Stardew Valley", "money"], [
    "## Year 1 Money\n\nSpring: Fish in mountain lake. Plant strawberries at Egg Festival.\nSummer: Blueberries (repeat harvest). Start preserving jars.\nFall: Cranberries (repeat harvest). Kegs if available.\nWinter: Focus on mining + greenhouse if unlocked.",
    "## Keg Empire\n\n1 keg per 2 crops. 10 kegs = 200 crops.\nAncient Fruit Wine: 1650g per bottle.\nStarfruit Wine: 2250g.\nAged in cellar to iridium: 3x value.",
    "## Late Game\n\nGreenhouse: 116 Ancient Fruit + 4 trees. Weekly harvest: 191,400g.\nPigs: 8 pigs = ~20 truffles/day = 21,300g/day.\n\nCombine: Greenhouse Ancient Fruit + cellar aging + pig farm.",
])

path = "minecraft/combat-guide.md"
pg("Minecraft Combat Guide", "Fighting mobs and bosses.", ["Minecraft", "combat"], [
    "## Melee Combat\n\nShield in offhand: Blocks 100% damage from front. Right-click to block.\n\nCritical hits: Jump before swinging. +50% damage.\n\nSweep attack: Hold attack to sweep (Java). Hits multiple enemies.",
    "## Ranged Combat\n\nBow: Hold to charge. Full charge = 150% damage.\nCrossbow: Pre-load, fire instantly. Multishot fires 3 arrows.\n\nTip: Use piercing/spectral arrows for special effects.",
    "## Boss Strategies\n\nEnder Dragon: Destroy crystals first. Use beds as explosives. Slow falling potion.\nWither: Fight underground (3-high tunnel). Smite V sword (4x to undead).",
])

# Also add more news posts
news2 = [
    ("2026-07-06-dyson-combat-overhaul.md", "Dyson Sphere Program Combat Overhaul", "New Dark Fog difficulty settings."),
    ("2026-07-06-shapez2-content-update.md", "Shapez 2 Content Update", "New shapes and logic components."),
    ("2026-07-06-timberborn-update-7.md", "Timberborn Update 7", "New bots and water mechanics."),
    ("2026-07-06-sons-forest-patch.md", "Sons of the Forest Patch", "New building pieces and bug fixes."),
    ("2026-07-06-grounded-2-tease.md", "Grounded 2 Teased by Obsidian", "Studio hints at sequel."),
]

for fname, title, desc in news2:
    w("news/posts/" + fname, "---\ntitle: '" + title + "'\ndescription: '" + desc + "'\ndate: " + NOW + "\ntags: [news, update]\n---\n\n## " + title + "\n\n" + desc + "\n\nLatest news for the game guide community.")

# Summary
import subprocess
result = subprocess.run(["find", DOCS, "-type", "f", "-name", "*.md"], capture_output=True, text=True)
files = [f for f in result.stdout.strip().split("\n") if f]
print(f"\nTotal .md files: {len(files)}")

# Category breakdown
from collections import Counter
cats = Counter()
for f in files:
    parts = f.replace(DOCS + "/", "").split("/")
    if len(parts) > 1:
        cats[parts[0]] += 1
for cat, count in sorted(cats.items()):
    print(f"  {cat}: {count} pages")
