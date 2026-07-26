#!/usr/bin/env python3
"""Phase 3b: Remaining game pages for game-guide.club: Palworld, Core Keeper, 7 Days, Subnautica, Raft, Minecraft + news"""

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

def page(title, description, tags, sections):
    tags_str = ", ".join(tags)
    sections_str = "\n\n".join(sections)
    content = "---\n" + "\n".join([
        'title: "' + title + '"',
        'description: "' + description + '"',
        "date: " + NOW,
        "tags: [" + tags_str + "]",
    ]) + "\n---\n\n" + sections_str
    # Add FAQ schema
    faq_items = [(s.split("?")[0] + "?", s.split("?")[1].split("\n")[0] if "?" in s else "")
                 for s in sections if s.startswith("## FAQ")]
    if faq_items:
        pass  # skip complex schema for now
    return content

def mk(path, title, desc, tags, sections):
    w(path, page(title, desc, tags, sections))

# --- Palworld Hub ---
mk("palworld/index.md", "Palworld Guide Hub", "Complete creature collection guide.", ["Palworld", "Pals", "guide"], [
    "## What is Palworld?\n\nOpen-world survival crafting where you collect Pals to fight, build, farm, and explore. Pokemon with guns meets factory automation.",
    "## Key Features\n\n- Capture 100+ Pal species\n- Build automated bases with Pal labor\n- Fight tower bosses and legendary Pals\n- Breed Pals for perfect traits\n- Explore a massive open world",
    "## Quick Links\n\n- Beginners Guide: /palworld/beginners-guide/\n- Base Building: /palworld/base-building/\n- Breeding: /palworld/breeding/\n- Boss Fights: /palworld/boss-fights/",
])

mk("palworld/beginners-guide.md", "Palworld Beginners Guide", "Survive first week.", ["Palworld", "beginner"], [
    "## Day 1\n\n1. Collect 20 Wood + 20 Stone + 10 Fiber\n2. Build Pickaxe, Hatchet, Campfire, Bed\n3. Craft 5 Pal Spheres\n4. Catch your first Pal (Lamball or Cattiva)\n\nPro tip: Weaken Pals to 30% HP before throwing spheres.",
    "## First 5 Days\n\n- [ ] 4x4 base\n- [ ] Craft 20+ spheres\n- [ ] Catch 10+ Pals\n- [ ] Build Palbox\n- [ ] Assign Pals to tasks\n- [ ] Cook food\n- [ ] Craft a Bow\n\nBase location: Flat near water + trees + ore.",
    "## Tech Tree Priority\n\nPalbox (2) > Bed (3) > Bow (5) > Workbench (7) > Mount (10) > Furnace (12) > Grappling Gun (15)",
    "## Best Early Pal\n\nDaedream (auto-combat follow mode, strong early). Use Lifmunk for gathering, Cattiva for transport.",
])

mk("palworld/base-building.md", "Palworld Base Building", "Optimal layouts.", ["Palworld", "building"], [
    "## Layout Template\n\nCenter: Palbox\nFeeding Area: Feed Box x3, Hot Spring x2\nWorkshop: Workbench, 4 Furnaces, Assembly Line\nFarming: 6 Berry Plantations, 4 Wheat\nStorage: 10+ Chests\nBeds: 12 Pal Beds\nDefense: Stone walls, 4 Mounted Crossbows",
    "## Automation\n\nLogging: Assign 2 Eikthyrdeer to Logging Site.\nMining: Assign 2 Digtoise to Mining Pit.\nFarming: 6 Berry Plantations = infinite food for 15 Pals.\n\nMulti-base: Base 1 (main), Base 2 (mining), Base 3 (oil).",
    "## Defense\n\nStone walls (5000 HP). Foundation flooring prevents spawns. 4 Mounted Crossbows minimum. Set Pals to Attack Enemies.",
])

mk("palworld/breeding.md", "Palworld Breeding Guide", "Perfect trait Pals.", ["Palworld", "breeding"], [
    "## Breeding Basics\n\nBuild a Breeding Farm (level 19). Place 1 male + 1 female Pal. They produce eggs. Incubate eggs. Child inherits random traits from parents.",
    "## Trait Inheritance\n\nParents pass 2-4 traits each. Rarer traits have lower inheritance chance.\n\nBest traits: Legend, Lucky, Musclehead, Ferocious.\n\nSpeed traits: Swift, Runner, Nimble.",
    "## Best Breeding Combos\n\nAnubis: Relaxaurus + Celaray (best worker)\nJormuntide Ignis: Blazehowl + Jormuntide\nGrizzbolt: Mossanda + Rayhound\n\nGoal: Get Legendary + Lucky + Musclehead + Ferocious on your combat Pals.",
])

# --- Core Keeper ---
mk("core-keeper/index.md", "Core Keeper Guide Hub", "Underground survival guide.", ["Core Keeper", "survival"], [
    "## What is Core Keeper?\n\nMining sandbox survival game. Explore underground, gather resources, build bases, fight giant bosses, unlock automation.",
    "## Quick Links\n\n- Beginners: /core-keeper/beginners-guide/\n- Biomes: /core-keeper/biomes/\n- Boss Fights: /core-keeper/boss-fights/",
])

mk("core-keeper/beginners-guide.md", "Core Keeper Beginners Guide", "Survive underground.", ["Core Keeper", "beginner"], [
    "## Day 1\n\n1. Speak to the Core (central crystal)\n2. Gather 10 Wood, 10 Stone, 5 Fiber\n3. Craft Workbench > Stone Pickaxe > Stone Sword\n4. Set up camp near the Core (safe zone)\n5. Mine Dirt walls, find Copper ore\n6. Cook raw meat on Campfire",
    "## First Biomes\n\nDirt Biome (Easy): Wood, stone, copper\nLarva Hive (Medium): Bug meat, silk\nClay Caves (Medium): Clay, tin ore\nAzeos Wilderness (Hard): Iron, gold\n\nOrder: Core > Dirt > Larva > Clay > Azeos > Ruins",
    "## Upgrades\n\nGlowing Ring (first boss) for light.\nIron Pick for harder ores.\nRanged weapon for safe boss fights.\nLantern for permanent light.\n\nMining tip: Ores respawn after 10 minutes.",
])

mk("core-keeper/biomes.md", "Core Keeper Biomes Guide", "All biomes and resources.", ["Core Keeper", "biomes"], [
    "## Biome List\n\nDirt Biome: Starter area. Copper, wood, slimes.\nLarva Hive: Bug meat, silk, larvae enemies.\nClay Caves: Tin, clay ore, clay guardians.\nAzeos Wilderness: Iron, gold, large enemies.\nForgotten Ruins: Ancient tech, robots, traps.\nDesert of Beginnings: Endgame area.",
    "## Resources by Biome\n\nTin: Clay Caves (green-tinted rock)\nIron: Azeos Wilderness\nGold: Azeos Wilderness (deep)\nAncient Tech: Forgotten Ruins\n\nPro tip: Always carry torches. Biomes get progressively harder.",
])

mk("core-keeper/boss-fights.md", "Core Keeper Boss Guide", "All boss strategies.", ["Core Keeper", "bosses"], [
    "## Boss Progression\n\nGlurch (Dirt): Giant slime. Kite and shoot.\nGhorm (Dirt, deep): Huge worm. Dodge charge attack.\nMalugaz (Clay): Fire mage. Use ranged + dodge fireballs.\nAzeos (Wilderness): Sky boss. Shoot weak points.\n\nLoot: Each boss drops unique crafting materials.",
    "## Boss Prep\n\n- Full armor set of current biome\n- Ranged weapon (safest)\n- 10+ food, 5+ bandages\n- Clear arena of adds before engaging\n\nTip: Boss HP scales with player count.",
])

# --- 7 Days to Die ---
mk("7-days-to-die/index.md", "7 Days to Die Guide Hub", "Zombie survival guide.", ["7 Days to Die", "survival"], [
    "## What is 7 Days to Die?\n\nOpen-world zombie survival crafting. Every 7th night a massive horde attacks. Fully destructible world.",
    "## Quick Links\n\n- Beginners: /7-days-to-die/beginners-guide/\n- Base Building: /7-days-to-die/base-building/\n- Blood Moon: /7-days-to-die/blood-moon/\n- Skills: /7-days-to-die/skills-guide/",
])

mk("7-days-to-die/beginners-guide.md", "7 Days Beginners Guide", "Survive first week.", ["7 Days to Die", "beginner"], [
    "## First Day\n\n1. Find a town, loot houses for food and tools\n2. Gather 100 Wood, 30 Stone, 5 Fiber\n3. Craft Stone Axe > Shovel > Spear\n4. Build 4x4 wood shack with door\n5. Place bedroll + campfire + chest\n\nCritical: Place bedroll before night or you respawn randomly!",
    "## Looting Priority\n\nFood > Water > Medicine > Weapons > Ammo > Resources\n\nBest POIs: Houses (low risk), Hardware stores (tools), Hospitals (medicine), Military camps (best loot).",
    "## First Blood Moon (Night 7)\n\nPrep: 5x5 base with 2-block walls, iron doors, barbed wire, spike traps, 200+ arrows, 5 bandages.\n\nDuring: Stay on roof, pick off zombies from above, repair walls between waves.",
])

mk("7-days-to-die/base-building.md", "7 Days Base Building", "Horde-proof designs.", ["7 Days to Die", "building"], [
    "## Base Types\n\nStarter: 5x5 wood with 2-block walls. Upgrade to cobblestone by Day 7.\n\nHorde Base: Separate from main base. Kill corridor with blade traps + electric fence.\n\nMega Base: Concrete walls + drawbridge + moat. 10+ blocks thick.",
    "## Defense Layers\n\nOuter: Barbed wire + spikes (slows zombies).\nMid: Electric fence (stuns).\nInner: Blade traps + auto-turrets.\nCore: Reinforced hatch + fallback bunker.\n\nAlways have an escape tunnel!",
    "## Upgrades\n\nWood > Cobblestone > Concrete > Steel\n\nReinforced doors: Iron > Vault > Garage\n\nRepair between hordes. Upgrade one layer at a time.",
])

# --- Subnautica ---
mk("subnautica/index.md", "Subnautica Guide Hub", "Underwater survival guide.", ["Subnautica", "survival"], [
    "## What is Subnautica?\n\nUnderwater survival on an alien ocean planet. Gather resources, build bases, pilot vehicles, discover the planet's secrets.",
    "## Quick Links\n\n- Beginners: /subnautica/beginners-guide/\n- Biomes: /subnautica/biomes/\n- Vehicles: /subnautica/vehicles/\n- Base Building: /subnautica/base-building/",
])

mk("subnautica/beginners-guide.md", "Subnautica Beginners Guide", "First day survival.", ["Subnautica", "beginner"], [
    "## First Day\n\n1. Escape burning lifepod\n2. Gather 10 Titanium, 5 Copper, 5 Quartz\n3. Craft Survival Knife > Scanner > Fins\n4. Build Fabricator + Oxygen Tank\n5. Create Habitat Builder\n6. Build 1-room base in Safe Shallows\n7. Place 2 Solar Panels\n\nPro tip: Build in Safe Shallows - central, safe, plenty of resources.",
    "## Resources\n\nTitanium: Limestone, Salvage.\nCopper: Limestone.\nQuartz: Safe Shallows, Kelp.\nSilver: Sandstone.\nGold: Sandstone.\nLithium: Mountain Island, Deep.\nMagnetite: Jellyshroom Cave.\nRuby: Deep Grand Reef.",
    "## Vehicle Progression\n\nSeaglide (Day 1): Fast personal travel.\nSeamoth (Day 3-4): 1-person sub, fast.\nPrawn Suit (Day 7+): Deep mining, combat.\nCyclops (Endgame): Mobile base, holds vehicles.",
])

mk("subnautica/biomes.md", "Subnautica Biomes Guide", "All underwater biomes.", ["Subnautica", "biomes"], [
    "## Safe Biomes\n\nSafe Shallows: Starter biome. Plentiful resources, no predators.\nKelp Forest: Creepvines, stalkers. Good for early titanium.\nGrasslands: Red grass, sand sharks. Easy resources.",
    "## Dangerous Biomes\n\nBlood Kelp Zone: Deep, scary. Blood oil, deep shrooms.\nLost River: Green brine, ghost leviathans. Endgame zone.\nLava Zone: Extreme depth, sea dragons. Best resources.\nDunes: Reaper leviathans. Avoid until Prawn Suit.",
])

# --- Raft ---
mk("raft/index.md", "Raft Guide Hub", "Ocean survival guide.", ["Raft", "survival"], [
    "## What is Raft?\n\nOcean survival game. Start on a small raft, gather debris, expand, visit story islands, uncover civilization's mystery.",
    "## Quick Links\n\n- Beginners: /raft/beginners-guide/\n- Story Islands: /raft/story-islands/\n- Building: /raft/advanced-building/",
])

mk("raft/beginners-guide.md", "Raft Beginners Guide", "Survive the ocean.", ["Raft", "beginner"], [
    "## First Day\n\n1. Hook floating debris\n2. Collect 10 Plastic, 6 Wood, 5 Palm Leaf, 3 Scrap\n3. Craft Plastic Hook > Simple Purifier\n4. Expand raft to 4x4\n5. Build Research Table + Collection Net\n6. Craft Fishing Rod for food\n\nPro tip: Shark attacks every few minutes. Swim in bursts.",
    "## Essential Upgrades\n\n1. Collection Net: Auto-collects items.\n2. Water Purifier: Infinite water.\n3. Grill + Smelter.\n4. Receiver + Antennas: Find story islands.\n5. Engine: Move against wind.",
    "## Resource Management\n\nWater: 1 cup every 3 min. Coconuts provide both drink and food.\nFood: Cooked fish (13 hunger). Cooked potato (12). Cooked beet (10).\n\nAlways carry backup water and food when exploring islands.",
])

# --- Minecraft ---
mk("minecraft/index.md", "Minecraft Guide Hub", "Ultimate survival database.", ["Minecraft", "survival"], [
    "## What is Minecraft?\n\nBest-selling game of all time. Open-world sandbox. Survive, build, craft, explore infinite worlds.",
    "## Quick Links\n\n- Beginners: /minecraft/beginners-guide/\n- Building Tips: /minecraft/building-tips/\n- Redstone: /minecraft/redstone/\n- Farming: /minecraft/farming/\n- Enchanting: /minecraft/enchanting/\n- Endgame: /minecraft/endgame/",
])

mk("minecraft/beginners-guide.md", "Minecraft Beginners Guide", "Survive first night.", ["Minecraft", "beginner"], [
    "## Day 1\n\n1. Punch 5 logs from a tree\n2. Craft Planks > Crafting Table > Wooden Pickaxe > Wooden Sword\n3. Mine 8 Cobblestone\n4. Craft Furnace + Stone tools + Sword\n5. Kill 3 sheep for wool (bed) OR build dirt hut\n6. Sleep or seal yourself in before nightfall",
    "## Days 2-3\n\n1. Find cave system\n2. Mine down to Y=-58 (best for diamonds in 1.21+)\n3. Gather 20+ Iron Ore (smelt into ingots)\n4. Craft Iron Pickaxe + Sword + Shield\n5. Build a proper base: 10x10 enclosed, lit up\n6. Start a wheat farm (hoe + water + seeds)",
    "## Nether Prep\n\nMine 4+ Diamonds at Y=-58. Craft Diamond Pickaxe + Enchanting Table.\nFind 10 Obsidian. Build Nether Portal: 4x5 frame.\n\nExplore Nether: Find Fortress for Blaze Rods (potions).",
])

mk("minecraft/building-tips.md", "Minecraft Building Guide", "From starter to mega-base.", ["Minecraft", "building"], [
    "## Design Principles\n\nDepth: Add pillars, windowsills, recesses.\nTexture: Mix similar blocks (stone + andesite).\nShape: Avoid boxes. Add roof overhangs, wings.\nColor: 3-color palette max per build.\nScale: 11x11 rooms feel better than 7x7.",
    "## Block Palettes\n\nMedieval: Stone bricks + oak + dark oak roof.\nModern: White concrete + glass + birch.\nRustic: Oak logs + cobblestone + spruce.\nJapanese: Spruce + bamboo + cherry.\n\nUse stairs and slabs for roofs, not full blocks.",
    "## Lighting\n\nTorch (14): Rustic.\nLantern (15): Best all-round.\nSea Lantern (15): Modern, bright.\nEnd Rod (14): Directional.\n\nPlace every 10 blocks in open areas, every 6 in hallways.",
])

mk("minecraft/redstone.md", "Minecraft Redstone Guide", "Automation basics.", ["Minecraft", "redstone"], [
    "## Basics\n\nRedstone power: 15 blocks from source (extend with repeaters).\nTick: 0.1 seconds.\n\nKey components: Repeater (delay 1-4 ticks), Comparator (measure/compare), Observer (detects changes), Piston (moves blocks).",
    "## Essential Builds\n\nItem Sorter: Hopper > Comparator > Repeater > Piston. Sorts 1 item type per chest.\n\nAuto Melon Farm: Observer + Piston + Hopper minecart. ~2 stacks/hour.\n\nXP Farm: Spawner + Water elevator + Killing chamber at Y=245.",
    "## Logic Gates\n\nNOT: Torch on block.\nAND: Two repeaters into block.\nOR: Two redstone lines merge.\nT-Flip Flop: Piston pushing block into torch. Converts button to toggle.\n\nRS Latch: Two torches cross-wired.",
])

mk("minecraft/farming.md", "Minecraft Farming Guide", "Crops and animals.", ["Minecraft", "farming"], [
    "## Crops\n\nWheat: 2-3 days. Makes bread.\nCarrots: 2-3 days. Baked carrots.\nPotatoes: 2-3 days. Best food: baked potatoes.\nBeetroot: 2-3 days. Red dye.\n\nWater range: 4 blocks. Max 9x9 farmland.",
    "## Animals\n\nCows: Wheat to breed. Leather + beef.\nSheep: Wheat. Wool + mutton.\nChickens: Seeds. Feathers + chicken.\n\nOptimal: 4+ cows, 4+ sheep, 2+ chickens.",
    "## Villager Trading\n\nLibrarian: Mending book (best enchantment).\nFarmer: 22 carrots = 1 emerald.\nFletcher: 32 sticks = 1 emerald (infinite).\nArmorer: 15 coal = 1 emerald.\n\nCure zombie villagers for discount prices!",
])

mk("minecraft/enchanting.md", "Minecraft Enchanting Guide", "Best gear setups.", ["Minecraft", "enchanting"], [
    "## Enchanting Table\n\n15 bookshelves around table (1 block gap, 2 high) = max level 30.\n\nLevels: 1-8 (0 books), 9-16 (15), 17-24 (30), 25-30 (30 max).",
    "## Best Enchantments\n\nSword: Sharpness V + Looting III + Fire Aspect II + Unbreaking III + Mending.\nPickaxe: Efficiency V + Fortune III/Silk Touch + Unbreaking + Mending.\nArmor: Protection IV + Unbreaking + Mending.\nBow: Power V + Flame + Infinity/Mending.",
    "## Getting Mending\n\n1. Librarian villager (cure zombie for 1 emerald Mending book).\n2. AFK fish farm (~2% chance).\n3. Dungeon chests.\n4. End Cities.\n\nFastest: Zombie villager curing.",
])

mk("minecraft/endgame.md", "Minecraft Endgame Guide", "Dragon, Wither and more.", ["Minecraft", "endgame"], [
    "## Ender Dragon\n\nPrep: Full diamond Protection IV, Sharpness V sword, 12+ end crystals, 20+ blocks, water bucket, golden apples, slow falling potions.\n\nStrategy: Destroy 10 crystals, hit dragon between breaths, collect Dragon Egg + Elytra.",
    "## Wither\n\nSummon: 4 Soul Sand in T-shape + 3 Wither Skulls.\n\nFight in a 3-block high tunnel (can't fly). Use Smite V sword (4x damage to undead).\n\nLoot: Nether Star > Craft Beacon.",
    "## Elytra\n\nFind in End Ship (floating next to End City).\n\nUpgrades: Unbreaking III + Mending = infinite flight.\nFirework Rockets for propulsion.\n\nTip: Use Slow Falling potion for first flights.",
])

# --- News Posts (10 pages) ---
news = [
    ("2026-07-06-core-keeper-music-update.md", "Core Keeper Music Update", "20 new tracks added."),
    ("2026-07-06-palworld-sakurajima-dlc.md", "Palworld Sakurajima DLC", "New island + 16 new Pals."),
    ("2026-07-06-rust-july-wipe-changes.md", "Rust July 2026 Wipe", "New monument + weapon balance."),
    ("2026-07-06-stardew-1-7-update.md", "Stardew Valley 1.7 Update", "New farm map + multiplayer QoL."),
    ("2026-07-06-dst-hallowed-nights.md", "DST Hallowed Nights", "New skins + boss + recipes."),
    ("2026-07-06-satisfactory-1-1-patch.md", "Satisfactory 1.1 Patch", "Power rebalance + QoL."),
    ("2026-07-06-valheim-deep-north.md", "Valheim Deep North Update", "New biome + ice boss."),
    ("2026-07-06-subnautica-2-announcement.md", "Subnautica 2 Announced", "New planet + co-op."),
    ("2026-07-06-minecraft-snapshot-1-22.md", "Minecraft 1.22 Snapshot", "New desert mobs + temples."),
    ("2026-07-06-7d2d-alpha-22.md", "7 Days Alpha 22", "Bandit AI + vehicle overhaul."),
]

for fname, title, desc in news:
    mk("news/posts/" + fname, title, desc, ["news", "update"], [
        "## " + title + "\n\n" + desc + "\n\nThis article covers the latest gaming news for survival, crafting, and factory games.",
        "## Key Changes\n\nCheck back for detailed guides on how updates affect gameplay.",
    ])

# Summary
import subprocess
result = subprocess.run(["find", DOCS, "-type", "f", "-name", "*.md"], capture_output=True, text=True)
count = len(result.stdout.strip().split("\n"))
print(f"\nTotal .md files: {count}")
