---
title: "Shapez 2 Shape Synthesis Reference"
description: "Complete reference for all 16 base shapes, their combinations, and efficient shape synthesis techniques in Shapez 2."
---

# Shapez 2 Shape Synthesis Reference

Shape synthesis is the core gameplay loop of Shapez 2. You extract shape **crystals** from the map, process them into **quadrant shapes**, then combine, color, and stack those shapes into complex deliverables for the hub. This reference covers every base shape, how synthesis works, and tips for building efficient production lines.

---

## How Shape Synthesis Works

Every shape in Shapez 2 is made of **4 quadrants** (top-left, top-right, bottom-left, bottom-right), arranged in a 2×2 grid. Each quadrant has two properties:

- **Shape type** — the form the quadrant takes (e.g., circle, rectangle, star)
- **Color** — the dye applied to that quadrant (white, red, green, blue, or their secondary mixes)

Shapes can also be **stacked** into up to **4 layers**, with each layer being its own 2×2 quadrant grid. A final deliverable shape is defined by the combination of all four quadrants across all layers.

### The Synthesis Pipeline

```
Extract → Process → Cut → Combine → Color → Stack → Deliver
```

| Step | Building | What It Does |
|:-----|:---------|:-------------|
| **Extract** | Miner | Mines shape crystals from deposits on the map |
| **Process** | Crystal Processor | Converts raw crystals into shape molds usable by Cutters |
| **Cut** | Cutter | Splits a 4-quadrant shape into its individual quadrants |
| **Combine** | Merger | Merges 2+ free-form quadrants into a new 4-quadrant shape |
| **Color** | Painter | Applies dye to a shape or quadrant |
| **Stack** | Stacker | Combines two shapes into a multi-layer shape |
| **Rotate** | Rotator | Rotates a shape 90° to align quadrants |
| **Deliver** | Hub / Station | The shape is shipped to complete a milestone |

### Crystal Types & Shape Types

Raw crystals come in two varieties:

1. **Shape Crystals** — determine the *form* of your quadrants
2. **Dye Crystals** — determine the *color* of your quadrants

Each shape crystal processes into a specific **shape mold** that produces a single shape type. The 8 shape types combined with 8 dye colors (including uncolored) create the full palette of quadrant possibilities.

---

## All 16 Base Shapes & Their Combinations

The table below lists every base shape type in Shapez 2 — 8 structural types + 8 dyed variants — along with their ingredients, complexity, when you first encounter them, and what they produce.

### Structural Base Shapes

| Shape Name | Shape Type | Ingredients | Complexity | Found in Level | Produces |
|:-----------|:-----------|:------------|:-----------|:---------------|:---------|
| Circle | Quarter circle quadrant | 1× Circle Crystal | 1 (Extract + Process) | 1 | Single-layer circle shapes; basic deliveries |
| Rectangle | Square quadrant | 1× Rectangle Crystal | 1 | 1 | Single-layer rectangle shapes; basic deliveries |
| Rounded Rectangle | Pill/square with rounded corners | 1× Rounded Rect Crystal | 1 | 2 | Rounded shapes; starter compound builds |
| Triangle | Right-angle triangle quadrant | 1× Triangle Crystal | 1 | 2 | Angled quadrant fills; first cut-and-combine puzzles |
| Star | Four-pointed star quadrant | 1× Star Crystal | 1 | 3 | Decorative / milestone shapes |
| Crescent | Moon / banana curve quadrant | 1× Crescent Crystal | 1 | 3 | Curved quadrant fills |
| Fan | Quarter-circle sector quadrant | 1× Fan Crystal | 1 | 4 | Radial quadrant fills |
| Pin | Logic connector quadrant | 1× Pin Crystal | 1 | 4 | Logic / wiring shapes; advanced station unlocks |

### Dyed & Compound Shapes

| Shape Name | Ingredients | Complexity | Found in Level | Produces |
|:-----------|:------------|:-----------|:---------------|:---------|
| Red Shape | Any base shape + Red Dye | 2 (shape + paint) | 5 | Colored milestone deliveries |
| Green Shape | Any base shape + Green Dye | 2 | 5 | Colored milestone deliveries |
| Blue Shape | Any base shape + Blue Dye | 2 | 5 | Colored milestone deliveries |
| White Shape | Any base shape + White Dye | 2 | 5 | White / uncolored milestone deliveries |
| Yellow Shape | Red Dye + Green Dye → mix, then apply | 3 | 6 | Secondary color deliveries |
| Purple Shape | Red Dye + Blue Dye → mix, then apply | 3 | 6 | Secondary color deliveries |
| Cyan Shape | Blue Dye + Green Dye → mix, then apply | 3 | 6 | Secondary color deliveries |
| Two-Color Shape | 2+ different colored quadrants combined | 3–4 | 7 | Multi-color milestone shapes |

### Example Compound Shapes

| Compound Shape | Ingredients (Quadrants) | Complexity | Used In |
|:---------------|:-----------------------|:-----------|:--------|
| Circle-in-Square | 4× Circle on Layer 1 + 4× Rectangle on Layer 2 | 5 | Milestone 8–10 |
| Red Star on White Square | 4× Red Star + 4× White Rectangle (stacked) | 6 | Milestone 11–12 |
| Two-Tone Rectangle | 2× Red Rectangle (top) + 2× Blue Rectangle (bottom) | 4 | Milestone 13 |
| Crescent + Circle Pinwheel | Mixed quadrants with rotation offsets | 5–6 | Milestone 14–15 |
| Full 4-Layer Colored | 4 layers of differing shapes + colors | 10+ | End-game milestones |

---

## Shape Complexity Explained

**Complexity** is a rough measure of how many processing steps a shape requires from raw extraction to finished form:

- **Complexity 1:** Extract + Process (raw crystal → shape mold)
- **Complexity 2:** Above + Cut or Color (one operation)
- **Complexity 3:** Above + Combine and/or Mix (two operations)
- **Complexity 4+:** Multiple combines, colors, and/or stacking layers

Each complexity point typically corresponds to one building in your production line. A shape with complexity 7 will need roughly 7 processing buildings (not counting belts, mergers, or splitters).

---

## Tips for Efficient Shape Production

### 1. Extract Near Deposits, Process On-Site

Build your crystal miners directly on deposits and place Crystal Processors right next to them. Shipping raw crystals is inefficient — convert to shape molds locally, then belt the molds to your main factory.

### 2. Keep Shape & Color Separate

**Don't** color shapes unless you need to. Keep a stock of uncolored quadrants on your main bus and only paint them at the last possible step. This lets you reuse the same shape belts for multiple colored outputs.

**Better:** Produce a generic "shape bus" (all uncolored) and a separate "dye bus," then paint + combine at the delivery station.

### 3. Bus Design: 8–12 Lanes Minimum

Run at least 8–12 parallel belt lanes through your factory:

| Lanes | Contents |
|:------|:---------|
| 1–4 | The four most-used shape types (Circle, Rectangle, Triangle, Star) |
| 5–6 | Crescent + Fan (mid-late game needs) |
| 7–8 | Dyes (Red + Green + Blue + White) |
| 9–12 | Specialty shapes / overflow |

### 4. Quadrant Compression

After cutting a shape into quadrants, combine matching quadrants onto single belts with mergers. A single belt carrying "all Circle quadrants" is more useful than four separate quadrant belts.

### 5. Build Modular Blueprints

Design small, tileable blueprint modules for common operations:

- **Quadrant cutter module** — 1 Miner → 1 Processor → 1 Cutter → 4 belt outputs
- **Color module** — Input quadrant belt + Input dye belt → Painter → Output
- **Stacker module** — Input Shape A + Input Shape B → Stacker → Output
- **Quadrant combiner** — 4 input belts → 4 free-form quadrants → Merger → 1 shape

Copy-paste these as your factory grows rather than rebuilding.

### 6. Use Rotators to Align Quadrants

Many compound shapes need quadrants rotated before they combine. Rotators are cheap and fast — always place a pair (0° and 90°) before your combiners so you have both orientations available.

### 7. Upgrade Belts Early

Belt throughput is the #1 bottleneck in Shapez 2. Upgrade to faster belts as soon as they unlock. A single fast belt can replace 3–4 slow belts, dramatically simplifying your factory layout.

### 8. Layer Strategically

Stacking is expensive (it doubles your shape volume). Whenever possible:

- Combine all 4 quadrants for Layer 1 first
- Stack the completed Layer 1 with Layer 2
- Avoid stacking single quadrants — combine before stacking

### 9. Read the Target Shape

Always examine the milestone target shape carefully before building. Count the quadrants, note the colors, and identify which layers need which shapes. A few minutes of planning saves hours of rebuilding.

### 10. Accept Imperfection

Shapez 2 has no resource limits and no penalties for deleting buildings. Don't optimize prematurely — just get the shape delivering, then refactor. "Perfect is the enemy of producing."

---

## Color Mixing Reference

| Color | Type | Mix Formula | Crystal Source |
|:------|:-----|:------------|:---------------|
| White | Primary | (mined directly) | White Dye Crystal |
| Red | Primary | (mined directly) | Red Dye Crystal |
| Green | Primary | (mined directly) | Green Dye Crystal |
| Blue | Primary | (mined directly) | Blue Dye Crystal |
| Yellow | Secondary | Red + Green | Mix Red & Green dye flows |
| Purple | Secondary | Red + Blue | Mix Red & Blue dye flows |
| Cyan | Secondary | Green + Blue | Mix Green & Blue dye flows |
| Uncolored | — | No dye | Skip the Painter step |

Secondary colors require a **Mixer** building that combines two primary dye flows before the Painter applies them.

---

> 🛒 [**Shapez 2 on Steam — Wishlist & Purchase**](https://store.steampowered.com/app/2162800/?utm_source=game-guide&utm_medium=referral&utm_campaign=shapes-reference)
