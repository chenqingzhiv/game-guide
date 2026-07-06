---
title: Rust Farming Guide 2.0 — Plant Genetics, Water, Fertilizer & Clones
description: Complete Rust farming guide for the Farming 2.0 system. Genetics, cross-breeding, optimal watering, fertilizer compounding, and automated greenhouse designs.
---

# 🌱 Rust Farming Guide 2.0

> Data version: Rust 2026 | Last updated: 2026-07

Rust's Farming 2.0 system is surprisingly deep. With the right genetics, water management, and fertilizer strategy, you can grow perfect crops that yield cloth, food, and scrap.

---

## 🌿 Farming 2.0 Basics

### Getting Started

| Step | Action |
|:-----|:-------|
| 1 | Craft a **Planter Box** (or Large Planter) — 2 wood + 1 metal frag per small box |
| 2 | Craft a **Water Jug** — 5 metal frags (holds 5,000 mL) |
| 3 | Find seeds: loot barrels, crates, or harvested plants |
| 4 | Craft a **Gardening Glove** — 2 cloth (check genetics) |
| 5 | Find water source (river, ocean — but ocean water is salty!) |

### Plant Types

| Plant | Grown From | Yield | Use |
|:------|:-----------|:------|:----|
| Corn 🌽 | Corn seed | Corn | Food, ethanol (fuel) |
| Pumpkin 🎃 | Pumpkin seed | Pumpkin | Food, explosives (sulfur processing) |
| Hemp 🌿 | Hemp seed | Cloth | Clothing, bandages, medical syringes |
| Potato 🥔 | Potato seed | Potato | Food, vodka |
| Blueberry 🫐 | Blueberry seed | Blueberries | Food, dye |
| Tomato 🍅 | Tomato seed | Tomatoes | Food, cooking ✓ 1.0 |

> 🏆 **Priority crop:** Hemp. Cloth is needed for everything — bandages, gear, weapons.

---

## 🧬 Plant Genetics (The Core System)

### Gene Types

| Gene | Icon | Effect |
|:-----|:-----|:--------|
| **G** (Growth) | 🌱 | Speed of growth (G1 = slow, G6 = fast) |
| **Y** (Yield) | 🏆 | Number of items per harvest (Y1 = 1, Y6 = 6+) |
| **H** (Hardiness) | 🛡️ | Resistance to disease (H1 = fragile, H6 = immune) |
| **W** (Water) | 💧 | Water efficiency (W1 = thirsts fast, W6 = sips) |

### Gene Values

| Value | Label | Color |
|:------|:------|:------|
| 1 | Poor | Red |
| 2 | Below avg | Orange |
| 3 | Average | Yellow |
| 4 | Good | Green |
| 5 | Great | Teal |
| 6 | Perfect | Purple |

### How Genetics Work

- Each plant has **4 genes**: G, Y, H, W
- Each gene is 1–6
- **Cross-breeding:** Plant two different plants next to each other → new seed spawns near them with mixed/parent genes
- **Cloning:** Once you have a perfect plant, use a **Gardening Glove** (right-click) to clone it — produces identical seeds

---

## 🌽 Cross-Breeding Strategy

### Getting to GGGG YYYY HHHH WWWW (Perfect 6s)

| Phase | Goal | Method |
|:------|:-----|:--------|
| 1 | Harvest seeds from wild plants | Break boxes, loot crates |
| 2 | Plant 4+ plants in a row | Spacing: 1 block between each |
| 3 | Check genetics with glove | Note G/Y/H/W for each |
| 4 | Pair best G + best G | Plant best-G plants next to best-Y plants |
| 5 | Pair best H + best Y | Cross-pollinate to get high Y+H |
| 6 | Clone the best | Once you get multiple 5s/6s, clone that plant |

### Cross-Breeding Grid (4×4)

```
    Col 1    Col 2    Col 3    Col 4
Row 1  [P1]     [P2]     [P3]     [P4]
Row 2  [P5]     [P6]     [P7]     [P8]
Row 3  [P9]     [P10]    [P11]    [P12]
Row 4  [P13]    [P14]    [P15]    [P16]
```

**Rule:** Only adjacent plants cross-pollinate (N, S, E, W). Diagonals don't count.

### Optimal Gene Targets By Crop

| Crop | Priority Genes | Why |
|:-----|:---------------|:----|
| Hemp | G6, Y6, H4+, W4+ | Cloth yield = Y gene × base yield |
| Corn | Y6, G4+, W6+ | Maximum ethanol fuel output |
| Pumpkin | Y6, H6, W4+ | Grows in poor conditions, max yield |
| Potato | Y6, G6 | Fast food production |
| Blueberry | Y6, G4+ | Dye + food |

---

## 💧 Watering Guide

### Water Needs Per Stage

| Stage | Water per Tick (mL) | Total per Grow |
|:------|:--------------------|:---------------|
| Seedling | 4 mL/tick | ~200 mL |
| Growing | 8 mL/tick | ~600 mL |
| Mature | 6 mL/tick | ~400 mL |
| Fruiting | 10 mL/tick | ~800 mL |
| **Total** | | **~2,000 mL per plant** |

### Water Sources

| Source | Quality | Salt? | Best Use |
|:-------|:--------|:------|:---------|
| Rainwater | 100% | No | Purest. Use sprinklers with raincatcher |
| River | 50% | No | OK for manual farming |
| Groundwater (well) | 80% | No | Good for greenhouses |
| Ocean | 0% | Yes | **Kills plants** — never use! |
| Water barrel (filled) | Varies | Depends on source | Filter first with water purifier |

### Sprinkler Setup

| Sprinkler Type | Coverage | Water per Min | Notes |
|:---------------|:---------|:--------------|:------|
| Old sprinkler | 5×5 area | 200 mL/min | Free from barrels |
| Advanced sprinkler | 9×9 area | 500 mL/min | Crafted, more expensive |

> 💡 **Pro Tip:** Build a **water catcher + pump + sprinkler** system. 1 rain catcher + 1 electrical water pump + 4 sprinklers covers a 12-plot planter box setup.

---

## 🧪 Fertilizer & Soil

### Fertilizer Types

| Fertilizer | Effect | Crafting |
|:-----------|:--------|:---------|
| **Fertilizer** (basic) | +20% growth speed | 3 feces + 1 wood → composter for 2 min |
| **Compost** | +10% all stats | 5 veggies + 1 wood → composter for 5 min |
| **Tea** | +30% growth speed | 1 blueberry + 1 hemp + 1 water |
| **Engine oil** | +50% growth (but kills taste) | Loot only — don't waste |

### Compounder Strategy

The **Composter** turns waste plants into fertilizer:

1. Collect all failed genetics plants and overripe plants
2. Put them in composter (10 plants at a time)
3. Wait 2 minutes → collect fertilizer
4. Apply to planter box before planting seeds

### Soil Tiers

| Tier | How to Get | Effect |
|:-----|:-----------|:-------|
| Dirt (default) | Any ground | No bonus |
| Fertilized soil | Apply fertilizer to planter | +20% to all growth stats |
| Rich soil | 3× fertilizer applications | +50% growth + disease immunity |

---

## 🏭 Automated Greenhouse Design

### Solar-Powered Greenhouse

| Component | Quantity | Function |
|:----------|:---------|:---------|
| Large planter boxes | 2 | 18 plant slots total |
| Advanced sprinklers | 2 | Auto-water (9×9 coverage) |
| Water pump | 1 | Pulls from rain catcher |
| Rain catcher | 2 | Passive water collection |
| Solar panel | 2 | Powers pump + sprinklers |
| Battery | 1 | Night-time backup |
| Electrical wires | ~10 | Connect everything |
| Roof glass | 4×4 | Let sunlight through (greenhouse effect) |

### Automation Sequence

```
Rain → Catcher → Pump → Sprinkler → Planter → Harvest → Composter → Fertilizer → Repeat
```

### Harvest Timer

| Crop | Time (no fertilizer) | Time (with fertilizer) | Manual speed |
|:-----|:--------------------|:----------------------|:-------------|
| Corn | 2 hours | 90 min | OK |
| Hemp | 2.5 hours | 1.5 hours | **Slow — automate!** |
| Pumpkin | 3 hours | 2 hours | Medium |
| Potato | 1.5 hours | 1 hour | Fast |
| Blueberry | 2 hours | 1.25 hours | Medium |

---

## 📊 Crop Profit Analysis

| Crop | Base Yield | Max Yield (Y6) | Base Cloth/Item | Scrap Value (Approx) |
|:-----|:-----------|:---------------|:----------------|:---------------------|
| Hemp | 5 cloth | 30 cloth | 3 cloth | 25–40 scrap per stack |
| Corn | 8 ears | 48 ears | 0 | 5–10 scrap (ethanol) |
| Pumpkin | 5 pumpkins | 30 pumpkins | 0 | 10–15 scrap (sulfur) |
| Potato | 6 potatoes | 36 potatoes | 0 | 5 scrap (food duty) |
| Blueberry | 4 berries | 24 berries | 0 | 10 scrap (dye) |

### Best Money Crop

| Rank | Crop | Why |
|:-----|:------|:----|
| 1 | **Hemp (Y6, G6, W6)** | Cloth is a base necessity. Sell for scrap |
| 2 | **Corn (Y6, W6)** | Ethanol = fuel. Fuel = boom + transport |
| 3 | **Pumpkin (Y6, H6)** | Grow anywhere, max yield |
| 4 | Potato | Fast food for health |
| 5 | Blueberry | Niche. Only for dye |

---

## 🚨 Common Farming Mistakes

| Mistake | Consequence | Fix |
|:--------|:------------|:-----|
| Using ocean water | Plant dies in 10 seconds | River or rain catcher only |
| Overwatering | Roots rot, yield -50% | Check soil moisture with glove |
| Underwatering | Wilting, yield -80% | Sprinkler timer every 30 min |
| Poor genetics | Crop yields 1 item per harvest | Cross-breed aggressively |
| No fertilizer | 50% slower growth | Keep composter running |
| Planting in dark (base interior) | Plant doesn't grow | Needs a skylight window (glass roof) |
| Ignoring disease | All plants die overnight | Check H gene — ≥H4 prevents most disease |
