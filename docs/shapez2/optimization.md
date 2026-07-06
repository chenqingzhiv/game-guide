---
title: "Shapez 2 Optimization Guide — Throughput, Balancers & Blueprint Architecture"
description: "Complete Shapez 2 optimization guide. Belt throughput optimization, balancer designs (4-to-4, 8-to-8), compact blueprint archetypes, bus architecture, stacker patterns, and endgame throughput scaling."
date: 2026-07-06
tags: [Shapez 2, optimization, guide, throughput]
---

# ⚡ Shapez 2 Optimization Guide

*Last updated: July 2026 | Game version: Early Access (Steam)*

---

Shapez 2 is about scaling — building factories that produce hundreds of shapes per minute with minimal space and belt spaghetti. This guide covers belt throughput, balancer designs, compact blueprints, and architecture patterns for endgame automation.

---

## Belt Throughput Basics

### Belt Speed Tiers

| Belt Tier | Shapes/Second | Shapes/Minute | Unlocked By |
|:----------|:--------------|:--------------|:------------|
| Basic Belt | 15/s | 900/m | Start |
| Fast Belt | 30/s | 1,800/m | Milestone 8 |
| Express Belt | 45/s | 2,700/m | Milestone 16 |
| **Max Belt** | **60/s** | **3,600/m** | Milestone 24 |

### Throughput Rules

```
Rule 1: Never merge beyond belt capacity.
  - Two belts at 30/s each → merging requires Express Belt (60/s max)
  - Merging two 45/s belts is impossible without upgrading belts

Rule 2: Balance before processing arrays.
  - Any array of 4+ machines needs a proper balancer on input
  - Without balancing, the first machine starves while the last idles

Rule 3: Upgrade belts in tiers.
  - Replacing all belts at once is expensive
  - Upgrade the main bus first, then branches, then individual lines
  - Express belts are only needed for the final 60/s push
```

---

## Belt Balancers

Balancers ensure that every input in a multi-belt system gets equal throughput, regardless of which belts are backed up.

### 4-to-4 Balancer (Compact)

```
     Input A    Input B    Input C    Input D
        │           │          │           │
        ▼           ▼          ▼           ▼
    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
    │ Split  │ │ Split  │ │ Split  │ │ Split  │
    └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
        │          │          │           │
        ├────┬─────┤          ├─────┬─────┤
        │    │     │          │     │     │
        ▼    ▼     ▼          ▼     ▼     ▼
    ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
    │ Merge  │ │ Merge  │ │ Merge  │ │ Merge  │
    └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
        │          │          │           │
        ▼          ▼          ▼           ▼
     Output A    Output B    Output C    Output D
```

**Build pattern:** Split all 4 inputs → cross-connect to 4 mergers → each output receives 1/4 of each input.

### 8-to-8 Balancer (Tileable)

```
Recommended design:
  1. Split all 8 inputs into 16 lines
  2. Cross-connect in pairs to 8 mergers
  3. Each output gets 1/8 of total input

Tiles: 8 wide × 6 long = 48 tiles
```

### N-to-1 Balancing

For feeding a single high-demand line:

```
Setup: Multiple inputs → load balancer → single output belt

If 3 inputs at 30/s feed 1 belt (max 60/s):
  - You need only 2 balanced inputs (2 × 30 = 60)
  - A 3-to-1 balancer: split one input, merge with the other two, discard excess
  
Better: balance all 3 inputs into 2 outputs (3:2 balancer) then merge those 2.
```

### When to Use Balancers

| Situation | Balancer Type | Why |
|:-----------|:--------------|:-----|
| Input to 4 identical processors | 4-to-4 | Each machine gets equal throughput |
| Loading a 8-belt main bus | 8-to-8 | Balanced lane use prevents bottlenecks |
| Unloading production arrays | Reverse balancer | Ensures all machines output evenly |
| Multiple mining patches → base | N-to-M | Handles uneven ore patch output |
| Any processing array of 3+ | Always balance | Without balance: first machine starved |

---

## Stacker Optimization

Stackers combine shapes. The order and positioning of stackers determines your throughput.

### Stacker Sandwich Technique

```
Standard approach (1 stacker):
  Shape A ──► Stacker ──► Shape A+B
  Shape B ──►          (1x throughput)

Sandwich approach (2 stackers, parallel):
  Shape A ──► Split ─┬─► Stacker1 ─┬─► Shape A+B
  Shape B ──► Split ─┤             │
                     ├─► Stacker2 ─┤
                     └─►          Merge ──► 2x throughput
```

### Quad-Stacker (4x Throughput)

For high-volume shape requirements (e.g., crystals for milestones):

```
Input A (60/s) ──► 4-way Split ─┬─► Stacker 1 ─┬─► Merge 1
Input B (60/s) ──► 4-way Split ─┤              │
                                ├─► Stacker 2 ─┤
                                │              ├─► Merge 2 → Output (60/s)
                                ├─► Stacker 3 ─┤
                                │              │
                                └─► Stacker 4 ─┘
Throughput: 4 stackers × 15/s each = 60/s (capped by belt)
```

### Stacker Priority

| Stacker Setup | Space (tiles) | Throughput | Best For |
|:--------------|:--------------|:-----------|:---------|
| Single stacker | 2×3 | 15/s | Early game, low volume |
| Stacker sandwich (2) | 4×4 | 30/s | Mid-game |
| Quad-stacker (4) | 8×6 | 60/s | Endgame high demand |
| Octo-stacker (8) | 16×8 | 120/s (dual belts) | Mega-factory only |

---

## Bus Architecture

A main bus carries all your shapes through a central highway. Production modules tap off what they need.

### 8-Belt Main Bus Layout

```
          Production Modules
                 │
    ┌────────────┼────────────┐
    │  Belt 1:  │ Shape A (raw)  │
    │  Belt 2:  │ Shape B (raw)  │
    │  Belt 3:  │ Shape C (raw)  │
    │  Belt 4:  │ Shape AB (stacked) │
    │  Belt 5:  │ Shape AC (stacked) │
    │  Belt 6:  │ Shape BC (stacked) │
    │  Belt 7:  │ Shape ABC (complex)│
    │  Belt 8:  │ Painted shapes     │
    └────────────┴────────────────────┘
                 │
          Bus lanes
     (all running same direction)
```

### Tapping the Bus

```
For each production module:

  1. Split one belt from the bus (using Splitter)
  2. Process the shapes (stack, paint, cut)
  3. Merge processed shapes back onto the bus

  Never tap a bus belt with 100% of its throughput.
  Always leave 20% headroom on main bus lanes.
  Tap from the RIGHT side of the bus (keep left clear).
```

### Bus Lane Allocation

| Game Stage | Bus Width | Content |
|:-----------|:----------|:--------|
| Early (M1-8) | 2-4 belts | Raw shapes only |
| Mid (M9-16) | 4-6 belts | Raw + simple stacks |
| Late (M17-24) | 6-8 belts | Raw + stacks + painted |
| Endgame (M25+) | 8-12 belts | Full complexity range |

```
💡 Bus tip: Use the "lane balancer" module every 20 tiles on the bus
to rebalance lanes. Uneven consumption will slowly drain one belt
while another overflows. A 4×2 balancer every 20 tiles fixes this.
```

---

## Blueprint Archetypes

### The Universal Processor (10×10 tiles)

```
┌──────────────────────────┐
│  INPUT ──► Splitter      │
│              │           │
│        ┌─────┴─────┐    │
│    Belt A        Belt B  │
│        │           │     │
│  ┌─────────┐ ┌─────────┐│
│  │Stacker  │ │Painter  ││
│  └────┬────┘ └────┬────┘│
│       │           │      │
│        └────┬─────┘      │
│             │            │
│         ┌───▼───┐       │
│         │ Merger│       │
│         └───┬───┘       │
│             │           │
│  OUTPUT ────┘           │
└──────────────────────────┘

Throughput: 15-30/s depending on belt upgrade
Best for: Any shape that needs stacking + painting
```

### Compact Stacker Block (6×6 tiles)

```
┌────────────────┐
│  A ──► SPLIT ──┤
│           │    │
│  B ──► ──┤    │
│           ▼    │
│       STACKER  │
│           │    │
│        ┌──▼──┐ │
│        │MERGE│ │
│        └──┬──┘ │
│     ┌───┐ │    │
│     │OUT │◄────┘
│     └───┘      │
└────────────────┘

Input: 2 belts (30/s each) → output: 1 belt (60/s after stacking)
```

### Painter Block (8×4 tiles)

```
┌──────────────────────────┐
│  Shape In ──► Splitter   │
│                  │        │
│           ┌──────┴──┐    │
│      Paint A     Paint B  │
│           │          │    │
│           └────┬─────┘    │
│                │          │
│           ┌────▼────┐    │
│           │  Merger  │    │
│           └────┬─────┘    │
│                │          │
│       Shape Out (colored) │
└──────────────────────────┘

Paint A and Paint B alternate colors on the output belt.
For 4 colors: chain two of these blocks.
```

---

## Endgame Throughput Strategy

### Milestone 24+ Optimization

At endgame, you need 60/s throughput on complex shapes. Here's how:

```
1. Parallel processing arrays
   - 8 processing lines in parallel for each complex shape
   - Each line: 4 stackers + 2 painters = 6 machines
   - Total: 48 machines per complex shape

2. Dedicated resource lines
   - Each raw shape gets its own 60/s belt
   - 4 mining outposts per raw shape type
   - Direct feeds (no bus) for highest-demand shapes

3. Output balancing
   - Every block of 4 machines gets a 4-to-4 balancer
   - Output merges to 2 Express belts (120/s total)
   - Feed directly into Hub input
```

### Throughput Math for Endgame

| Component | Max Throughput | Limiting Factor |
|:----------|:--------------|:----------------|
| Single belt | 60/s | Belt speed cap |
| Single stacker | 15/s | Machine speed cap |
| Stacker array (4) | 60/s | Belt input limit |
| Painter | 30/s | Faster than stackers |
| Crystal mixer | 15/s | Machine speed cap |
| Hub input | 120/s (2 belts) | Hub belt slot limit |

### Unlocking Full Potential

```
To reach 60/s on complex shapes:
  1. Upgrade all belts to Express (60/s)
  2. Build quad-stackers for each stacking step
  3. Use parallel painting lanes (2 painters per color)
  4. Balance EVERYTHING with 4-to-4 balancers
  5. Feed the Hub with 2 belts (left + right input)
  
Total footprint: ~100×150 tiles for one full-complexity shape line
```

---

## Color Mixing Optimization

### Compact Color Wheel (12×12 tiles)

For efficient crystal/color production:

```
          Crystal In (60/s)
               │
         4-way Splitter
       ┌────┬──┴──┬────┐
       │    │     │    │
       ▼    ▼     ▼    ▼
     ┌──┐ ┌──┐ ┌──┐ ┌──┐
     │R │ │G │ │B │ │W │
     └┬─┘ └┬─┘ └┬─┘ └┬─┘
      │    │     │    │
      └────┼─────┼────┘
           ▼     ▼
        ┌────┐ ┌────┐
        │Mix1│ │Mix2│  ← Create secondary colors
        └──┬─┘ └──┬─┘
           │      │
           └──┬───┘
              ▼
           ┌───────┐
           │ OUTPUT│ 60/s max
           └───────┘
```

### Paint Efficiency

| Paint Type | Shapes Painted | Crystal Cost Per Shape |
|:-----------|:---------------|:----------------------|
| Single color | 1 shape | 1 paint unit |
| Striped (2-color) | 1 shape | 2 paint units |
| Checkered (4-color) | 1 shape | 4 paint units |
| Gradient (8-color) | 1 shape | 8 paint units |

**Pro tip:** Always produce the minimum color variety needed. If a shape only needs red and blue, don't produce the full rainbow — it wastes crystal throughput.

---

## Blueprint Library Essentials

Save these 5 blueprints for rapid expansion:

| Blueprint | Size | Purpose |
|:----------|:-----|:---------|
| 4-to-4 Balancer | 4×6 | Universal balancing |
| Quad-Stacker | 8×6 | 60/s stacking |
| Compact Painter | 8×4 | 2-color painting |
| Universal Processor | 10×10 | Stack + Paint module |
| Dual Hub Feeder | 4×8 | 120/s hub input |

---

## Common Bottlenecks & Fixes

| Symptom | Cause | Fix |
|:--------|:------|:----|
| Machines idle randomly | Unbalanced input | Add a 4-to-4 balancer |
| Belt backed up but machines starved | Wrong merge order | Stack before merging, not after |
| Stackers at 15/s while belts are 60/s | Single stacker bottleneck | Build quad-stacker array |
| Hub not accepting full throughput | Only 1 input belt used | Split to both Hub inputs |
| Painters skipping shapes | Paint supply empty | Add paint buffer chest |
| Complex shape output below 30/s | Crystal bottleneck | Upgrade crystal mixer to quad |

> *All throughput numbers based on Shapez 2 Early Access (Steam, v0.x). Belt speeds and machine rates may change with updates. Always verify in sandbox mode before committing to a build.*
