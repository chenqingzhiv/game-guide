---
title: Factorio Advanced Strategies & Megabase Guide
description: Master Factorio's endgame with advanced base designs — Main Bus, City Blocks, Train Grid Megabases, beacon setups, UPS optimization, and SPM scaling from 100 to 10K.
---

# 🏭 Factorio Advanced Strategies & Megabase Guide

Once you've launched your first rocket, the real Factorio begins. Scaling from a starter base to a 1K+ SPM megabase requires entirely new design philosophies. This guide covers the core strategies used by veteran engineers, from mid-game expansion through 10K SPM mega-factories.

---

## 1. Base Design Philosophies

Every Factorio base falls into one of three architectural styles. Each has strengths and weaknesses that matter more as you scale.

### 🛣️ Main Bus

The **Main Bus** is the default "golden path" for getting to your first rocket and beyond. Key materials (iron plates, copper plates, steel, circuits, plastic) run in parallel belts through the factory, with production branches pulling off one side.

| Pros | Cons |
|------|------|
| Simple to plan and expand | Belt throughput caps around 3-4 lanes per material |
| Easy to troubleshoot | Long bus lines create latency and UPS cost |
| Works great for 30-60 SPM | Scales poorly past ~150 SPM due to belt saturation |
| Well-documented blueprints everywhere | Becomes unwieldy beyond 8-12 lanes wide |

**Best for:** Mid-game (first rocket, 30-90 SPM). Can stretch to 150-200 SPM with dedicated smelting arrays per bus section and 4-lane belts of iron/copper.

**Key tip:** Keep the bus one-sided — pull materials from only one side so you can always add more lanes on the other.

### 🧩 City Block / Grid Base

A **City Block** base divides the map into a square grid (typically 100×100, 7×7 chunks, or 124×124 tiles fitting a roboport grid). Each block is a self-contained production module with standardized train stations.

| Pros | Cons |
|------|------|
| Extremely scalable — add blocks to increase throughput | High rail infrastructure cost early on |
| Blueprintable — place, paste, wire | Requires circuit network for demanding LTN/Cybersyn setups |
| Easy to isolate and debug individual blocks | Empty blocks waste space until filled |
| UPS-friendly with direct insertion inside blocks | More complex than a bus for new players |

**Best for:** 500-5K SPM. The dominant megabase architecture for good reason.

**Key tip:** Standardize block size around your roboport coverage. A 7×7 chunk block (112×112 tiles) aligns perfectly with roboport logistics ranges and creates nice 2-chunk-wide rail corridors between blocks.

### 🍝 Spaghetti

Embrace the chaos. **Spaghetti** is any base without a formal layout — belts weave around assemblers, underground belts cross everywhere, and everything is stuffed into the smallest possible footprint.

| Pros | Cons |
|------|------|
| Maximum density per tile | Nightmare to expand or debug |
| Fun and creative challenge | Impossible to scale past 30-60 SPM |
| Minimal wasted belts/pipes | Adding new production often requires tearing down old builds |
| Teaches you belt mechanics intimately | UPS disaster at any real scale |

**Best for:** Early game, challenge runs, speedruns. Avoid for serious megabases.

**Key tip:** If you're spaghetti-ing intentionally, use lots of underground belts to weave through tight spaces. If you're spaghetti-ing because you're lost, it's time to build a bus.

---

## 2. Train Grid Megabase (3-8 Train System)

Once you pass ~200 SPM, trains become mandatory. A properly designed rail grid is the backbone of any megabase.

### Train Length Philosophy

The Factorio community standardizes on **1-4 trains** (1 locomotive, 4 cargo wagons) for general use, but megabases scale to larger sizes:

| Train Config | Best For | Throughput | Notes |
|-------------|----------|-----------|-------|
| 1-2 | Early outposts, fluid wagons | Low | Easy to build, low throughput |
| 1-4 | Standard megabase workhorse | Medium | Best balance of acceleration and cargo |
| 2-4 | High-throughput ore/plate routes | High | Two locos keep acceleration reasonable |
| 3-8 | Endgame megabases (2K+ SPM) | Very High | Needs long stackers and big stations |

**3-8 trains** (3 locomotives, 8 cargo wagons) are the sweet spot for very large bases. They carry twice the cargo of 1-4 trains with only ~30% more rail infrastructure cost. The three locomotives provide enough acceleration that the long train doesn't crawl.

### Rail Grid Design

A good rail system uses a **grid-aligned track network** with:

- **Two-way tracks** (one per direction) with a rail signal every train-length
- **Chain signals** at every intersection entrance and inside the intersection
- **Roundabouts** for 90° turns at grid intersections
- **Stackers** at every station (capacity = number of trains serving that station × 2)

Standard rail spacing: **6 tiles between parallel rails** (center-to-center) to accommodate train width and signals.

### Station Design Principles

- **Loading stations:** Use 12 stack inserters per wagon (6 per side) with max belt compression
- **Unloading stations:** 12 stack inserters into steel chests → belts → provider chests
- **Balanced unloading:** Wire all 12 chests per wagon to a decider combinator set to "Read contents → Output that" and enable inserters only when chest contents < (max/ number of inserters). This ensures even draw-down across all chests.

### Intersection Throughput

The most common megabase killer is intersection deadlock. Best practices:

- Use **buffered intersections** (rail signals create short "buffer" segments between crossings)
- Prefer **4-way roundabouts** over cross intersections
- For 5K+ SPM, consider **fully grade-separated intersections** (no crossing paths) — search "Factorio Celtic Knot intersection"
- Never place a station immediately after an intersection — leave at least one train-length of clearance

---

## 3. Modules and Beacons

Modules are not optional for megabases. You will use **Productivity Module 3** in everything that can take them, and **Speed Module 3** in beacons surrounding those buildings.

### The 8-Beacon vs 12-Beacon Decision

Beacons affect up to N buildings around them. The standard layouts:

**8-Beacon Design:**

```
B . B . B
. A . A .
B . B . B
. A . A .
B . B . B
```

- 8 beacons per assembler (B = beacon, A = assembler)
- 8 beacons fits neatly in a tileable column
- Each beacon provides 2 speed modules → assembler receives +400% speed (8 × 50%)
- **Pros:** Simpler belt/bot logistics, easier to build, fewer beacons needed overall
- **Cons:** Less speed boost per assembler

**12-Beacon Design:**

```
B . B . B
. A . A .
B . B . B
. A . A .
```

Wait — this also shows 8. For 12-beacon, each row of beacons surrounds assemblers on both sides:

```
B B . B B
. . A . .
B B . B B
. . A . .
B B . B B
```

- Each assembler is adjacent to 12 beacons
- +600% speed from beacons (12 × 50%)
- Requires more careful layout, but **fewer total assemblers** for the same output
- **Pros:** Fewer entities = lower UPS cost, less space used
- **Cons:** Harder to belt, needs more beacons per assembler, more power draw

**Verdict:** Use **12-beacon** for high-volume intermediates (green circuits, iron/copper plates, plastic) where UPS matters. Use **8-beacon** for low-throughput items or when you're tight on beacon footprint.

### Module Progression

| Stage | What to Module | Modules |
|-------|---------------|---------|
| Early (pre-rocket) | Labs, rocket silo | Prod 1 / Speed 1 |
| Mid (post-rocket) | Circuit assemblers, oil refineries | Prod 2 / Speed 2 |
| Late (megabase) | Every production machine | Prod 3 / Speed 3 |
| Endgame | Mining drills | Prod 3 only (no beacon) |
| Endgame | Electric furnaces | Speed 3 in beacons, Prod 3 in furnace |

### Power Cost Reality Check

A single 12-beacon assembler with Prod 3 modules draws approximately **2.5 MW** (beacons included). A 1K SPM base consumes roughly **4-6 GW**. Plan your nuclear (or solar) accordingly.

---

## 4. UPS Optimization

UPS (Updates Per Second) is the invisible wall preventing infinite factory growth. At 60 UPS, the game simulates your factory smoothly. At 30 UPS, everything runs at half speed. Here's how to keep UPS high.

### The UPS Killers (Ranked)

1. **Inserters** (especially when picking items off belts)
2. **Belts** (every belt segment is tracked; thousands of items on belts cost UPS)
3. **Pipes and Fluid mixing** (the fluid system is O(n²) in pipes)
4. **Robots** (every logistics request is a pathfinding job)
5. **Biters** (pathfinding, pollution, expansion logic)

### UPS-Saving Strategies

**1. Go bot-based for low-volume items**
   - Bots excel when throughput per chest is low (e.g., red circuits, modules, science packs)
   - Use bots for the last 20-30 tiles of delivery; belts for long-haul transport

**2. Direct insertion wherever possible**
   - Copper wire → green circuits should be direct insertion (wire assembler → circuit assembler, no belt)
   - Gear wheels → belts, engines, red science — direct insert from assembler to assembler
   - Every belt segment removed is UPS saved

**3. Belt compaction**
   - Use blue belts (or even green belts from mods) to max throughput per belt
   - Compress belts fully before feeding assemblers
   - Avoid sideloading and belt weaving (looks cool, costs UPS)

**4. Fluid simplification**
   - Use barreling+bot delivery instead of pipes for long-distance fluids
   - Build refineries with direct pipe connections (no underground pipes crossing each other)
   - **The "no pipe" approach:** Each refinery complex makes one product and ships it by train

**5. Solar > Nuclear > Steam**
   - Solar panels + accumulators = **zero UPS cost** after placing
   - Nuclear power requires fluid heat mechanics — significant UPS cost
   - Steam power with boilers is surprisingly UPS-heavy for the power output

**6. Disable biters (or clear them)**
   - Biters are heavy on UPS due to pathfinding and pollution calculations
   - Peaceful mode or cleared borders = 10-15% UPS savings at scale

### Measuring UPS Impact

Install the **Show FPS/UPS** mod (`/c game.show_fps=true` in console) or use the **Time Tool** mod to see exact entity update costs. Aim to keep entity update time under 8-10 ms per tick.

---

## 5. SPM Scaling: 100 → 1K → 10K

SPM (Science Per Minute) is the standard megabase metric. Here's what each tier requires.

### 100 SPM — Starter Megabase

- **Base style:** Main bus or simple city blocks
- **Raw resources:** ~2-4 iron ore belts (blue), ~2-3 copper ore belts
- **Oil:** ~1,000 crude oil/min
- **Modules:** Prod 2 / Speed 2
- **Buildings:** ~100-150 assemblers total
- **Power:** ~100-200 MW
- **Time to build:** 20-40 hours from a fresh start
- **Trains:** 1-4 trains, 4-6 stations

**Blueprint:** Belt-based 100 SPM is the most documented base design in Factorio. Search "Factorio 100 SPM blueprint book" for dozens of ready-made designs.

### 1,000 SPM — Full Megabase

- **Base style:** City blocks or dedicated production cells
- **Raw resources:** ~20-30 iron ore belts, ~15-25 copper ore belts
- **Oil:** ~10,000 crude oil/min
- **Modules:** Prod 3 / Speed 3 (12-beacon for high-volume items)
- **Buildings:** ~1,500-2,000 assemblers
- **Power:** ~4-6 GW (20,000+ solar panels, or 12-16 reactors)
- **Time to build:** 80-150 hours
- **Trains:** 30-50 trains, 1-4 or 1-8 config

**Key milestones:**
1. Massive green circuit production (~100 assemblers with 12-beacon)
2. Dedicated smelting arrays (electric furnaces, 12-beacon)
3. One city block per science pack (or per intermediate)
4. 4-8 rocket silos for space science
5. Logistics network covering the entire base for construction bots

**Common bottleneck:** Green circuits. A 1K SPM base needs ~600 green circuits/second. That's about 100 assemblers with 12-beacon design — each fed by direct-insertion copper wire.

### 10,000 SPM — Megabase Endgame

- **Base style:** Modular train grid, 3-8 trains, dedicated mining worlds
- **Raw resources:** ~200-300 iron ore belts, ~150-250 copper ore belts
- **Oil:** ~100,000+ crude oil/min
- **Modules:** Prod 3 everywhere, 12-beacon everything
- **Buildings:** ~15,000-20,000 assemblers
- **Power:** ~40-60 GW (400K+ solar panels, or separate modular reactor grid)
- **UPS at 60:** Requires aggressive optimization (see section 4)
- **Time to build:** 300-600 hours

**What changes at 10K SPM:**

1. **It's a UPS game now.** Every design decision is made for UPS savings, not aesthetics or ease of building.
2. **Mining productivity research** is critical — at level 100+ you get 5+ ore per mined tile, reducing mining outposts.
3. **Bots are banned** (or used minimally) in production chains. Everything is direct insertion or trains.
4. **Fluid must be barreled** or handled in dedicated on-site processing blocks. Pipes are too expensive.
5. **Beacon density must be maximized** — 12-beacon everything, even for low-volume items.

**The 10K SPM checklist:**
- [ ] Mining productivity ≥ 100
- [ ] 3-8 train infrastructure with grade-separated intersections
- [ ] Solar-only power (no fluid heat mechanics)
- [ ] Direct insertion for all intermediates
- [ ] No fluid pipes > 5 segments long
- [ ] Max 2 logistics chests per production block
- [ ] Use train deliveries for raw ore, not plates (faster throughput)
- [ ] Disable biters or clear them entirely
- [ ] Aim for < 6ms entity update time

### SPM Reference Table

| SPM | Iron Ore/min | Copper Ore/min | Oil/min | Power | Approx. UPS |
|-----|-------------|---------------|---------|-------|-------------|
| 60 | ~1,800 | ~1,200 | ~500 | 50 MW | 60 |
| 150 | ~4,500 | ~3,000 | ~1,500 | 150 MW | 60 |
| 500 | ~15,000 | ~10,000 | ~5,000 | 1-2 GW | 60 |
| 1,000 | ~30,000 | ~20,000 | ~10,000 | 4-6 GW | 60 |
| 2,500 | ~75,000 | ~50,000 | ~25,000 | 10-15 GW | 55-60 |
| 5,000 | ~150,000 | ~100,000 | ~50,000 | 20-30 GW | 45-55 |
| 10,000 | ~300,000 | ~200,000 | ~100,000 | 40-60 GW | 30-45 |

*Note: Actual numbers vary based on module levels, mining productivity research, and build efficiency. These are rough estimates for Prod 3 / Speed 3 builds with moderate mining productivity.*

---

## 6. Recommended Mods for Megabases

While vanilla megabases are absolutely possible, these mods improve quality of life and (counterintuitively) can improve UPS by reducing the number of entities needed:

| Mod | Purpose |
|-----|---------|
| [LTN (Logistic Train Network)](https://mods.factorio.com/mod/LogisticTrainNetwork) | Smart train scheduling with request/provider logic |
| [Cybersyn](https://mods.factorio.com/mod/cybersyn) | Modern alternative to LTN — simpler setup, same concept |
| [Rate Calculator](https://mods.factorio.com/mod/RateCalculator) | Calculate required assemblers/belts for a desired SPM |
| [Factory Planner](https://mods.factorio.com/mod/factoryplanner) | Full production chain planner with matrix solver |
| [Bottleneck Lite](https://mods.factorio.com/mod/BottleneckLite) | Visual indicators on machines that are starved/blocked |
| [Even Distribution](https://mods.factorio.com/mod/even-distribution) | Auto-balance items into machines and chests |
| [Squeak Through](https://mods.factorio.com/mod/Squeak%20Through) | Walk between tightly packed buildings |
| [Module Inserter](https://mods.factorio.com/mod/ModuleInserter) | Auto-insert modules so you don't have to |

---

## Quick-Reference Blueprint Links

- [100 SPM Main Bus Blueprint Book (Factorio Prints)](https://factorioprints.com/search?q=100+spm+bus)
- [1K SPM City Block Blueprint Book (Factorio Prints)](https://factorioprints.com/search?q=1000+spm+city+block)
- [10K SPM Megabase Blueprint Collection (Factorio Prints)](https://factorioprints.com/search?q=10000+spm+megabase)
- [12-Beacon Modular Tile Blueprints (Factorio School)](https://factoriocheatsheet.com/)

---

## 🎮 Get Factorio

Ready to build your factory? Pick up Factorio on Steam:

[![Factorio on Steam](https://i.imgur.com/0hDq0DN.png)](https://store.steampowered.com/app/427520/Factorio/?curator_clanid=44763507)

*Note: This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*

---

*Last updated: June 2026 | Game version: Factorio 2.0+ (Space Age compatible)*
