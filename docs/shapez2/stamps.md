---
title: "Shapez 2 Stamps & Blueprint System Guide"
description: "Master the Shapez 2 stamp system — reusable blueprints, stamp dimensions, mirroring, and advanced layout patterns."
---

# 📐 Shapez 2 Stamps & Blueprint System Guide

Stamps are one of Shapez 2's most powerful features. They allow you to **save and reuse** production layouts — think of them as blueprints. Instead of rebuilding the same dye factory 10 times across the map, you design it once, save it as a stamp, and **paste** it anywhere.

> **Data source:** Shapez 2 in-game manual v0.9.0 — Last verified: July 2026

---

## What Are Stamps?

Stamps are **reusable production templates** that save the position, rotation, and settings of all buildings and belts in a selected area. Unlike Shapez 1 where every build was manual, Shapez 2's stamp system lets you:

- ✅ Copy an entire factory section with one click
- ✅ Mirror layouts horizontally or vertically
- ✅ Chain stamps together for complex production lines
- ✅ Share stamp designs as codes (text-based)
- ✅ Upgrade stamps with MK2/MK3 buildings without redesign

---

## Stamp Size & Grid

Every stamp occupies a rectangular area on the grid. The size is measured in **tiles** (studs).

### Size Limits

| Stamp Type | Max Width | Max Height | Best For |
|:-----------|:----------|:-----------|:---------|
| **XS Stamp** | 8 tiles | 8 tiles | Compact modules: Painters, single Mixers |
| **S Stamp** | 16 tiles | 16 tiles | Processors + mixers, small production chains |
| **M Stamp** | 32 tiles | 32 tiles | Full color factories, stamp-based sorting |
| **L Stamp** | 64 tiles | 64 tiles | Large production lines, hub delivery systems |
| **XL Stamp** | 128 tiles | 128 tiles | Megafactory modules (late game) |

> **Tip:** Start with S and M stamps for most practical builds. XL stamps are useful for late-game megafactories but cumbersome to modify.

---

## How to Create & Use Stamps

### Creating a Stamp

1. Select the **Stamp tool** (hotkey: `T`)
2. Click and drag to select the area you want to save
3. Name your stamp (e.g., "Yellow Dye Factory")
4. The stamp is saved to your **stamp library**

### Placing a Stamp

1. Open the **stamp library** (hotkey: `G`)
2. Select a saved stamp
3. Click to place it on the map
4. All buildings, belts, and settings are instantly recreated

### Mirroring

| Mirror Mode | Key/Button | Use Case |
|:------------|:-----------|:---------|
| **Horizontal** | `H` or Mirror icon | Symmetric layouts, parallel production |
| **Vertical** | `V` or Mirror icon | Stacked designs, vertical belt routing |
| **None** | Default | Asymmetric but efficient layouts |

**Critical detail:** When you mirror a stamp, **belt directions and building rotations** are also mirrored. Test mirrored stamps with items flowing before committing to a layout.

---

## Essential Stamp Designs

### 1. Color Production Stamp (8×8)

A compact module producing one secondary color from two primary crystals:

```
Size: 8×8
Inputs: 2× Crystal belts
Output: 1× Colored dye belt

[Miner] → [Processor] → [Mixer] → [Output]
[Miner] → [Processor] → 
```

Use this stamp for **Yellow**, **Cyan**, and **Purple**. Chain 3 of these to cover all secondary colors from 6 crystal mines.

### 2. Full Color Factory Stamp (24×24)

Produces **8 colors** from 4 crystal inputs:

```
Inputs: White, Red, Green, Blue crystals
Outputs: Yellow, Cyan, Purple, Orange, Pink, Lime, Teal, Black

┌──────────────────────────────────────┐
│  [W→Proc] → Mix(W+R→Pink)           │
│  [R→Proc] → Mix(R+G→Yell) → Mix→Ora │
│  [G→Proc] → Mix(G+B→Cy) → Mix→Purp  │
│  [B→Proc] →           → Mix→Black    │
└──────────────────────────────────────┘
```

### 3. Compact Sorting Stamp (6×4)

Routes specific colored shapes to specific outputs:

```
Size: 6×4
Input: Mixed colored shape belt
Outputs: 4× sorted shape belts

[Filter(W)] → [Filter(R)] → [Filter(G)] → [Filter(B)]
```

---

## Stamp Sharing Codes

Shapez 2 stamps can be **exported as text codes** and shared with other players:

```
Export: Stamp Library → Right-click stamp → "Export Code"
Import: Stamp Library → "Import Code" → Paste code
```

Codes are compact alphanumeric strings representing the entire layout. They include:
- All building types and positions
- Belt directions and lengths
- Building settings (paint colors, filter types, etc.)
- Stamp name and metadata

> **Community tip:** The r/shapez subreddit and Discord have dedicated stamp-sharing channels with hundreds of pre-built designs.

---

## Advanced Stamp Techniques

### Chaining Stamps

Place stamps so their inputs/outputs align:

```
[Stamp A: Crystal Mine] 
    → [Stamp B: Processor]
        → [Stamp C: Mixer, Painter]
            → [Stamp D: Stacker]
```

Use **Grid Snapping** (toggle with `G` while placing) to ensure perfect alignment between stamps.

### Stamp Templates

Create **templates** — variants of a base stamp optimized for different colors:

1. Design a generic "Painter Module" stamp
2. Save it as a template with **parameterized color input**
3. Place the stamp, then set the target color per instance

This is the most efficient approach for large-scale shape production.

### Upgrading Stamps to MK2/MK3

When you unlock MK2 buildings, your existing stamps **don't automatically upgrade**. You must:

1. Place the stamp on the map
2. Manually upgrade each building (or use the upgrade tool)
3. Re-save the stamp if you want the upgraded version for future use

**Pro tip:** Keep a "stamp workshop" area where you refine stamps before saving them permanently.

---

## Stamp Library Management

| Task | How To |
|:-----|:-------|
| **View all stamps** | `G` → Opens stamp library |
| **Delete a stamp** | Right-click → Delete |
| **Rename a stamp** | Right-click → Rename |
| **Export stamp** | Right-click → Export Code |
| **Import stamp** | Import Code → Paste string |
| **Organize stamps** | Prefix names: `[Color]`, `[Logic]`, `[Mine]` |

### Recommended Naming Convention

```
[CATEGORY] - [PRODUCT] - [SIZE]
Examples:
[Color] - Yellow Dye - S
[Color] - Full Rainbow - M  
[Logic] - AND Gate Module - XS
[Mine] - Quad Miner - S
[Sort] - 4-Way Color Sorter - S
```

---

## Common Stamp Mistakes

| Mistake | Problem | Fix |
|:--------|:--------|:----|
| ❌ **Incomplete selection** | Missing belts or buildings | Double-check your drag selection |
| ❌ **Wrong orientation** | Mirrored belts run backwards | Place stamp → test with items → undo if wrong |
| ❌ **Overlapping stamps** | Belt conflicts at boundaries | Leave 1-2 tile gaps between stamps |
| ❌ **No input labeling** | Can't remember what goes where | Add colored belts or signs near inputs |
| ❌ **Stamps too large** | Hard to place in tight spaces | Prefer S/M stamps over L/XL |

---

## Stamp-Based Factory Architecture

For endgame factories, design your layout as interconnected stamps:

```
Production Zones (each = 1 stamp cluster):
  
  [Crystal Mining]        ← L stamp cluster with 8+ miners
        ↓
  [Basic Processing]      ← M stamp: Processors → sorted outputs
        ↓
  [Dye Production]        ← M stamp: 8 color outputs
        ↓  
  [Shape Assembly]        ← L stamp: Cutters + Mergers + Painters
        ↓
  [Stacking & Delivery]   ← M stamp: Stackers → Hub input
```

This modular approach makes it easy to:
- Scale individual sections without rebuilding everything
- Identify bottlenecks (which stamp is struggling?)
- Quickly expand production when new milestones demand more output

---

> 🛒 [**Buy Shapez 2 on Steam**](https://store.steampowered.com/app/2162800/) — Support the developer!
>
> *Affiliate link — we earn a small commission at no extra cost to you.*
