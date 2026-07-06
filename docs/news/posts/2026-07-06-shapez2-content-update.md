---
title: "Shapez 2 Content Update — New Shapes, Logic Components, and Modular Belt System"
description: "Tobspr Games drops a major free content update for Shapez 2 with 8 new shape types, programmable logic gates, modular belt junctions, and a new endgame milestone."
date: 2026-07-06
author: game-guide
tags: [news, update, shapez-2]
---

## Shapez 2 Content Update — Logic and Expansion

Tobspr Games has released a significant **free content update** for Shapez 2, the pure factory-building automation game that launched to strong reviews earlier this year. The update introduces **8 new shape types**, a fully programmable **logic component system**, **modular belt junctions**, and an extended endgame milestone that gives even the most dedicated factory architects new challenges.

### New Shape Types

The update adds 8 new base shapes that appear as you progress through the mid-to-late game:

**Quadrant shapes (tier 3):**

1. **Crystal** — Sharp, angular quadrant. Requires quartz processing to unlock. Used in advanced circuit recipes.
2. **Wave** — Curved quadrant that requires fluid processing (new mechanic — see below). Pairs with other fluid-based components.
3. **Gear** — Toothed quadrant. A purely decorative shape variant, but required for some milestone goals.
4. **Node** — Circular quadrant with connection points. Used in logic circuit recipes.

**Composite shapes (tier 4):**

5. **Star** — 4-point star shape, formed by combining Crystal + Wave quadrants.
6. **Hex** — Hexagonal shape, formed by combining Gear + Node quadrants.
7. **Circuit** — A complex shape with internal routing lines. Requires all four tier-3 quadrants.
8. **Cog** — A mechanical composite shape. Used in the new endgame milestone.

### Logic Component System

The biggest change in this update is the introduction of **programmable logic gates** that let you control belt flow, building activation, and sorting with real-time logic.

**Basic logic components (tier 3 unlock):**

- **AND Gate** — Outputs a signal when both inputs A and B are active.
- **OR Gate** — Outputs a signal when either input A or B is active.
- **NOT Gate** — Outputs a signal when the input is inactive (inverter).
- **XOR Gate** — Outputs a signal when inputs A and B differ.
- **Signal Splitter** — Divides an input signal into two outputs at a configurable ratio (25/75, 50/50, 75/25).

**Advanced components (tier 4 unlock):**

- **Memory Cell** — Stores a binary state that persists until overwritten. Can chain multiple cells for shift registers.
- **Counter** — Counts input pulses and outputs a signal every N pulses. Configurable threshold.
- **Comparator** — Compares two input values. Outputs A > B, A = B, or A < B.
- **Delay Line** — Delays signal propagation by N game ticks. Useful for timing belt merges.

**Practical applications:**
- Route shapes to specific processors based on color matching.
- Pause a production line when output buffers are full.
- Count the number of shapes passing a checkpoint and trigger an alarm at a threshold.
- Synchronize multiple belt lines for perfect merging without jams.

### Modular Belt Junctions

Belt management gets an upgrade with the **Modular Junction** system:

- **4-way Intersection** — A single-tile junction that handles belts crossing from all four directions with smart priority routing.
- **Roundabout** — A 2x2 tile circular junction that prevents deadlocks on high-throughput belts.
- **Elevated Crossing** — One belt crosses over another without intersection. Handy for dense factory floors.
- **Tunnel Belt** — Underground belt segment (up to 8 tiles) for routing under existing machinery.

### Fluid Processing

As hinted by the Wave quadrant, the update introduces a light **fluid processing** layer:

- **Fluid Pipes** — Connect between buildings. Can transport colored dye or coolant.
- **Dye Vat** — Submerges shapes in colored dye before they enter the painting step. Dye can be piped in from a centralized dye production area.
- **Coolant Tower** — Required for tier-4 processors. Consumes water (piped in) and vents steam.

Fluid is optional for most of the game but required for Crystal and Wave shape production.

### New Endgame Milestone

A new building, the **Memorial Hub**, serves as the ultimate endgame milestone. To construct it, players must deliver:

- 1,000 Star shapes (any color)
- 1,000 Hex shapes (any color)
- 500 Circuit shapes (any color)
- 100 Cog shapes (any color)
- 10,000 units of coolant

Completing the Memorial Hub unlocks the **Infinite Overdrive** upgrade — all belts move at 2x speed, and all processors operate at 1.5x speed. It's a permanent per-save upgrade designed for players who want to push their factory to maximum throughput.

### Community Reaction

> *"The logic gates completely change how I approach belt routing. I built a shape counter in 10 minutes. This is Factorio levels of circuit network now."* — r/shapezio

> *"Fluid processing was unexpected but it's implemented elegantly. It doesn't overshadow the core shape mechanics."* — Steam review

> *"Modular junctions alone make this update worth it. No more spaghetti intersections."* — Shapez 2 Discord

### How to Update

The update is **free** for all Shapez 2 owners. It will download automatically on Steam. The new content is added to existing saves — you'll need to research the tier-3 shape upgrades at the Hub.

For complete Shapez 2 guides, including logic gate tutorials and optimal fluid layouts, visit game-guide.club.
