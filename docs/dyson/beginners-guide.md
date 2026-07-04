---
title: "Dyson Sphere Program Beginner's Guide — First 20 Hours to Interplanetary Travel"
description: "Complete DSP beginner's guide. From waking up in your crashed mecha to launching your first interstellar logistics vessel — step by step with exact machine counts, research priorities, and time estimates."
date: 2026-07-04
---

# 🌌 Dyson Sphere Program: Complete Beginner's Guide — First 20 Hours

**Developer:** Youthcat Studio | **Publisher:** Gamera Game  
**Steam Price:** $19.99 | **Current Version:** 0.10.x  
**Estimated Playtime:** 15–25 hours to first interplanetary logistics

---

## Overview

Dyson Sphere Program (DSP) can overwhelm new players. You wake up on an alien planet with a damaged mecha and a single mining drill, and within minutes you're staring at a procedurally-generated star cluster with dozens of planets — each with different resources, wind speeds, and luminosity. **Where do you go? What do you build first? Which research unlocks what?**

This guide walks you through the **first 20 hours** of DSP, broken into clear phases with exact machine counts, research priorities, and time estimates. Whether you're a complete newcomer or a veteran of Factorio and Satisfactory, this is your roadmap from crash-landed AI to interplanetary empire builder.

---

## Phase 1: Survival & Basic Tools (0–30 Minutes)

**Goal:** Establish a sustainable base, automate your first resources, and unlock blue science.

### Step 1: The First Hour — Manual Mining

You spawn with a **Mining Drill MK.I** (hand-mining) and a **Construction Robot** that places basic buildings. Your immediate priorities:

1. **Find iron ore** (grey rocks) and **copper ore** (reddish rocks). These are abundant everywhere on your starting planet.
2. **Mine 200 iron + 100 copper** by hand. This takes about 10–15 minutes with one person.
3. **Build your first Mining Drill MK.I** — place it on an iron ore node. It mines 6 iron ingots/min (with 2 smelters).
4. **Build 2 Smelters** — each converts 1 iron ore/min → 2 iron ingots/min. Place them next to your drill.
5. **Build 1 Assembler MK.I** — this is your first crafting station.

> 💡 **Time estimate:** 15–30 minutes of manual mining, then 5 minutes to set up your first automated iron+copper line.

### Step 2: The Core Early-Game Trio

Once you have basic automation, focus on these three products — they unlock everything else:

| Product | Machines | Input Rate | Output Rate | Purpose |
|---------|----------|------------|-------------|---------|
| **Magnetic Coil** | 1 Assembler | 2 iron/s + 1 copper/s | 1/s | Blue science ingredient |
| **Circuit Board** | 1 Assembler | 2 iron/s + 2 copper/s | 1/s | Blue science ingredient |
| **Blue Science (Matrix)** | 1 Assembler | 2 magnetic coils + 1 circuit board | 1/s | Research unlock |

**Machine layout recommendation:**
```
[Iron Drill] → [Smelter] → [Iron Ingot Belt] ─┐
[Copper Drill] → [Smelter] → [Copper Ingot Belt] ─┤→ [Assembler MK.I] → Magnetic Coil
                                                    → [Assembler MK.I] → Circuit Board
```

> ⚠️ **Common mistake:** Don't overbuild smelters before you have conveyors. A single drill feeds 2 smelters perfectly. Adding more smelters without more drills just wastes power and space.

### Step 3: Power Your Base

Early game power is straightforward:

| Power Source | When to Use | Output |
|-------------|-------------|--------|
| **Wind Turbine** | Starting planet (most have decent wind) | 0.3–1.5 MW (varies by location) |
| **Solar Panel** | High-luminosity planets | 0.42–0.6 MW |
| **Thermal Generator (Coal)** | When wind isn't enough | 2.16 MW (burns 27 coal/min) |

**Rule of thumb:** Build 3–4 wind turbines near your base before you need coal. Coal generators are reliable but consume resources you'll need for other things.

> 🎯 **Milestone:** By the end of Phase 1, you should have 1–2 blue science per minute flowing into your research lab. Total time: **20–45 minutes**.

---

## Phase 2: Blue Science to Yellow Science (30 Min – 3 Hours)

**Goal:** Unlock logistics MK.II, drones, and begin planning your first rare-ore expedition.

### Research Priority Queue

Research in this exact order. Don't skip ahead — each unlocks the next:

1. **Logistics MK.I** (blue) → unlocks Planetary Logistics Stations (drones)
2. **Logistics MK.II** (blue) → unlocks faster drones and larger PLS capacity
3. **Construction Robot MK.II** (blue) → faster building, larger inventory
4. **Interstellar Logistics** (yellow, requires red science) → unlocks ILS vessels
5. **Dyson Swarm** (red) → unlocks solar sails for early power boost

### The Drone Revolution — PLS Deployment

Once you unlock **Planetary Logistics Stations (PLS)**, your factory transforms. Here's how:

1. **Place a Supplier PLS** near your main production zone (iron, copper, coal, stone)
2. **Place Requester PLS** near your assemblers and smelters
3. **Drones auto-transport** items between them — no belts needed

**Why this matters:** Without PLS, you route everything through belts. With PLS, a single drone pair can replace hundreds of meters of belt. This is the single biggest quality-of-life improvement in early DSP.

> 💡 **PLS placement rule:** Supplier PLS goes where raw materials are mined. Requester PLS goes where machines consume materials. Keep them within 500–1000 meters of each other for best drone performance.

### Rare Ore Scouting

Before you leave your starting planet, **map all nearby planets** in your star cluster:

| Planet Type | Rare Ore | Value |
|------------|----------|-------|
| **Volcanic / Ash** | Kimberlite Ore | Replaces graphite → diamond chain |
| **Desert / Gobi** | Optic Crystal | Replaces processor chain |
| **Ice / Gelisol** | Spiniform Stalagmite | Replaces nanotube chain |
| **Barren / Desolate** | Fractal Silicon | Replaces silicon smelting |
| **Ocean / Swamp** | Grassstone | Replaces half of stone processing |

**How to scout:** Build a rocket (unlocked by red science) or fly your mecha to each planet. Check the resource scanner in the bottom-right corner. Note which planets have rare ores.

> ⚠️ **Don't colonize rare-ore planets yet.** You can't land on them until you unlock the **Rare Ore Extractor** (purple science). For now, just note their coordinates.

### 🎯 Milestone: You now have drones running your factory, blue science flowing consistently, and a map of all planets in your cluster. Total playtime: **2–3 hours**.

---

## Phase 3: Red Science & The Proliferator (3–8 Hours)

**Goal:** Unlock the Proliferator (game-changer) and establish your first interplanetary supply chain.

### The Proliferator — Your Best Friend

The **Proliferator** is the single most impactful machine in DSP. It sits on top of a resource node and increases output by 25% per level (up to level 3, for +75% total).

**How to build one:**
1. Unlock **red science** (requires titanium + deuterium)
2. Build a **Proliferator MK.I** on top of your most bottlenecked resource node
3. Upgrade to MK.II and MK.III as you unlock more red science

**Priority order for Proliferator placement:**
1. **Iron** — everything flows from iron
2. **Copper** — second most universal resource
3. **Silicon** — needed for processors and quantum chips
4. **Titanium** — needed for yellow and purple science

> 💡 **Pro tip:** A level-3 Proliferator on iron is worth building 3 extra iron mines. Always proliferate before expanding.

### Red Science Production

Red science (🔴) requires **titanium** and **deuterium**:

| Input | Machines | Rate |
|-------|----------|------|
| 3 Titanium Ingots + 1 Deuterium | 2 Assembler MK.II | 1 red matrix/min |

**Titanium sourcing:** Find a titanium-rich planet (check resource scanner). Ship raw titanium ore back to your main factory — it stacks to 100, so transport is efficient.

**Deuterium sourcing:** Use a **Fractionator** with crude oil. The fractionation process produces deuterium as a byproduct. Alternatively, use an **Orbital Collector** around a gas giant for direct hydrogen/deuterium harvesting.

### Interstellar Logistics — Your First Vessel

Once you unlock **interstellar logistics** (purple science prerequisite), you can build your first **Interstellar Logistics Station (ILS)** and launch a **Vessel**:

1. Build an ILS on your main factory planet
2. Construct a Vessel at the ILS (requires warpers — green science)
3. Set the Vessel to transport rare ores from colonized planets back to your main factory

**Vessel capacity:** Each vessel carries 50 stacks of items. Plan your routes carefully — ship raw materials, not finished products.

> ⚠️ **Warpers are the bottleneck.** Green science (quantum chip + graviton lens) is extremely expensive. Don't rush to build warpers until your main factory is stable.

### 🎯 Milestone: Proliferators on your key resources, red science flowing, and your first interplanetary vessel en route. Total playtime: **5–8 hours**.

---

## Phase 4: Yellow & Purple Science (8–15 Hours)

**Goal:** Establish multi-planet operations, unlock the Dyson Swarm, and prepare for your first sphere layer.

### Yellow Science (🟡) — The Expansion Trigger

Yellow science unlocks:
- **Logistics MK.III** (faster, higher-capacity drones)
- **Orbital Collectors** (harvest gas giants from orbit)
- **Rare Ore Extractor** (mine rare ores on colonized planets)

**Recipe:** 3 Titanium Crystals + 2 Processors per minute

**Processor bottleneck:** Processors require silicon, which means you need a dedicated silicon mine. If your starting planet doesn't have enough silicon, colonize a barren planet or import from another cluster planet.

### Purple Science (🟣) — The Late-Game Gateway

Purple science unlocks:
- **Dyson Sphere construction** (the game's namesake mechanic)
- **MK.III Assemblers** (3× throughput)
- **Advanced warper technology**

**Recipe:** 5 Plutonic Crystals + 4 Processors per minute

Plutonic crystals come from **particle colliders** on specific planets. You'll need to identify which planets in your cluster have particle collider resources.

### The Dyson Swarm — Early Power Rush

Before building the permanent Dyson sphere, construct a **Dyson Swarm** using solar sails:

1. Build a **Dyson Swarm Generator** (unlocked by red science)
2. Launch solar sails around your star
3. Each sail generates power that feeds into **Ray Receivers** on your planets

**Why start with sails?** Solar sails degrade after ~2 hours but generate massive power during their lifetime. This gives you the energy to build your first rocket-launched sphere layer before sails decay.

**Optimal sail count:** Start with 50–100 sails. Each sail generates approximately 1–5 MW depending on the star type. O-type stars (brightest) give the highest output.

### 🎯 Milestone: Multi-planet factory network, Dyson Swarm operational, purple science research underway. Total playtime: **12–15 hours**.

---

## Phase 5: The Dyson Sphere & Beyond (15–20+ Hours)

**Goal:** Launch your first permanent sphere layer and achieve energy independence.

### Rocket-Launched Sphere Construction

Unlike temporary solar sails, rockets build the **permanent frame** of your Dyson sphere:

1. **Build a Rocket Launch Pad** on your main planet
2. **Construct Rockets** (requires titanium, carbon nanotubes, and photonic processors)
3. **Launch Rockets** to build frame nodes and beams around your star
4. **Fill frames** with solar panels for maximum power output

**Frame construction strategy:**
- Start with a small radius (0.5–0.8× the star's radius)
- Use the **automatic editor** with the "triangle grid" preset
- Build 3–5 concentric layers around the brightest star in your cluster

### Energy Independence

Once your first sphere layer is operational:

| Sphere Layer | Power Output | Time to Build |
|-------------|-------------|---------------|
| **Layer 1** (small radius) | ~500–2000 MW | 2–4 hours |
| **Layer 2** (same star) | +500–2000 MW | 4–8 hours |
| **Layer 3** (different star) | Variable | 8–12 hours |

> 💡 **Golden rule:** Build your sphere around the **brightest star** (O or B type). An O-type star sphere generates 5–10× more power than a red dwarf sphere.

### Post-Sphere Priorities

After achieving energy independence, your goals shift:

1. **Scale up white science** (antimatter + all colored matrices) — this unlocks infinite research upgrades
2. **Build antimatter fuel rods** — the most efficient power source in the game
3. **Expand to other star clusters** — each cluster has unique rare ores and star types
4. **Optimize your factory** — apply proliferators everywhere, replace belts with drones, centralize smelting

### 🎯 Completion: You've built a Dyson sphere. The game is yours to explore from here. Total playtime: **20–30 hours** for a satisfying first run.

---

## Zero-Spend vs. Paid Strategies

| Aspect | Free-to-Start (Zero Investment) | Mod-Enhanced (Recommended) | Speedrun (Experienced Players) |
|--------|--------------------------------|---------------------------|-------------------------------|
| **Research pace** | Follow guide exactly | Use "Faster Research" mods | Skip non-essentials |
| **Factory layout** | Manual belt routing | Use blueprint mods | Pre-planned mega-factories |
| **Time to sphere** | 20–30 hours | 15–20 hours | 6–10 hours |
| **Recommended mods** | None | Factory Planner, Faster Drones | Everything |

---

## Common Beginner Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| **Overbuilding smelters without drills** | Wastes power and space | 1 drill → 2 smelters max |
| **Ignoring Proliferators** | 25–75% less output than potential | Proliferate iron and copper first |
| **Shipping processed goods interplanetary** | 5× less efficient than shipping ore | Ship raw ores, smelt at main factory |
| **Not building a mall planet** | Hand-crafting buildings is a massive time sink | Automate belt/asm/smelter production on a dedicated planet |
| **Underbuilding power** | Factory stalls when you expand | Build 3× the power you think you need |
| **Empty research queue** | Wasted time waiting for science | Always have 2–3 research items queued |

---

## Quick Reference: Research Unlock Tree

```
Blue Science (🟢)
  ├── Logistics MK.I → Planetary Logistics Stations (drones)
  ├── Logistics MK.II → Faster drones
  └── Construction Robot MK.II → Better building robots

Red Science (🔴)
  ├── Proliferator → +25% resource node output per level
  ├── Dyson Swarm → Solar sails for early power
  └── Rare Ore Extractor → Mine rare ores

Yellow Science (🟡)
  ├── Logistics MK.III → Maximum drone efficiency
  ├── Orbital Collector → Harvest gas giants
  └── Rare Ore Extractor MK.II → Higher-yield rare ore mining

Green Science (🟤)
  ├── Warpers → Interstellar vessel travel
  └── Quantum Chip → Advanced crafting

Purple Science (🟣)
  ├── Dyson Sphere construction
  ├── MK.III Assemblers → 3× throughput
  └── Advanced warpers → Faster interstellar travel

White Science (⚪)
  └── Infinite research upgrades → Max everything
```

---

> 🛒 [**Buy Dyson Sphere Program on Steam**](https://store.steampowered.com/app/1366540/) — Support the developer!
>
> *Affiliate link — we earn a small commission at no extra cost to you.*

*Data from Dyson Sphere Program Wiki (v0.10.x) and dsp-calc.com. Last updated: July 2026.*
