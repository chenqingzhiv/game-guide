---
title: "Timberborn Endgame Guide — Rocket, Mega-Districts & Bionic Upgrades"
description: "Complete Timberborn endgame guide. Building the rocket, bionic upgrade priorities, mega-district layout for 200+ beavers, drought-proof power and water systems, and population optimization."
date: 2026-07-06
tags: [Timberborn, endgame, rocket, guide]
---

# 🏆 Timberborn Endgame Guide

*Last updated: July 2026 | Game version: Update 5+*

---

Timberborn's endgame shifts from basic survival to industrial-scale colony management. You'll manage 200+ beavers across multiple districts, construct the rocket for the victory condition, and unlock bionic upgrades that transform your beavers into super-workers. This guide covers everything you need for the endgame push.

---

## Victory Condition: Building the Rocket

The rocket is Timberborn's only victory condition. It requires massive resource throughput.

### Rocket Construction Phases

| Phase | Materials Required | Science Cost | Notes |
|:------|:-------------------|:-------------|:------|
| **Launch Pad** | 60 Planks + 20 Treated Planks | 1000 | Foundation, 5×5 area |
| **Booster Stage** | 300 Metal Blocks + 50 Explosives | 2000 | Requires 3+ Smelters running |
| **Fuel Tank** | 200 Planks + 150 Metal + 100 Treated Planks | 3000 | Need continuous maple syrup for treated planks |
| **Command Module** | 150 Metal Blocks + 50 Treated Planks | 4000 | Final assembly |
| **Fuel** | 500 Biofuel (or alternative) | — | From potatoes/chestnuts via distilleries |

### Rocket Resource Pipeline

```
Forestry ═══► Logs → Sawmills → Planks ──► Rocket
                    ↓
              Treated Planks ←─ Maple Syrup ←─ Maple Trees
                    ↓
              ──────────── Rocket ───────────
                    ↑
Mines ═══► Iron/Metal → Smelters → Metal Blocks
                    ↑
           Explosives Factory ←─ Coal + Sulfur
```

### Pre-Rocket Stockpile Targets

| Resource | Target | Production Needed |
|:---------|:-------|:-----------------|
| Planks | 500+ | 4-5 Large Sawmills |
| Treated Planks | 200+ | 3 Treated Planks workshops |
| Metal Blocks | 600+ | 3 Smelters + 2 Mines |
| Explosives | 60+ | Explosives factory with dedicated hauler |
| Biofuel | 600+ | 3 Distilleries + potato farm |
| Science | 5000+ saved | Multiple observatories/inventors |

```
💡 Rocket tip: Start your rocket resource pipeline when you hit 100 beavers.
Collecting the materials takes 20-30 days even with optimized production.
Don't wait — stockpile as you expand.
```

---

## Bionic Upgrades

Bionic upgrades are permanent beaver improvements researched in the Bionic Laboratory.

### Upgrade Details

| Upgrade | Science Cost | Effect | Cost in Materials | Priority |
|:--------|:-------------|:-------|:-----------------|:---------|
| **Steel Teeth** | 800 | +50% Gather/Rate | 20 Metal, 5 Planks | ★★★★★ |
| **Iron Stomach** | 600 | +50% Carry Capacity | 15 Metal, 5 Treated Planks | ★★★★☆ |
| **Reinforced Bones** | 1000 | +50% Lifespan | 30 Metal, 10 Planks | ★★★★★ |
| **Bionic Limb** | 1200 | +30% Build Speed | 40 Metal, 5 Treated Planks | ★★★☆☆ |
| **Brain Implant** | 1500 | +25% Work Speed | 50 Metal, 10 Treated Planks | ★★★★☆ |

### Upgrade Priority Guide

```
Phase 1 (First 1000 science):
  1. Steel Teeth (+50% gather) — your whole economy is built on gathering
  2. Reinforced Bones (+50% lifespan) — fewer deaths = fewer replacements

Phase 2 (Next 2000 science):
  3. Brain Implant (+25% work speed) — affects ALL buildings
  4. Iron Stomach (+50% carry) — helps logistics across districts

Phase 3 (Final 3000+ science):
  5. Bionic Limb (+30% build speed) — only matters for construction projects
```

### Upgrade Strategy

- **Don't upgrade all beavers equally.** Prioritize builders and gatherers first.
- **Apply Steel Teeth to all gatherers.** 50% more resources from the same buildings.
- **Reinforced Bones is multiplicative.** A base 50-day lifespan becomes 75 days — fewer deaths during droughts.
- **Brain Implant affects work speed** which includes everything from smelting to farming. This is the best ROI after lifespan.
- **Use the upgrade window:** When a beaver is selected, their upgrade slots show in the UI. Apply all available upgrades to your workforce.

---

## Mega-District Architecture

### The 5-District Model

For population 200+, this is the optimal district layout:

| District | Population | Focus | Buildings | Key Stats |
|:---------|:-----------|:------|:-----------|:----------|
| **A: Capitol** | 30-40 | Residential + Food | Lodges, Grills, Bakery, Water Pumps | Housing: 5+ Large Lodges |
| **B: Industrial** | 40-60 | Wood, Planks, Metal | Sawmills, Smelters, Workshops | 3 Smelters + 6 Sawmills |
| **C: Science** | 30-40 | Research, Paper, Books | Observatories, Inventors, Paper Mills | 500+ science/day |
| **D: Power & Water** | 20-30 | Dams, Turbines, Water Pumps | 3 Large Water Tanks, 6 Turbines | 10000+ water stored |
| **E: Mega-Farm** | 40-60 | All crops + Forestry | Farms, Orchards, Forester Huts | 12+ farm plots, 3 forests |

### District Connection Infrastructure

```
A (Residential)
│
├═══ Aqueduct ═══► B (Industrial)     — Water flow via channels
├═══ Road + Belt ═► B                 — Goods via Distribution Post
├═══ Tunnel ═════► C (Science)        — Underground paths (temperature)
│
B ─── Belt ───► D (Power+Water)       — Metal/Planks for upgrades
B ─── Belt ───► E (Farm)              — Fertilizer/Seedlings
│
E ─── Belt ───► A (Food)              — Crops → Capitol kitchens
D ─── Aqueduct ─► E (Farm)            — Irrigation water
```

### Distribution Post Settings

| Route | Goods | Priority | Min/Max Stock |
|:------|:------|:---------|:--------------|
| A ← E | Potatoes, Carrots, Bread | High | 50/200 |
| A ← B | Planks, Metal | Medium | 20/100 |
| B → E | Fertilizer, Planks | Low | 20/80 |
| C → All | Books, Science | High | 10/50 |
| B → D | Planks, Gears | Medium | 30/150 |

```
🏘️ District tip: Set District Crossing at 50+ beaver capacity.
One crossing handles ~10 beavers/min. For 200 beavers, use 3-4 crossings
between major districts (A↔B, B↔C, A↔E).
```

---

## Population 200+ Management

### Housing Requirements

| Building Type | Beavers Housed | Comfort Level | Materials | Count Needed |
|:--------------|:---------------|:--------------|:----------|:-------------|
| Small Lodge | 2 | 3 | 20 Planks | 20+ for breeding pairs |
| Large Lodge | 4 | 5 | 50 Planks, 10 Treated | 15+ for bulk housing |
| Penthouse | 2 | 8 | 80 Planks, 20 Metal | 5+ for breeders |

**Target:** 15 Large Lodges + 10 Small Lodges = 80 housing units for 200 beavers.

### Breeding Management

| Need | Setup | Notes |
|:-----|:------|:------|
| **Breeding Pods** | 5-6 pods | Each pod produces 1 beaver every ~5 days |
| **Wellbeing > 10** | Decorations + Carousels + Monuments | Required for breeding to function |
| **Housing available** | At least 10 empty beds | Beavers stop breeding when full |
| **Food surplus** | 1000+ food stored | Breeding stops below 500 food |

### Population Control

```
Drought protocol:
  - Reduce breeding to 1-2 pods during drought
  - Stockpile food before (3000+ units)
  - Emergency: Deactivate pods entirely if food < 1000

Expansion protocol:
  - Max breeding (5-6 pods) when:
    • Food production > 50/day
    • Water > 5000 stored
    • Housing > 20 empty beds
  - New district when current district hits 60 population
```

---

## Water Management at Scale

### Drought-Proof Water Storage

| Structure | Water Capacity | Materials | Best Use |
|:----------|:---------------|:----------|:---------|
| Small Water Tank | 50 | 10 Planks | Emergency only |
| Large Water Tank | 200 | 30 Planks, 5 Metal | Primary storage |
| Deep Reservoir | 1000+ | Dams + Excavation | Mega-project storage |

### Reservoir Design

```
A 4-deep reservoir (5×20 tiles) holds approximately 4000 units.

  ════════════════════════  ← Dam wall (source side)
  ║                      ║  
  ║   20 tiles × 5 tiles ║  ← 4m deep excavation
  ║   4m deep            ║  
  ║                      ║
  ╚═══════════════════════╝  ← Dam wall (downstream)

Fill time: ~3 days with 3 Water Dumps
Drain time: ~30 days for 200 beavers (drinking + irrigation)
```

### Water Conservation

- **Waste not:** Use Mechanical Water Pumps (not manual) at scale — 3x faster
- **Recycle:** Route water from industrial districts back to farm irrigation
- **Evaporation control** — Water evaporates from surfaces wider than 3 tiles. Keep channels narrow (2 tiles wide) to minimize loss.
- **Sludge:** Contaminated water can be filtered through purification sluices before returning to the main system

---

## Power Systems for Endgame

### Gravity Battery Power Wall

```
         ════════════  ← Water channel (source at high elevation)
         ↓ ↓ ↓ ↓ ↓ ↓  
        ┌─┐┌─┐┌─┐┌─┐ ← Water Wheels (tier 2+)
        └─┘└─┘└─┘└─┘
         ↓ ↓ ↓ ↓ ↓ ↓  
         ════════════  ← Drain channel to lower elevation
```

Each Water Wheel (tier 2) produces 200 HP at 2.0 flow rate. A wall of 6 wheels = 1200 HP.

### Power Distribution

| Generation Method | HP Output | Build Cost | Reliability |
|:-----------------|:----------|:-----------|:------------|
| Small Windmill | 60-100 | 20 Planks | Unreliable (wind dependent) |
| Large Windmill | 150-350 | 50 Planks, 10 Metal | Unreliable |
| Water Wheel (T1) | 100-150 | 30 Planks, 5 Gears | 100% if flow constant |
| Water Wheel (T2) | 175-250 | 40 Planks, 10 Metal | 100% if flow constant |
| Engine | 500 | 100 Planks, 30 Metal | Fuel-dependent, expensive |
| **Gravity Battery** | 1000+ | Complex reservoir | 100% reliable after setup |

### Endgame Power Target

| Requirement | HP Needed | Solution |
|:------------|:-----------|:---------|
| Basic colony (50-80) | 300-500 | 2 Large Windmills + 1 Water Wheel |
| Mid-game (100-150) | 800-1200 | Gravity battery + 3 Water Wheels |
| **Endgame (200+)** | **2000-3000** | **Gravity battery wall + 2 Engines (emergency)** |

---

## Mega-Farming for 200 Beavers

### Daily Consumption

| Resource | Per Beaver/Day | For 200 Beavers | Crop Plots Needed |
|:---------|:---------------|:----------------|:------------------|
| Food (general) | 2.5 units | 500/day | 60+ plots |
| Water | 20 units | 4000/day | — (reservoir) |
| Maple Syrup (planter) | 0.1 | 20/day | 15+ maple trees |
| Potatoes/Biofuel | 0.5 (distillery) | 100/day | 30+ potato plots |

### Crop Rotation for 200 Beavers

| Crop | Plots | Yield/Day | Purpose |
|:-----|:------|:----------|:--------|
| Potatoes | 25 | 150 | Biofuel + Grilled Potatoes |
| Carrots | 15 | 100 | Direct food + Breeding |
| Wheat | 20 | 120 | Bread (processed through Bakery) |
| Sunflower | 10 | 60 | Oil (for Engines) |
| Chestnuts | 15 | 75 | Treated Planks (maple) |
| Blueberries | 10 | 50 | Decorative + Extra food |

### Automated Farm Layout

```
  ┌───🌾──┬───🌾──┬───🌾──┬───🌾──┐
  │Wheat  │ Wheat │ Wheat │ Wheat │  ← Row 1 (auto-harvest radius)
  ├───🥔──┼───🥔──┼───🥔──┼───🥔──┤
  │Potato │Potato │Potato │Potato │  ← Row 2
  ├───🥕──┼───🥕──┼───🥕──┼───🥕──┤
  │Carrot │Carrot │Carrot │Carrot │  ← Row 3
  ├───🌻──┼───🌻──┼───🌻──┼───🌻──┤
  │Sunfl. │Sunfl. │Sunfl. │Sunfl. │  ← Row 4
  └───────┴───────┴───────┴───────┘
  
  4 Farmhouses, each covering their quadrant.
  Irrigation channels between rows.
  Forester Hut on each side for tree regen.
```

---

## Endgame Milestone Checklist

- [ ] Rocket research complete (Launch Pad → Command Module)
- [ ] All 5 bionic upgrades researched
- [ ] 200+ beaver population stable
- [ ] 5-district layout operational
- [ ] 10,000+ water stored (drought-proof)
- [ ] 3,000+ food surplus
- [ ] 2,000+ HP power grid (gravity battery)
- [ ] 500+ science/day production
- [ ] Rocket fuel bank (500+ biofuel)
- [ ] Explosives factory running
- [ ] Breeding pods at 6 for replacement rate

> *Data sourced from the [Timberborn Wiki](https://timberborn.fandom.com/) and community theorycrafting (Update 5). Rocket recipes and bionic costs may change with future updates.*
