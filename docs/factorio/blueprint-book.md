---
title: "Factorio Blueprint Book"
description: "Essential blueprints — smelting arrays, rail intersections, defense perimeters, science blocks, and sharing tips."
date: 2026-07-06
tags: [Factorio, blueprints, design]
---

## Blueprint Basics

Open library with **B**, create with **Alt+B** (drag selection), place by clicking. Import/export strings for sharing.

| Action | Key | Notes |
|--------|-----|-------|
| Open library | B | All saved blueprints |
| Create | Alt+B + drag | Entities, tiles, modules |
| Place | Click on ground | Ghosts → bots build |
| Import | Click "Import string" | Cross-session sharing |
| Export | Right-click → "Export" | Share on FactorioPrints |

## Smelting Arrays

### 48 Furnace Array (Early)

24+24 split feed from a red belt. Use long-handed inserters on output. Power poles every 4 furnaces. Upgrade stone → steel → electric in the same footprint.

### Beaconed Electric (End-game)

8 Speed 3 beacons around 4 electric furnaces with Prod 3 modules. Each furnace produces ~3× output with 30% less ore. Blue belt (2,700/min) per 4 furnaces.

### Steel Smelting

Ratio 5:1 (iron smelters : steel smelter). Use direct insertion. 48 iron furnaces → 12 steel furnaces = 1 red belt of steel (900/min).

## Rail Intersections

### 4-Way Intersection

**Chain signal** on every entrance, **Path signal** on straight paths, **Block signal** on exits. Size: 4×4 chunks. Throughput: 16+ trains/min.

### T-Junction

Same signaling. Size: 3×3 chunks. Add chain signals between junction segments.

### Train Stacker

6 parallel bays, each long enough for your longest train. Chain signal at bay inputs. Only one train exits at a time.

## Defense Blueprints

### Perimeter Segment (12 tiles)

```
[Dragon's teeth × 2] → [Wall × 3] → [Mines × 1]
|Gun|[Flame]|Gun|[Flame]|Gun|
[Laser row] [Backup wall] [Ammo belt + oil pipe] [Roboport × 15 tiles]
```

Place end-to-end for full perimeter coverage.

### Artillery Outpost

6 cannons + 10 uranium guns + 4 flamethrowers + 20 lasers + 4 wall layers + train station + roboport.

## Science Blocks

### 60 SPM Dimensions

| Science | Size | Inputs |
|---------|------|--------|
| Red | 12×8 | 5 iron, 2 copper |
| Green | 16×12 | 15 iron, 5 copper |
| Gray | 16×14 | 5 iron, 2 coal, 2 copper |
| Blue | 24×20 | 15 iron, 20 copper, 30 oil |
| Purple | 24×24 | 30 iron, 10 plastic |
| Yellow | 30×24 | 20 iron, 20 copper, 10 plastic |

Tile the same block for 120/240/480 SPM. Feed all blocks from one main bus.

## Blueprint Sharing

### Best Resources

| Site | Best For |
|------|----------|
| FactorioPrints.com | Largest collection |
| Factorio.school | Interactive viewer |
| Reddit r/factorio | Weekly bp threads |
| KatherineOfSky | Megabase designs |
| Nilaus Master Book | Complete megabase set |

### Version Notes

| Version | Changes |
|---------|---------|
| 0.17 | First library system |
| 1.0-1.1 | Stable — all previous work |
| 2.0 | Elevated rails, quality modules |

Always check version compatibility. 1.1 blueprints work in 2.0 but won't use new features.
