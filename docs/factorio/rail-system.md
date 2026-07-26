---
title: "Factorio Rail System Guide — Trains, Signals & Layouts"
description: "Complete guide to Factorio rail networks: track types, rail vs chain signals, junction designs, train configurations, station naming, LTN, City Blocks, and pros/cons of each layout."
---

# 🚂 Factorio Rail System Guide

Trains are the **backbone of every megabase**. A well-designed rail network scales to 10,000+ items per minute across dozens of outposts while a poorly built one deadlocks the moment a second train enters the picture. This guide covers everything you need to build a robust, deadlock-free rail system.

---

## 📋 Track Types & Rail Essentials

### Regular Rail vs Elevated Rail (2.0+)

Factorio 2.0 introduced elevated rails, fundamentally changing junction design.

| Feature | Regular Rail | Elevated Rail |
|:--------|:-------------|:--------------|
| **Max grade** | Any slope | Must be flat (no diagonal elevation change) |
| **Intersection with regular rail** | Same plane | Passes **over** — no collision |
| **Cost** | 1 Steel + 1 Stone | 4 Steel + 10 Concrete (per rail) |
| **Max speed** | Same as regular | Same as regular |
| **Best use** | Surface network, mining outposts | Grade-separated interchanges, crossing busy main lines |
| **Unlocked** | Railway tech | Elevated Railway tech (2.0) |

> 💡 **Key insight:** Elevated rails let you build **grade-separated junctions** where merging/diverging lanes never cross on the same plane — this is the single biggest improvement for high-throughput networks in 2.0.

### Rail Support Types

| Support | Height | Best For |
|:--------|:-------|:---------|
| **Low support** | 2 tiles high | Crossing belts, pipes, or other rails at ground level |
| **High support** | 6 tiles high | Crossing over lakes, cliffs, or entire factory blocks |

---

## 🚦 Signals: Rail vs Chain

Getting this wrong is the #1 cause of deadlocks. The rule is simple:

> **Rail signal** = "I can reserve the block ahead if it's empty."  
> **Chain signal** = "I can only enter the block ahead if I can also **exit** it."

### Comparison

| Signal Type | Enters Block On | Can Stop Inside | Typical Placement |
|:------------|:----------------|:----------------|:------------------|
| **Rail signal** | Block empty | ✅ Yes | Straight track segments, station exits |
| **Chain signal** | Block empty **and** exit block empty | ❌ No (reserves full path) | Junctions, merges, before crossings |

### Placement Rules of Thumb

```text
1.  Place a chain signal BEFORE every junction entrance.
2.  Place a rail signal AFTER every junction exit.
3.  Inside a junction, chain signals every 1-2 rail segments.
4.  On straightaways, space rail signals so the longest train JUST fits.
5.  At stations: chain signal before the station, rail signal after.
```

### Common Mistake: The "Chain-In-Rail-Out" Rule Violation

Bad layout:

```
→ [Chain] → [Junction] → [Chain] → [Junction] → [Chain] → [Rail]  ✓
→ [Rail]  → [Junction] → [Rail]  → [Junction] → [Rail]            ✗ (deadlock risk)
```

If a train stops inside a junction because of a rail signal ahead, it blocks **all intersecting routes**.

---

## 🛤️ Signal Block Logic (How Trains Actually "See")

Every signal divides the track into **blocks**. A train will never enter a block that another train occupies. Block size determines throughput.

| Block Size | Pros | Cons |
|:-----------|:-----|:-----|
| **Long blocks** (~train length) | Simple, fewer signals | Poor throughput on busy lines |
| **Short blocks** (1-4 rail segments) | High throughput, trains follow closely | More signals, marginal UPS cost |
| **Mixed** | Optimal | Requires planning |

**For megabases:** Short blocks (2 rails per block) on main lines. Long blocks in stations and low-traffic branches.

---

## ⚡ Train Configurations

### The Locomotive-to-Wagon Ratio

| Design | Locomotives | Cargo Wagons | Length (tiles) | Best For | Max Throughput (iron plates/min) |
|:-------|:------------|:--------------|:---------------|:---------|:---------------------------------|
| **1-1** | 1 | 1 | ~12 | Early game, personal transport | ~600 |
| **1-2** | 1 | 2 | ~19 | Mid-game, small outposts | ~1,200 |
| **1-4** | 1 | 4 | ~32 | Standard all-purpose | ~2,400 |
| **2-4** | 2 | 4 | ~35 | Heavy hauling with acceleration | ~2,400 |
| **1-8** | 1 | 8 | ~59 | Slow megabase hauler | ~4,800 |
| **2-8** | 2 | 8 | ~62 | **Megabase standard** | ~4,800 |
| **3-8** | 3 | 8 | ~65 | Fast megabase hauler (max acceleration) | ~4,800 |
| **4-12** | 4 | 12 | ~92 | Extreme bulk (low UPS cost per item) | ~7,200 |

### Acceleration Table (with no cargo)

| Design | Max Speed (km/h) | 0→100 km/h | Stopping distance (full) |
|:-------|:-----------------|:-----------|:-------------------------|
| 1-2 | 259 | ~2s | ~12 tiles |
| 1-4 | 259 | ~5s | ~24 tiles |
| 2-4 | 259 | ~2.5s | ~22 tiles |
| 2-8 | 259 | ~6s | ~42 tiles |
| 3-8 | 259 | ~3s | ~38 tiles |

> 💡 **Recommendation:** Start with **1-4** for mid-game. Upgrade to **2-8** for your megabase — it's the sweet spot between train length (fits standard station blueprints) and cargo per trip.

---

## 🔀 Junction Designs: Pros & Cons

### T-Junction

```
      │
      │
──┐   │
  │   │
──┘   │
      │
```

| Aspect | Rating |
|:-------|:-------|
| **Throughput** | ⭐⭐⭐ |
| **Space efficiency** | ⭐⭐⭐⭐ |
| **Deadlock risk** | Low (if signalled correctly) |
| **Difficulty** | Easy |
| **Best for** | Branch lines, low-to-medium traffic |

**Signalling:** Chain signal at each entrance, rail signal at each exit. Keep the junction area as one chain-signalled block.

### Standard Roundabout

```
  ┌─────┐
──┤     ├──
  │  ⏺  │
──┤     ├──
  └─────┘
```

| Aspect | Rating |
|:-------|:-------|
| **Throughput** | ⭐⭐ |
| **Space efficiency** | ⭐⭐⭐ |
| **Deadlock risk** | ⚠️ **HIGH** (see note) |
| **Difficulty** | Easy |
| **Best for** | Low-traffic intersections only |

> ⚠️ **Roundabout warning:** Standard 4-way roundabouts are famous for deadlocking. The circular path means a train entering from any direction can loop around and collide with itself or trap crossings. **If you use them**, use chain signals at every entrance and **no rail signals inside the circle**.

### Grade-Separated Interchange (Elevated Rails, 2.0+)

```
       ═══╗    ╔═══
          ║    ║
══╗       ║    ║       ╔══
  ║       ╝    ╚       ║
══╝                 ╚══
```

| Aspect | Rating |
|:-------|:-------|
| **Throughput** | ⭐⭐⭐⭐⭐ |
| **Space efficiency** | ⭐⭐ |
| **Deadlock risk** | Nearly zero |
| **Difficulty** | Hard (requires elevated rail planning) |
| **Best for** | 2+ lane bus networks, 1,000+ SPM megabases |

**How it works:** Through-traffic uses elevated rail to cross above the intersection. Merging/diverge lanes stay at ground level. No path crosses on the same plane — eliminated deadlock.

### Compact 4-Way (Nilaus / Spaghetti Style)

```
  ╔══╗  ╔══╗
  ║  ║  ║  ║
══╝  ╚══╝  ╚══
══╗  ╔══╗  ╔══
  ║  ║  ║  ║
  ╚══╝  ╚══╝
```

| Aspect | Rating |
|:-------|:-------|
| **Throughput** | ⭐⭐⭐⭐ |
| **Space efficiency** | ⭐⭐⭐⭐ |
| **Deadlock risk** | Low |
| **Difficulty** | Medium |
| **Best for** | City block grids, high density |

A compact 4-way using braided (crossing) tracks with careful chain signalling. Very space-efficient but requires precise signal placement.

---

## 🏛️ City Block Concept

The **City Block** system is the most popular megabase organization method. The idea: divide the map into a grid of identical blocks, each dedicated to one production process.

### Standard Block Sizes

| Block Size (tiles) | Rails Around | Stations Inside | Best For |
|:-------------------|:-------------|:----------------|:---------|
| **100×100** | 2-lane | 1-2 (1-4 trains) | Early megabase |
| **104×104** | 2-lane | 2 (1-4 trains) | Nilaus standard |
| **124×124** | 4-lane | 2-3 (2-8 trains) | Large-scale megabase |
| **160×160** | 4-lane | 4+ (2-8 trains) | Extreme throughput |

### Pros & Cons

| Pros | Cons |
|:-----|:------|
| ✅ Blueprintable — paste and connect | ❌ Wastes space on low-density items (e.g. gears) |
| ✅ Easy to expand — add blocks on the edge | ❌ Grid imposes fixed station orientation |
| ✅ Well-suited for LTN or vanilla train networks | ❌ Crossing the grid with belts/bots adds complexity |
| ✅ Clear visual organization | ❌ Signal placement must be perfectly consistent |

### City Block Roundabout Placement

Each City Block junction should be signalled identically:

1. **Chain signal** on every entrance rail.
2. **Chain signal** between each intersecting segment inside the junction.
3. **Rail signal** on every exit rail, placed so the block past it is at least as long as the longest train.

---

## 📦 LTN (Logistic Train Network) Concepts

**LTN** is a popular mod that treats trains like logistic bots — depots, requests, and automatic dispatch.

| Feature | Vanilla | LTN |
|:--------|:--------|:----|
| **Train scheduling** | Manual (fixed schedule per train) | Automatic (dynamic dispatch) |
| **Multiple requests per station** | Needs multiple trains | 1 train serves many requests |
| **Depot** | Not needed | Required — idle trains wait here |
| **Stacking** | Separate stacker blueprint | Built into depot logic |
| **Complexity** | Low | Medium-High |
| **UPS cost** | Lower | Slightly higher (combinator logic) |
| **Best for** | ~50 trains or fewer | 50+ trains, complex networks |

### LTN Station Naming Convention

| Station Function | Name Pattern | Example |
|:-----------------|:-------------|:---------|
| **Provide** | `[item] Provide` | `Iron Plate Provide` |
| **Request** | `[item] Request` | `Green Circuit Request` |
| **Depot** | `[LTN] Depot` | `[LTN] Depot 01` |
| **Fuel stop** | `[item] Fuel` | `Nuclear Fuel Fuel` |

> 💡 LTN uses **combinators** to read chest contents and set request thresholds. A station only calls a train when its buffer drops below the threshold.

---

## 🏷️ Station Naming Conventions (Vanilla)

Even without LTN, consistent naming prevents chaos.

### Recommended Convention

| Pattern | Example | Effect |
|:--------|:---------|:-------|
| `[item] Load` | `Iron Plate Load` | Provider station — trains load here |
| `[item] Unload` | `Iron Plate Unload` | Consumer station — trains unload here |
| `[item] Load [N]` | `Iron Plate Load 1` | Multiple identical provider stations |
| `[train-stack] Wait` | `Iron Plate Wait` | Stacker / waiting bay before a load station |
| `Depot [N]` | `Depot 01` | Fuel & waiting area for idle trains |

### Logical Naming for Mixed Cargo Stations

| Pattern | Example | Use Case |
|:--------|:---------|:---------|
| `[A] [B] Load` | `Iron Copper Load` | Mixed ore pickup |
| `[A] → [B]` | `Iron → Steel` | Direct smelting drop |
| `Mall [N]` | `Mall 01` | Building supply station |

> 💡 **Rule of thumb:** Keep names **short** (<15 chars) so they're visible in the train GUI. Use underscores instead of spaces if you prefer.

---

## 🏗️ Specific Rail Layouts

### 2-Lane Two-Way System (Early Game)

```
←──────────────────
──────────────────→
```

| Aspect | Detail |
|:-------|:-------|
| **Track count** | 2 (one each direction) |
| **Min radius** | Any |
| **Throughput** | ~8 trains/min per direction |
| **Best for** | Up to blue science |
| **Signal spacing** | ~1 train length apart |
| **Upgrade path** | → 4-lane or 2-lane elevated |

### 4-Lane System (Megabase Standard)

```
←────────────────── ──────────────────→
←────────────────── ──────────────────→
            (or inner = express)
```

| Aspect | Detail |
|:-------|:-------|
| **Track count** | 4 (2 each direction) |
| **Min radius** | Use basic rail curves (avoid too tight) |
| **Throughput** | ~30+ trains/min per direction |
| **Best for** | 500+ SPM, city blocks |
| **Signal spacing** | 4-6 rail pieces between signals |
| **Usage** | Inner lanes = express / outer lanes = local |

**Pro tip:** Use the inner 2 lanes for **express trains** that pass through without stopping, and outer lanes for **local trains** that are approaching/leaving stations. This prevents a stopped local train from blocking express traffic.

### 2-Lane Elevated Trunk (2.0+)

```
←  (elevated, above everything)
→
```

| Aspect | Detail |
|:-------|:-------|
| **Track count** | 2 (one each direction) |
| **Elevation** | 6 tiles above ground |
| **Throughput** | ~15+ trains/min |
| **Best for** | Crossing lakes, bases, or existing rail |
| **Signal spacing** | 8-10 rail pieces (fewer interruptions) |
| **Cost** | Higher material cost |

### Stacker / Waiting Bay Design

```
         ┌──[Station 1]──┐
         ├──[Station 2]──┤
─────────┤  ├──[Station 3]──┤─────→
         ├──[Station 4]──┤
         └──[Station 5]──┘
```

| Stacker Type | Tracks | Capacity | Space | Best For |
|:-------------|:-------|:---------|:------|:---------|
| **Parallel** | Side-by-side | Unlimited | Wide | High-throughput processing |
| **Serpentine** | Shared single track | 4-8 trains | Compact | Low space availability |
| **Inline** | Station-only | 1 train per station | Minimal | Low-traffic outposts |

**Signalling:** Chain signal at the stacker entrance. Rail signal at each stacker bay exit. Rail signal at each station exit.

---

## 📊 Rail Network Throughput Comparison

| Layout | Max Trains/min (single direction) | Deadlock Risk | Build Complexity | Space Required (per km) |
|:-------|:----------------------------------|:--------------|:-----------------|:-------------------------|
| 2-lane two-way | 8-12 | Medium | Low | 4 tiles |
| 2-lane one-way (basic junctions) | 15-20 | Low | Low | 4 tiles |
| 2-lane elevated trunk (2.0+) | 20-30 | Very Low | Medium | 4 tiles (ground footprint minimal) |
| 4-lane (compact junctions) | 30-40 | Low | Medium | 8 tiles |
| 4-lane (grade-separated) | 50+ | Near zero | High | 8 tiles |
| City block grid (2-lane, 100×100) | 25-35 per edge | Low (if signalled correctly) | Medium | Grid-dependent |

---

## ⚠️ Common Mistakes & Fixes

| Mistake | Symptom | Fix |
|:--------|:--------|:----|
| Rail signal inside a junction | Trains stop in the intersection | Replace with chain signal |
| Too few chain signals | Trains enter junction without exit path | Chain signal at every entrance + internal segment |
| Station on a main line | Through traffic blocked by loading train | Build a stacker/passing lane |
| Single-track bidirectional (shared rail) | Head-on collisions waiting to happen | Convert to two parallel one-way tracks |
| No fuel management | Trains stranded with empty fuel | Add fuel request to depot stations |
| Mixed train lengths on same line | Signal spacing issues (trains stop mid-block) | Standardize train length per line |
| Elevation changes on curve | Unbuildable / janky rail placement | Keep curves flat; use elevated transition ramps on straight sections |

---

## 📚 Blueprint & Reference Links

| Resource | Link |
|:---------|:------|
| Nilaus City Block Blueprint Book | [factorioprints.com](https://factorioprints.com) |
| Official Factorio Wiki — Railway | [wiki.factorio.com](https://wiki.factorio.com/Railway) |
| Factorio Calculator & Planner | [kirkmcdonald.github.io](https://kirkmcdonald.github.io) |
| Train Signalling Tutorial (Video) | [YouTube ~Nilaus~](https://youtube.com) |
| r/factorio Rail Design Showcase | [reddit.com/r/factorio](https://reddit.com/r/factorio) |

---

> 🛒 [**Buy Factorio on Steam**](https://store.steampowered.com/app/427520/) — The highest-rated game on Steam (98% positive). One purchase includes the base game; the Space Age DLC adds 4 new planets.
>
> *Rail stats verified against Factorio 2.0. Elevated rail and space age mechanics included where noted.*
