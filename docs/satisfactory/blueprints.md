---
title: Satisfactory Blueprint System Guide — Complete Blueprint Designer Tutorial
description: Complete guide to Satisfactory's blueprint system. Blueprint Designer tiers (Mk.1/Mk.2/Mk.3), size limits, efficient blueprints, import/export, and the best blueprint libraries.
date: 2026-07-05
---

# 📐 Satisfactory Blueprint System Guide

*Last updated: July 2026 | Game version: 1.0+*

The **Blueprint System** is one of the most powerful tools in Satisfactory. Introduced in Update 8 and refined for 1.0, it lets you save, paste, and share modular factory sections — transforming hours of repetitive building into seconds of blueprint placement.

This guide covers everything from unlocking blueprints to designing production-ready modules.

---

## 1. What Are Blueprints?

Blueprints are saved collections of buildings, belts, pipes, and foundations that you can **place instantly** anywhere in your world. Think of them as pre-fabricated factory modules.

| Feature | Detail |
|---------|--------|
| **Unlock** | Tier 4 — Advanced Manufacturing (MAM: Caterium research) |
| **Save format** | `.cfg` files (plain text, editable) |
| **Location** | `%LOCALAPPDATA%/FactoryGame/Saved/SaveGames/blueprints/` |
| **Sharing** | Copy `.cfg` files → share with others |
| **Paste mode** | Snap-to-grid or free placement |

> 💡 **Blueprinting is essential post-Tier 4.** Without it, building repeated production lines (smelting arrays, circuit factories) becomes painfully tedious.

---

## 2. Blueprint Designer Tiers

The **Blueprint Designer** is the machine used to create blueprints. It comes in three sizes, each unlocked separately.

### Mk.1 Blueprint Designer

| Stat | Value |
|-----|-------|
| **Size** | 4×4 foundation tiles |
| **Unlock** | Tier 4 — Advanced Manufacturing |
| **Cost** | 10 Reinforced Iron Plate + 50 Cable + 250 Concrete |
| **Max build volume** | 4×4×4 tiles |
| **Best for** | Smelting arrays, power plant modules |

The Mk.1 fits on a single 4×4 foundation. It's enough for small modules but very limiting for complex production.

### Mk.2 Blueprint Designer

| Stat | Value |
|-----|-------|
| **Size** | 6×6 foundation tiles |
| **Unlock** | Tier 6 — Train technology milestone |
| **Cost** | 10 Heavy Modular Frame + 50 Computer + 250 Concrete |
| **Max build volume** | 6×6×6 tiles |
| **Best for** | Production cell blueprints, train stations |

The Mk.2 is the **sweet spot** — large enough for meaningful factory modules but not so large that blueprints become unwieldy.

### Mk.3 Blueprint Designer

| Stat | Value |
|-----|-------|
| **Size** | 8×8 foundation tiles |
| **Unlock** | Tier 8 — Endgame milestones |
| **Cost** | 10 Turbo Motor + 50 Radio Control Unit + 250 Concrete |
| **Max build volume** | 8×8×8 tiles |
| **Best for** | Full production lines, mega-modules |

The Mk.3 enables massive modules. An 8×8×8 volume is enough for a complete heavy modular frame factory or a fully self-contained aluminum processing plant.

### Size Comparison

| Designer | Foundations | Max Volume (tiles) | Best Use |
|----------|-------------|--------------------|----------|
| Mk.1 | 4×4 | 64 | Small arrays, smelting, power |
| Mk.2 | 6×6 | 216 | Mid-game cells, train stations |
| Mk.3 | 8×8 | 512 | Endgame modules, full lines |

---

## 3. Blueprint Design Principles

### Rule 1: Design for Repeatability

A good blueprint can be placed side-by-side with itself without gaps or overlaps.

```
❌ Bad: Input belts exit the blueprint area on the right
✅ Good: Input belts terminate at the blueprint edge with clear merge points
```

**Checklist for repeatable blueprints:**

- [ ] Belt inputs/outputs at exact grid-aligned positions
- [ ] Pipe inputs/outputs at standardized heights (2m, 4m)
- [ ] Power poles at blueprint edges for simple daisy-chaining
- [ ] Foundation is flush with the blueprint boundary

### Rule 2: Use Vertical Space

Satisfactory allows stacking foundations. A 4×4×4 volume can fit **multiple floors**.

| Floor | Purpose |
|-------|---------|
| Ground | Logistics (belts, splitters, mergers) |
| Floor 1 | Production machines |
| Floor 2 | Belt lifts bring inputs up, outputs down |
| Roof | Power poles, walkways |

> 💡 **Vertical blueprint trick:** Build your logistics layer on floor -1 (foundation sunk by 1m), machines on floor 0, and output belts on floor 1. This gives clean, separate layers for belts and machines.

### Rule 3: Overclock Once, Blueprint Always

Design blueprints for **fully overclocked machines** (250% clock speed). This way you only need to calculate ratios once and can paste the same cell wherever needed.

### Rule 4: Standardize Connections

| Connection Type | Standard Position | Orientation |
|-----------------|-------------------|-------------|
| Raw ore input | Bottom edge, center | Belt level 1 |
| Ingot output | Top edge, offset | Belt level 2 |
| Fluid input | Left edge, 2m height | MK2 pipe |
| Fluid output | Right edge, 2m height | MK2 pipe |
| Power | Back edge, pole at 2m | Wall outlet |
| Water | Bottom-left | MK2 pipe |

---

## 4. Essential Blueprints to Build

### 🏗️ Smelting Array (Mk.1, 4×4)

A basic 8-smelter array for iron or copper:

```
Blueprint contents:
- 8 Smelters (2 rows of 4)
- 1 Mk.3 belt input (splitter tree → 8 smelters)
- 1 Mk.3 belt output (merger tree from 8 smelters)
- 2 power poles (daisy-chainable)
- 4×4 foundation base
```

| Input | Output | Power |
|-------|--------|-------|
| 480 ore/min (pure node, Mk.3 miner) | 480 ingots/min | ~48 MW |

### 🔋 Coal Generator Block (Mk.2, 6×4)

A standard 8-generator coal power plant:

```
Blueprint contents:
- 8 Coal Generators (2 rows of 4)
- Central water pipe manifold (4 extractors feed in)
- Coal belt manifold (front)
- 2 power poles
- 6×4 foundation base
```

| Inputs | Outputs | Power |
|--------|---------|-------|
| 480 coal/min, 720 water/min | 8 generators | 600 MW |

**Pipe layout:**

```
Water → Pipe Junction → Pipe Junction
         ↓                ↓
Extractor 1-4      Main pipe running generators
         ↓                ↓
    [Generator 1-4]    [Generator 5-8]
```

### 🚂 Train Station Pair (Mk.3, 8×8)

A complete loading/unloading station pair:

```
Blueprint contents:
- 2 Train Stations (back-to-back)
- 8 Freight Platforms (4 per station)
- Belt input manifolds (12 belts → 4 cargo slots per station)
- 2 Fluid platforms (if needed)
- Signal posts, power infrastructure
- Walkways along both sides
```

### 🧊 Aluminum Processing Cell (Mk.3, 8×8)

```
Blueprint contents (3 floors):
- Floor -1: Bauxite input belts, water pipe manifold, coal belt
- Floor 0: 4 Refineries (Alumina Solution)
- Floor 1: 4 Refineries (Aluminum Scrap) plus water recycling
- Floor 2: 4 Foundries (Aluminum Ingot), output belt
- Roof: Power infrastructure
```

| Inputs | Outputs |
|--------|---------|
| 720 bauxite/min, 480 coal/min, water | ~480 aluminum ingots/min |

### 📦 Storage Mall (Mk.2, 6×6)

A wall of storage containers connected to a main belt:

```
Blueprint contents:
- 16 Storage Containers (4×4 grid)
- 1 main input belt with programmable splitters
- 1 overflow belt to AWESOME Sink
- Power for smart splitters
- Walkway in front
```

---

## 5. Blueprint Import & Export

### Exporting Blueprints

1. Build a **Blueprint Designer** (Mk.1/2/3)
2. Open the designer UI (E key)
3. Build your module **inside** the designer volume
4. In the designer UI, click **Save Blueprint**
5. Name your blueprint (descriptive names help!)
6. The `.cfg` file is saved to your blueprints folder

### Importing Blueprints

| Method | Steps |
|--------|-------|
| **From file** | Place `.cfg` files in `.../blueprints/` folder, restart game |
| **From clipboard** | Copy `.cfg` content, paste using blueprint library |
| **From community** | Download from [satisfactoryblueprints.com](https://satisfactoryblueprints.com) → extract to blueprints folder |

### Blueprint File Location

```
Windows: %LOCALAPPDATA%/FactoryGame/Saved/SaveGames/blueprints/
Steam Cloud: .../Steam/userdata/<steam-id>/526870/remote/blueprints/

Example:
C:/Users/<you>/AppData/Local/FactoryGame/Saved/SaveGames/
  blueprints/blueprint-name.cfg
```

### Naming Convention

Good naming helps you find blueprints quickly:

```
[Type]-[Input]-[Output]-[Size]

Examples:
smelter-iron-480-4x4
power-coal-8gen-6x4
train-station-dual-8x8
aluminum-cell-480-8x8
storage-mall-16box-6x6
```

---

## 6. Recommended Blueprint Libraries

| Website | Description | Items |
|---------|-------------|-------|
| [Satisfactory Blueprints](https://satisfactoryblueprints.com) | Largest community library | 10,000+ blueprints |
| [Satisfactory Calculator — Blueprints](https://satisfactory-calculator.com/en/blueprints) | Production-optimized blueprints | Tool-integrated |
| [SCIM Blueprints](https://satisfactory-calculator.com/en/blueprints) | Popular blueprints from the community | Filterable by tier |
| [r/Satisfactory Blueprints](https://reddit.com/r/SatisfactoryBlueprints) | Reddit community | Screenshot + CFG |

> 💡 **Always verify blueprints before pasting.** Check belt tiers match your tech level and that pipe connections are correct for your setup.

---

## 7. Advanced Blueprint Techniques

### Nested Blueprints

Build small blueprints (Mk.1) and combine them into larger ones (Mk.3).

```
Example:
Mk.1: 4-smelter cell → Place 4 in Mk.3 Designer
Mk.3: 16-smelter array
```

### Blueprint Editing

Blueprints are `.cfg` files — plain text. Advanced players can:

- **Edit belt tiers:** Replace `mConveyorBeltMk4` with `mConveyorBeltMk6`
- **Change recipes:** Swap production recipes in manufacturer blueprints
- **Adjust clock speeds:** Change `mCurrentRecipeRate` values
- **Fix connection errors:** Realign misplaced pipe or belt connections

> ⚠️ **Edit cautiously.** One wrong character can corrupt the blueprint. Always back up your blueprints before editing.

### Soft Blueprinting

Place a blueprint and use the **Soft Clearance** mode (default in 1.0) to allow buildings to overlap with existing structures. Useful for upgrading existing factory sections without tearing them down first.

### Blueprint Modules for Large Bases

For megabase-scale builds, create a **standard module** and tile it:

```
1. Define your standard production cell size (e.g., 8×8)
2. Design each function as a standalone blueprint
3. Lay out a grid of foundations
4. Populate with blueprints
5. Connect belts between cells
```

---

## 8. Common Blueprint Mistakes

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| Non-aligned inputs/outputs | Blueprints don't connect side-by-side | Always snap belts to grid positions |
| Including too much foundation | Overlapping foundations on placement | Only include foundation where machines sit |
| Building outside designer volume | Parts get cut off on save | Stay within the highlighted build area |
| No power connections | Manual wiring every time | Add power poles at blueprint edges |
| Wrong belt tier | Bottleneck in early game | Design for max belt tier, underclock if needed |
| Over-complex first blueprints | Frustrating to debug | Start simple (smelter arrays, power plants) |

---

## 9. Blueprint Upgrade Path

| Game Phase | Designer | Focus |
|------------|----------|-------|
| **Tier 4-5** | Mk.1 (4×4) | Smelting arrays, constructor lines |
| **Tier 6-7** | Mk.1 + Mk.2 | Coal power, train stations, oil processing |
| **Tier 7-8** | Mk.2 + Mk.3 | Aluminum cells, heavy frames, computers |
| **Endgame** | Mk.3 (8×8) | Full production lines, mega-modules |

---

## 🔗 Related Guides

- [Satisfactory Complete Guide](/satisfactory/) — Main hub
- [Production Line Guide](/satisfactory/lines/) — Ratios, manifolds, load balancers
- [Logistics Optimization](/satisfactory/logistics/) — Belts, pipes, trains, drones
- [Tier Progression](/satisfactory/tiers/) — When to unlock each designer

---

## 🎮 Get Satisfactory

[**🎮 Satisfactory on Steam — $34.99**](https://store.steampowered.com/app/526870)

*This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*

---

*Last updated: July 2026 | Game version: Satisfactory 1.0+*
