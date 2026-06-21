---
title: "Timberborn Districts & Logistics Guide"
description: "Master Timberborn districts, district crossings, distribution towers, and logistics. Learn how to set up multi-district colonies, manage warehouses, and compare Folktail vs Ironteeth district strategies."
---

# 🏘️ Timberborn Districts & Logistics Guide

As your beaver colony grows beyond the first handful of buildings, you'll hit a hard limit: **your beavers won't walk that far.** Timberborn's districts system lets you split your settlement into manageable zones connected by automated logistics, unlocking truly sprawling mega-colonies.

| Section | What You'll Learn |
|:--------|:------------------|
| [What Are Districts?](#what-are-districts) | The core concept & why they exist |
| [How to Set Up Districts](#how-to-set-up-districts) | Step-by-step setup guide |
| [District Crossings](#district-crossings) | Connecting districts physically |
| [Distribution — Logistics Explained](#distribution-logistics-explained) | How goods move between districts |
| [Warehouse Management](#warehouse-management) | Storage strategies for multi-district colonies |
| [Folktail vs Ironteeth District Strategies](#folktail-vs-ironteeth-district-strategies) | Faction-specific approaches |
| [Common Mistakes](#common-mistakes) | Pitfalls to avoid |

---

## What Are Districts?

A **district** is a self-contained zone in Timberborn with its own workforce, warehouses, and resource pool. Every colony starts with a single **District Centre** — your main hub. When your beavers have to trek across half the map to deliver logs, you know it's time to expand.

### Why Districts Matter

- **Walking distance limits** — Beavers spend most of their day walking. A beaver that walks 30 tiles to a job works half as much as one that walks 10 tiles. Districts keep travel time low.
- **Resource specialisation** — One district farms, another logs, a third manufactures. Goods are shipped automatically via distribution.
- **Population management** — Each district has its own population cap (controlled by housing). You can balance growth across zones.
- **Performance optimisation** — Fewer pathfinding calculations per district means better FPS on large maps.

### How Districts Work

| Concept | Explanation |
|:--------|:------------|
| **District Centre** | The building that defines a district's boundary and population. Every beaver is assigned to one. |
| **Workforce** | Each district has its own pool of beavers. Jobs in that district are filled only by assigned beavers. |
| **Local Storage** | Warehouses, log piles, and tanks are *per-district*. Beavers in District A cannot access District B's storage directly. |
| **Cross-District Transport** | Goods move between districts **only** through the Distribution system (see below). |
| **Unlock** | Build a second District Centre after researching **District Management** (Science, ~100 Science points). |

> 💡 **District Centres are expensive** — 20 Logs, 15 Planks, and 5 Gears. Don't build one until you genuinely need it (typically 30+ beavers or when your builders are walking 40+ tiles to work).

---

## How to Set Up Districts

### Step 1 — When to Expand

Build a second district when:

1. Your beavers are walking **40+ tiles** to reach resources or jobs
2. You've depleted local resources (trees, metal) near your first district
3. You want to claim a distant water source or fertile land
4. Your population exceeds **30–40 beavers** and FPS is dipping

### Step 2 — Choose the Location

Scout for a location that is:

- **Flat land** (or easy to terrace) — you'll build housing, production, and storage here
- **Near a resource** — trees, water, metal, or fertile soil
- **Accessible** — you'll need to connect it to your main district with paths

### Step 3 — Build the District Centre

1. Research **District Management** in the Science tree
2. Craft **1 District Centre** (20 Logs, 15 Planks, 5 Gears)
3. Place it in your chosen location
4. **Beavers will automatically migrate** from your main district to fill jobs in the new one

> ⚠️ **The new district starts empty.** It has zero resources. You must either:
> - Send resources via **Distribution** (see below), or
> - Build a **District Crossing** immediately so haulers can carry goods by hand

### Step 4 — Assign Jobs and Build Housing

Each district needs its own:

| Building | Purpose |
|:---------|:--------|
| **Housing** | Controls population cap |
| **Water Pump** | Local water supply |
| **Farm** | Local food production |
| **Warehouses** | Storage for goods |
| **Production buildings** | Workshops, lumber mills, etc. |

> 🔄 **You can move beavers** between districts by clicking a District Centre and adjusting the "desired population" slider. Beavers will migrate as housing becomes available.

---

## District Crossings

A **District Crossing** is a physical gate that connects two districts. Without it, beavers and haulers cannot cross the border.

### What District Crossings Do

- Allow **haulers** to carry goods between districts (manually, before Distribution Towers are built)
- Let **beavers** pathfind across the boundary to reach job sites (if jobs are available)
- Create a **visible border** — a gate structure you can see on the map

### How to Build

1. Select the **District Crossing** from the Paths menu
2. Place it at the border between two districts. Each end must land in a different district's zone.
3. The crossing automatically connects the two districts

### Important Rules

| Rule | Detail |
|:-----|:-------|
| **Zone boundaries** | District zones are visible as coloured overlays when you select a District Centre. Crossings must span the boundary. |
| **One per border** | You only need one crossing between any two adjacent districts. |
| **Beaver access** | Build paths on both sides so beavers can actually reach the crossing. |
| **Upgrade path** | Later, Distribution Towers replace manual hauling through crossings. |

> 🧭 **Pro tip:** When planning your second district, place the District Centre first, then observe the zone boundary. Build the crossing *exactly* where it makes sense for future path networks. Moving a crossing later is costly.

---

## Distribution — Logistics Explained

Distribution is how goods move *automatically* between districts. This is the heart of Timberborn's logistics system.

### The Distribution Tower

| Stat | Value |
|:----|:------|
| **Cost** | 25 Logs, 20 Planks, 10 Gears |
| **Workers** | 1–2 haulers |
| **Range** | Visible radius when placed (large, covers most of a district) |
| **Recipients** | 1 per Distribution Tower (select target district) |
| **Unlock** | Research **Distribution** (Science tree, after District Management) |

### How It Works

1. **Building A** (District A) has a Distribution Tower
2. You set the tower to send goods to **District B**
3. Haulers in District A pick up goods from local storage and carry them to the tower
4. Goods are transported to District B's **Drop-Off Point** (a small building placed in the target district)
5. Haulers in District B distribute those goods to local warehouses

### Configuring Distribution

Click a Distribution Tower to configure:

| Setting | What It Does |
|:--------|:-------------|
| **Target District** | Which district receives goods |
| **Resource Filters** | What specific goods to send (or "All") |
| **Minimum Stock** | Keep this much in *this* district before exporting. Default is 50 units. |
| **Maximum Desired** | Stop sending when the target district has this much. Default is 200 units. |
| **Priority** | High/Medium/Low — determines which goods haulers move first |

### Example Scenario

```text
District A (Forestry):  ↓ sends logs & planks
                          ↓ via Distribution Tower
District B (Farming):   ↓ receives logs & planks
                          ↓ sends carrots & berries
                          ↓ via Distribution Tower
District A (Forestry):  → receives food
```

> ⚡ **Pro tip:** Each district needs its *own* Distribution Tower to export. District A's tower sends *out*; District B needs its own tower to send *back*. Plan for two towers for bidirectional trade.

### Drop-Off Points

A Drop-Off Point is where inbound goods arrive in a district.

| Stat | Value |
|:----|:------|
| **Cost** | 10 Logs, 5 Planks |
| **Capacity** | 60 units (small buffer) |
| **Workers** | 0 (passive building) |

Place Drop-Off Points near your warehouses so haulers don't have to carry goods far. One well-placed Drop-Off Point can serve multiple warehouses.

---

## Warehouse Management

Warehouses are **per-district** in Timberborn. Goods stored in District A are invisible to District B unless moved by distribution.

### Warehouse Types

| Building | Storage Slots | Cost | Best For |
|:---------|:-------------|:-----|:---------|
| **Small Warehouse** | 3 stacks × 15 units = 45 | 6 Logs | Early game, local storage |
| **Large Warehouse** | 9 stacks × 15 units = 135 | 15 Logs + 8 Planks | Mid-game bulk storage |
| **Log Pile** | 50 logs | 3 Logs | Log-specific storage |
| **Plank Pile** | 50 planks | 5 Logs + 3 Planks | Plank-specific storage |
| **Water Tank** | 750–1500 water | 12 Logs + 6 Planks | Water only |

### Multi-District Storage Strategy

| Strategy | How |
|:---------|:----|
| **Hub-and-Spoke** | Central "capital" district with bulk storage; satellite districts hold only 2–3 days of food/water. Ship overflow to capital. |
| **Edge Buffers** | Place small warehouses near District Crossings/Drop-Off Points. Goods arrive there, then get distributed locally. |
| **Tiered Storage** | Raw materials (logs, planks) stored in the producing district. Finished goods shipped to consuming district. |
| **Water Independence** | Every district should have its own water tank(s) sized for the local population × drought length. Never rely on water distribution. |

> ⚠️ **Critical rule:** Never set Minimum Stock too low on essential goods. If District A sends *all* its logs to District B, District A can't build anything. Always keep a safety buffer — at least 50 units of logs, planks, and food per district.

### Setting Stock Limits

| Parameter | Recommended Value | When to Adjust |
|:----------|:-----------------|:---------------|
| **Minimum Stock** | 50–100 (essentials), 10–20 (luxuries) | Increase if district runs out during normal operation |
| **Maximum Desired** | 100–200 (small districts), 300–500 (large) | Increase if receiving district starves; decrease if distribution is wasteful |

---

## Folktail vs Ironteeth District Strategies

The two factions approach districts very differently thanks to their unique buildings and playstyles.

### 🐾 Folktails — Organic Growth

**Strengths:**
- Cheaper buildings (wood economy)
- Observatories reveal the map early, helping you plan district locations
- Brewery gives +2 happiness, offsetting the morale penalty of new districts
- Wood is renewable and fast-growing

**District Strategy:**

| Phase | Approach |
|:------|:---------|
| **Early (1–30)** | Single district. Focus on water reservoir, basic farms, and lumber. |
| **Mid (30–80)** | Second district focused on **logging + planks**. Ship wood products to main district. Folktails can sustain a 3:1 log district ratio (3 log districts : 1 everything else). |
| **Late (80+)** | Specialised districts: Farming, Forestry, Manufacturing, Residential (with Brewery). Folktails scale beautifully because wood is cheap and renewable. |

**Tips:**
- Use **Observatories** to scout district locations before placing District Centres
- Folktail housing (Lodges) is compact — good for dense residential districts
- Keep a **Brewery district** centralised; ship beer everywhere for the happiness bonus
- Folktails' **Engine** (wood-fired power) means you want a dedicated wood district feeding power stations

### ⚙️ Ironteeth — Industrial Efficiency

**Strengths:**
- **Mines** provide infinite metal — enables metal-intensive district infrastructure
- **Factories** mass-produce goods, making centralised manufacturing viable
- **Excavators** level terrain for perfect district layouts
- Better power generation (steam engines, iron power wheels)

**District Strategy:**

| Phase | Approach |
|:------|:---------|
| **Early (1–25)** | Single district. Rush to metal recycling and small windmills. |
| **Mid (25–60)** | Second district near a **metal node** (for Mine). Ship metal plates and gears to main district. Factories make this incredibly efficient. |
| **Late (60+)** | Full factory system: Raw materials district → Processing district → Manufacturing district → Residential district. A linear chain works better than hub-and-spoke for Ironteeth. |

**Tips:**
- Ironteeth excel at **linear production chains**. Place districts in a line: Raw → Process → Manufacture → Consume.
- Use **Mechanical Water Pumps** to supply inland districts that aren't on rivers
- Ironteeth housing (Apartments) is tall — stack vertically to minimise district footprint
- **Drop-Off Points** are critical for Ironteeth because their production chains are longer (more intermediate goods)

### Faction Comparison Table

| Aspect | 🐾 Folktails | ⚙️ Ironteeth |
|:-------|:-------------|:-------------|
| **Best District Layout** | Hub-and-spoke (central capital + satellites) | Linear chain (raw → process → manufacture) |
| **Number of Districts** | 3–5 (spread out, natural) | 4–7 (compact, industrial) |
| **Key Export Good** | Logs, planks, beer | Metal plates, gears, processed goods |
| **Best District Type** | Forestry, farming | Mining, manufacturing |
| **Logistics Bottleneck** | Wood supply (requires large forested area) | Metal distribution (heavy goods, slow haulers) |
| **Power Per District** | Independent (water wheels, windmills) | Centralised (steam engines need fuel shipment) |
| **Morale Management** | Brewery (+2 happiness) | Apartments (efficient space, but no happiness bonus) |
| **Expansion Difficulty** | Easy — wood is everywhere | Moderate — need metal node or scrap |

---

## Common Mistakes

### ❌ Building a Second District Too Early

A second district before you have:
- Stable food supply for 30+ beavers
- At least 200 stored water
- District Management researched

...will starve your new district and cripple your main one. The new District Centre costs precious planks and gears. Don't build it until you have surplus.

### ❌ Forgetting Drop-Off Points

A Distribution Tower sends goods, but they arrive at a **Drop-Off Point**. If you forget to build one in the target district, the goods have nowhere to go and the haulers just stand around.

**Fix:** Always place a Drop-Off Point immediately after building a new District Centre.

### ❌ Not Setting Minimum Stock

Default Minimum Stock is **50**. That sounds safe, but if you have only 60 logs, your main district sends 10 away and then can't build a new water pump during a drought.

**Fix:** Raise Minimum Stock on essentials to 100–150 for your primary district. Leave defaults for dedicated production districts.

### ❌ One-Way Distribution

You send logs to the farm district, but the farm district has no Distribution Tower to send food back. Your main district slowly starves while the farm district rots in surplus.

**Fix:** Every district that *receives* should also *send* something back (or be self-sufficient in food/water).

### ❌ Ignoring Path Quality

Haulers use paths. Bad paths (dirt, long distances, steep inclines) slow distribution to a crawl.

**Fix:** Pave main distribution routes with **boards** or **metal paths** (late-game). Build stairs or elevators for vertical connections.

### ❌ Overpopulating a New District

When you build a District Centre, beavers migrate automatically. If the new district has too much housing and too few jobs, you get unemployed beavers consuming food and water for nothing.

**Fix:** Set the desired population slider low (5–8 beavers) initially. Increase it only after jobs and housing are ready.

### ❌ Not Planning for Water Independence

Every district needs water. If your farming district is 100 tiles from the river and you rely on water distribution, one broken Distribution Tower chain means colony collapse.

**Fix:** Each district gets its own water pump(s) and tank(s). Calculate: `Population × Drought Days × 1.5 (safety margin)`. Build that much tank capacity locally.

### ❌ Tight Warehouse Placement

Placing warehouses in a cluster looks neat but creates traffic jams. Haulers block each other trying to access adjacent warehouses.

**Fix:** Leave 1-tile gaps between warehouses. Place Drop-Off Points at the edge of the warehouse cluster, not in the middle.

---

## Summary Checklist

| # | Task | Done? |
|:--|:-----|:------|
| 1 | Research **District Management** before building a second centre | ☐ |
| 2 | Scout location with flat land + nearby resources | ☐ |
| 3 | Build District Centre + local housing immediately | ☐ |
| 4 | Build a **District Crossing** at the border | ☐ |
| 5 | Place **Drop-Off Point** in the new district | ☐ |
| 6 | Build **Distribution Tower** in your main district | ☐ |
| 7 | Set Minimum Stock (100+) on essentials | ☐ |
| 8 | Give the new district its own **water supply** | ☐ |
| 9 | Give the new district its own **food supply** | ☐ |
| 10 | Add Distribution Tower in the new district to send goods back | ☐ |

---

## 🔗 Useful Links

| Resource | Link |
|:---------|:-----|
| Official Timberborn Wiki | [timberborn.fandom.com](https://timberborn.fandom.com) |
| Mechanistry (Developer) | [mechanistry.com](https://mechanistry.com) |
| Timberborn Subreddit | [reddit.com/r/Timberborn](https://reddit.com/r/Timberborn) |
| Steam Community Hub | [steamcommunity.com/app/1062090](https://steamcommunity.com/app/1062090) |

---

> 🛒 [**Buy Timberborn on Steam**](https://store.steampowered.com/app/1062090/?utm_source=game-guide&utm_medium=affiliate&utm_campaign=timberborn-districts) — Overwhelmingly Positive (95%+ rating), constantly updated by Mechanistry.
>
> *Guide data verified against Timberborn 1.0 (March 2026 release). Faction-specific mechanics noted where applicable.*
