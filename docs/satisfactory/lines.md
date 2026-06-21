# Satisfactory Production Line Guide

*A comprehensive guide to building efficient production lines from early game to late game.*

---

## 1. Understanding Production Chains

Every factory in Satisfactory is built on a chain of production steps that transform raw resources into increasingly complex parts. Understanding how these chains work is the foundation of good factory design.

### The Basic Flow

```
Mining → Smelting → Constructing → Assembling → Manufacturing
```

| Step | Machine | Input | Output |
|------|---------|-------|--------|
| **Mining** | Miner Mk1–Mk3 | Resource node | Raw ore (iron, copper, limestone, etc.) |
| **Smelting** | Smelter | Raw ore | Ingots (iron, copper, steel, etc.) |
| **Constructing** | Constructor | Ingots | Basic parts (plates, rods, wire, cable) |
| **Assembling** | Assembler | Basic parts | Complex parts (rotors, stators, motors) |
| **Manufacturing** | Manufacturer | Complex parts | Advanced parts (heavy frames, computers) |

Each machine has a **cycle time** and produces a certain number of items per minute. The key to efficiency is matching input rates to output consumption so nothing backs up or starves.

### Recipes

Every recipe specifies:

- **Input items** and their **rate** (items/min)
- **Output items** and their **rate**
- **Power** consumed while operating
- **Duration** per cycle

Example — Iron Plate recipe:

| Input | Amount | Output | Amount | Duration |
|-------|--------|--------|--------|----------|
| Iron Ingot | 3 | Iron Plate | 2 | 6 sec |

At 100% clock speed, a Constructor produces **20 Iron Plates/min** from **30 Iron Ingots/min**.

---

## 2. Basic Factory Layout Patterns

There are two dominant approaches to feeding machines: **manifold** and **load balancer**.

### Manifold (Preferred for Most Builds)

A manifold is a single belt that runs past every machine, with splitters feeding each one in sequence.

```
Input → [Splitter] → [Splitter] → [Splitter] → ...
           ↓            ↓            ↓
        Machine 1    Machine 2    Machine 3
```

**Advantages:**
- Minimal beltwork and space required
- Scales easily — just extend the belt
- Works well at high belt tiers

**Disadvantages:**
- Long ramp-up time — machines at the end of the line don't get materials until earlier machines fill their buffers
- Uneven distribution during startup

**Best for:** Almost everything. Especially large builds where you can let the factory "warm up."

### Load Balancer

A load balancer uses splitters and mergers to distribute items evenly to every machine simultaneously.

```
             ┌→ [Splitter] → Machine 1
             │
Input → [Splitter] ──┼→ [Splitter] → Machine 2
             │       │
             └→ [Splitter] → Machine 3
```

**Advantages:**
- Instant, even distribution — no warm-up time
- Predictable behavior for ratio-perfect builds

**Disadvantages:**
- Complex belt layouts — especially for non-power-of-2 machine counts
- Takes up much more space
- Hard to expand later

**Best for:** Precision builds, compact ratio factories, and builds where warm-up time matters.

### Rule of Thumb

Use **manifolds** for 90% of your factory. Use **load balancers** only for specific throughput-critical sections like nuclear fuel rod production or when you need instant saturation of a downstream process.

---

## 3. How to Calculate Ratios

Every production line needs correctly matched machine counts. The formula is straightforward.

### The Ratio Formula

```
Machines Needed = Output Target (items/min) ÷ Output per Machine (items/min)
```

Or more precisely:

```
Machines Needed = (Target Rate × Cycle Time) ÷ Output per Cycle
```

### Step-by-Step Example

**Goal:** Produce 60 Iron Plates/min.

1. Look up the recipe: Iron Plate makes **2 plates per 6 seconds**.
2. Calculate output per minute: `2 plates ÷ 6 sec × 60 sec = 20 plates/min` per Constructor.
3. Calculate machines: `60 ÷ 20 = 3` Constructors.
4. Check input requirement: Each needs 30 Iron Ingots/min → `3 × 30 = 90` Iron Ingots/min.
5. Calculate Smelters: Each Smelter produces 30 Iron Ingots/min → `90 ÷ 30 = 3` Smelters.
6. Calculate Miners: On a pure node with Mk1 Miner: 60 ore/min. Need 90 ore/min → `90 ÷ 60 = 1.5` — so overclock one Miner to 150% or use a Mk2 Miner.

### Quick Reference Formula

```
Downstream_machines = Upstream_machines × (Upstream_output_per_min ÷ Downstream_input_per_min)
```

### Dealing with Decimals

If you get a fractional machine count like 6.67, you have options:

- **Round up** and underclock the extra machine (saves power)
- **Round down** and overclock remaining machines
- **Use a different recipe** — alternate recipes can dramatically change ratios

---

## 4. Early Game Production Lines

Early game revolves around **Iron** and **Copper**. You have access to Miners Mk1, Smelters, Constructors, and Assemblers.

### Iron Plate Line

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Iron Plate | 3 Iron Ingot | 2 Iron Plate | 20/min |

Build: 1 Miner Mk1 (pure node) → 2 Smelters → 3 Constructors.

Produces 60 Iron Plates/min — enough for early storage and building.

### Iron Rod Line

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Iron Rod | 1 Iron Ingot | 2 Iron Rod | 30/min |

Build: 1 Miner Mk1 (normal node) → 1 Smelter → 1 Constructor.

Produces 30 Iron Rods/min. Rods are used for Screws, Reinforced Plates, and later for Modular Frames.

### Screw Production

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Screw | 1 Iron Rod | 4 Screw | 60/min |

**Critical ratio:** 1 Rod Constructor feeds 2 Screw Constructors (30 rods/min → 2 × 60 screws/min). Screws are used in enormous quantities — plan for this.

### Wire and Cable

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Wire | 1 Copper Ingot | 3 Wire | 45/min |
| Cable | 2 Wire | 1 Cable | 30/min |

Build for Wire: 1 Miner Mk1 (pure copper) → 1 Smelter → 1 Constructor = 45 Wire/min.

Cable is less throughput-intensive — 1 Cable Constructor needs 30 Wire/min, so 1 Wire Constructor feeds 1.5 Cable Constructors.

### Reinforced Iron Plate (First Assembly)

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Reinforced Iron Plate | 6 Iron Plate, 12 Screw | 1 Reinforced Iron Plate | 5/min |

This is your first Assembler build. Feed it from your existing Iron Plate and Screw lines.

---

## 5. Mid Game Production Lines

Steel unlocks at Tier 3/4 and opens up faster belts, stronger buildings, and new production chains.

### Steel Production

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Steel Ingot | 3 Iron Ore, 3 Coal | 3 Steel Ingot | 45/min |

Build: 1 Miner Mk2 (pure iron) + 1 Miner Mk2 (pure coal) → 3 Foundries.

**Key ratio:** 1 Foundry consumes 45 iron ore/min and 45 coal/min, producing 45 steel ingots/min.

### Steel Beam and Steel Pipe

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Steel Beam | 4 Steel Ingot | 1 Steel Beam | 10/min |
| Steel Pipe | 3 Steel Ingot | 2 Steel Pipe | 30/min |

Steel Beams are slow (10/min per constructor) — you'll need many constructors.
Steel Pipes are faster (30/min) and used in larger quantities.

### Encased Industrial Beam

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Encased Industrial Beam | 5 Steel Beam, 6 Concrete | 1 Encased Industrial Beam | 6/min |

Build: 1 Assembler needs 30 Steel Beams/min → 3 Constructors making Steel Beams.
Concrete: 1 Constructor of concrete (at 45/min) easily covers this.

### Motor Production

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Motor | 2 Rotor, 4 Stator | 1 Motor | 6/min |

Each Motor needs:

- **Rotor** (1/min): 5 Iron Rod, 25 Screw per Assembler
- **Stator** (2/min): 9 Steel Pipe, 8 Wire per Assembler

Build: Dedicated sub-factories for Rotors and Stators feeding into Motor Assemblers. This is your first real "sub-factory" challenge.

---

## 6. Late Game Production Lines

Late game introduces complex multi-stage manufacturing with Manufacturers, Blenders, and Refineries.

### Heavy Modular Frame

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Heavy Modular Frame | 5 Modular Frame, 4 Steel Pipe, 4 Encased Industrial Beam, 100 Screw | 1 HMF | 2/min |

This is one of the most complex items in the game. A full production line involves:

1. **Iron Ingots** → Screws, Iron Plates
2. **Steel** → Steel Pipes, Encased Industrial Beams
3. **Concrete** → for Encased Industrial Beams
4. **Modular Frames** → Reinforced Iron Plates + Iron Rods

A single Manufacturer making Heavy Modular Frames requires massive upstream support — typically 30+ machines total.

### Aluminum Production

Aluminum starts at Tier 7 and involves a completely new chemistry system.

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Aluminum Scrap | 6 Bauxite, 6 Coal, 12 Water | 10 Aluminum Scrap, 2 Silica | /cycle |

**Production chain:**

1. Refinery: Bauxite → Alumina Solution (with water)
2. Refinery: Alumina Solution + Coal → Aluminum Scrap (with Silica byproduct)
3. Foundry: Scrap + Silica → Aluminum Ingot
4. Constructor/Assembler: Ingots → Aluminum products (Casings, Sheets)

**Water management is critical** — aluminum production outputs more water than it inputs. You must recycle or sink the excess water to avoid deadlock.

### Radio Control Unit

| Recipe | Input | Output | Rate |
|--------|-------|--------|------|
| Radio Control Unit | 2 Crystal Oscillator, 2 Computer, 1 High-Speed Connector, 5 Rubber | 1 RCU | 2/min |

This is a true endgame item requiring multiple complex supply chains:

- **Crystal Oscillators**: Quartz + Silica + Wire
- **Computers**: Circuit Boards + Cables + Plastic
- **High-Speed Connectors**: Quickwire + Cable + Circuit Boards
- **Rubber**: Oil → Polymer Resin → Rubber

RCUs are used primarily for **Turbo Motors** and **Thermal Propulsion Rockets**, endgame space elevator parts.

---

## 7. Belt Throughput Table

Choosing the right belt tier is essential for preventing bottlenecks.

| Belt | Tier | Max Speed | Unlocked At | Best Used For |
|------|------|-----------|-------------|---------------|
| **Conveyor Belt Mk1** | 1 | 60 items/min | Tier 0 | Early ore, plates, rods |
| **Conveyor Belt Mk2** | 2 | 120 items/min | Tier 2 | Mid-iron lines, steel |
| **Conveyor Belt Mk3** | 3 | 270 items/min | Tier 4 | Steel production, mid-game |
| **Conveyor Belt Mk4** | 4 | 480 items/min | Tier 6 | Late-game input lines |
| **Conveyor Belt Mk5** | 5 | 720 items/min | Tier 7 | Main bus, aluminum, endgame |
| **Conveyor Belt Mk6** | 6 | 1200 items/min | Tier 9 (post-1.0) | Ultimate throughput |

### Splitters and Mergers

| Item | Function | Throughput Limit |
|------|----------|------------------|
| Splitter | Divides 1 input into 3 outputs | Same as input belt |
| Smart Splitter | Filters specific items per output | Same as input belt |
| Programmable Splitter | Complex filtering | Same as input belt |
| Merger | Combines 3 inputs into 1 output | Limited by output belt speed |

### Choosing the Right Belt

A single Mk3 Miner on a pure node with no overclock produces 240 ore/min. That means:

- Mk1 belt (60/min): ❌ Will bottleneck
- Mk2 belt (120/min): ❌ Still too slow
- Mk3 belt (270/min): ✅ Just enough with headroom
- Mk4+ belt: ✅ Future-proof if you plan to overclock

**Golden rule:** Always check your belt speed against your maximum item rate. A bottlenecked belt will starve downstream machines silently.

---

## 8. Common Mistakes to Avoid

### ❌ Belt Bottlenecks

The most common error. You have 240 ore/min coming out of a miner, but you used a Mk1 belt. The miner backs up and underperforms.

**Fix:** Always use belts one tier above what you think you need. When in doubt, use Mk3+ for main lines.

### ❌ Ignoring Screw Throughput

Screws are used in massive quantities but take up significant belt capacity. A single Wilson's Screw Calculator won't save you from the reality: 60 screws/min on a Mk1 belt means the belt is full.

**Fix:** Use alternate recipes (Steel Screws, Cast Screws) to eliminate screw transport entirely, or use high-tier belts on screw lines.

### ❌ Building Too Compact

Trying to fit everything into a tight space works early on but becomes a nightmare to expand. Smelters right next to miners with no room for belt work leads to spaghetti.

**Fix:** Leave 1-2 foundation's worth of space between production rows. Use verticality — stack floors.

### ❌ No Overflow or Sink

A single backed-up production line can halt your entire factory. If one output fills up (e.g., Silica byproduct from Aluminum), the whole chain stalls.

**Fix:** Use **Smart Splitters** to send overflow to an **AWESOME Sink**. Always sink byproducts you can't consume.

### ❌ Underestimating Power

Adding a Manufacturer without building more power plants is a classic trap. Manufacturers consume 40–75 MW each. A bank of 10 consumes as much as a small power plant generates.

**Fix:** Build 2× the power generation you think you need. Use underclocking to reduce power consumption by up to 75% for the same total output.

### ❌ Manifold Ramp-Up Impatience

Your manifold-fed factory takes 15 minutes to fully saturate. You watch the last machine starve and think something is wrong.

**Fix:** Walk away and come back. Or hand-feed the first few stacks into the last machines to speed up saturation.

### ❌ No Vertical Planning

Building everything on one foundation layer creates a sprawling mess that's hard to navigate and expand.

**Fix:** Design in floors:
- Floor 1: Raw ore → Ingots
- Floor 2: Ingots → Components
- Floor 3: Components → Assemblies

Use lifts between floors for clean vertical logistics.

---

## 9. Production Line Design Checklist

Before building any production line, ask yourself:

| Question | Why It Matters |
|----------|----------------|
| What is my target output rate? | Everything scales from here |
| Do I have enough node capacity? | Miner speed limits total potential |
| What belt tier do I need? | Avoids bottlenecks |
| What recipes am I using? | Alternate recipes change everything |
| Where will I expand later? | Plan for Mk3 miners and overclocking |
| How will I handle byproducts? | Prevents deadlocks |
| What are my power requirements? | Prevents brownouts |

---

## 10. Recommended Tools

| Tool | Purpose | URL |
|------|---------|-----|
| **Satisfactory Calculator** | Interactive production planner | [satisfactory-calculator.com](https://satisfactory-calculator.com) |
| **Satisfactory Tools** | Alternate recipe analysis | [satisfactorytools.com](https://satisfactorytools.com) |
| **Satisfactory Wiki** | Recipe database | [satisfactory.wiki.gg](https://satisfactory.wiki.gg) |
| **SCIM (Map)** | Interactive world map | [satisfactory-calculator.com/map](https://satisfactory-calculator.com/map) |

---

## Summary

Building production lines in Satisfactory is a journey from simple mining-to-plate setups to sprawling multi-floor factories processing thousands of items per minute. The key skills are:

1. **Calculate ratios** before you build
2. **Use manifolds** for simplicity, load balancers for precision
3. **Plan belt tiers** ahead of time
4. **Always handle overflow** — sink byproducts
5. **Build vertically** and leave room for expansion
6. **Check power** before flipping the switch

F.I.C.S.I.T. reminds you: *Efficiency is progress. Progress is mandatory.*

---

*Last updated: June 2026 — Compatible with Satisfactory 1.0.*

---

> 🛒 [**Buy Satisfactory on Steam**](https://store.steampowered.com/app/526870/) — Build, automate, optimize.
>
> *This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*
