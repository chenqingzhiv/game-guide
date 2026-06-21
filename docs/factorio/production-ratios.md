---
title: "Factorio Production Ratios Guide — Factory Game Guides"
description: "Exact production ratios for Factorio 2.0. Science per minute, belt capacity, module effects and more. Build the perfect factory."
---

# 📐 Factorio Production Ratios Guide

The beauty of Factorio is that **everything can be calculated exactly**. No RNG, no guesswork — just math. Here are the essential ratios you need.

---

## 🔢 Basic Ratios Reference

### Power Generation

| Setup | Ratio | Notes |
|:------|:------|:------|
| **Steam** | 1 Offshore Pump : 20 Boilers : 40 Steam Engines | Max 60 MW per offshore pump |
| **Nuclear** | 1 Reactor : 4 Heat Exchangers : 7 Steam Turbines | +100% neighbor bonus per adjacent reactor |
| **Solar** | 0.84 Accumulators per Solar Panel | For 24h continuous power |

### Smelting

| Input | Output | Electric Furnace | Steel Furnace |
|:------|:-------|:-----------------|:--------------|
| **Iron Ore → Iron Plate** | 1 per 3.2s | 1 furnace : 48 ore/min | 1 furnace : 31.5 ore/min |
| **Copper Ore → Copper Plate** | 1 per 3.2s | Same as iron | Same as iron |
| **Iron Plate → Steel** | 1 per 16s | 5 iron furnaces : 1 steel furnace | 5 iron : 1 steel |

### Green Circuits

**Assembly Machine 2:** 3 Copper Wire : 2 Green Circuit — 1 copper wire assembler feeds 1.5 green circuit assemblers

```
3 Copper Wire → 2 Green Circuit
Ratio: 3 Wire AMs : 2 Green Circuit AMs
```

### Red Circuits

**Assembly Machine 3 with Speed Module 1:**  
4 Plastic : 4 Copper Wire : 1 Green Circuit → 2 Red Circuits

```
2 Copper Wire : 1 Green Circuit : 1 Plastic → 1 Red Circuit
```

---

## 📊 Science Per Minute (SPM) Design Targets

Target figures per **100 SPM** with Assembler 3 + Speed 3 in all buildings:

| Science | Input/min | Building Count | Key Resource/min |
|:--------|:----------|:---------------|:-----------------|
| 🟥 **Automation** | 100 | 1 AM3 + 1 Gear AM3 | 200 Iron |
| 🟩 **Logistic** | 100 | 2 AM3 (inserters+belts) | 150 Iron + 40 Copper |
| 🟦 **Military** | 100 | 2 AM3 | 250 Iron + 50 Copper |
| ⚗️ **Chemical** | 100 | 3 AM3 | 300 Oil + 200 Iron |
| 🟪 **Production** | 100 | 2 AM3 + 2 Electric Furnace | 400 Iron + 300 Copper |
| 🟨 **Utility** | 100 | 3 AM3 | 250 Copper + 100 Plastic |
| 🔵 **Space** | 100 | 3 AM3 + Rocket Silo | 500 Copper + 300 Steel |

> 💡 **Rule of thumb:** 100 SPM = ~1 full red belt of iron + ~1 full red belt of copper.

---

## 🏗️ Belt Throughput

| Belt Type | Items/min (single lane) | Items/min (both lanes) | Upgrade cost |
|:----------|:-----------------------|:----------------------|:-------------|
| **Yellow** | 900 | 1,800 | Starting belt |
| **Red** | 1,800 | 3,600 | 1 Iron gear + 4 plates |
| **Blue** | 2,700 | 5,400 | 1 Lubricant + 5 Iron gear + 10 plates |

---

## ⚡ Module Efficiency

| Module | Speed | Productivity | Energy | Best Used For |
|:-------|:------|:-------------|:-------|:--------------|
| **Speed 3** | +50% | — | +70% | Miners, Pumps — more output from same patch |
| **Productivity 3** | -15% | +10% | +80% | Assemblers, Refineries — free items (must use Speed on beacons) |
| **Efficiency 3** | — | — | -80% | Early power-limited bases, biters near pollution |

**Pro tip:** A single Speed 3 beacon (+50% to 8 surrounding buildings) is more UPS-efficient than Speed 3 in each building. Use **8-beacon** or **12-beacon** layouts for megabases.

---

## 🚛 Logistics Bot Ratios

| Bot Type | Speed | Capacity | Cargo/min (2 roboports) |
|:---------|:------|:---------|:------------------------|
| **Logistic** | 3 tiles/s | 3 items | ~540 |
| **Construction** | 3.6 tiles/s | 4 items | ~864 |
| **Logistic 2** (follower) | 5.5 tiles/s | 4 items | ~1,320 |
| **Logistic 3** | 7.8 tiles/s | 5 items | ~2,340 |

**Roboport coverage:** 50×50 tiles logistic, 110×110 tiles construction.  
**Network recommendation:** Max 1-2 roboports wide for high-throughput lines.

---

## 📍 Blueprint References

| Blueprint | Link |
|:----------|:------|
| 8-beacon Green Circuit (1000+/min) | [factorioprints.com](https://factorioprints.com) |
| 1-4 Train Station | [factorioprints.com](https://factorioprints.com) |
| 1M+ SPM Megabase Starter | [factorioprints.com](https://factorioprints.com) |

---

> 🛒 [**Buy Factorio on Steam**](https://store.steampowered.com/app/427520/)
>
> *Ratings verified against Factorio 2.0 and official Wiki. Module ratios are for Quality 1 modules.*
