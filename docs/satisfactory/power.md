---
title: ⚡ Satisfactory Power Grid Guide — Coal, Nuclear & Fuel Generator Setup
description: From flickering biomass burners to roaring nuclear reactors — master every power source in Satisfactory.
date: 2026-06-27
---

# ⚡ Satisfactory Power Systems Guide

*From flickering biomass burners to roaring nuclear reactors — master every power source in Satisfactory.*

---

## 1. Introduction to Power

Power is the lifeblood of every Satisfactory factory. Every machine — from the humblest Constructor to the most demanding Particle Accelerator — requires electricity to operate. Unlike some factory games where power is a binary on/off concern, Satisfactory demands active management: you must expand generation capacity as your factory grows, handle multiple fuel types, manage waste, and prevent grid collapse.

This guide covers every power source in the game, from the hand-fed Biomass Burner you start with to the zero-fuel Geothermal Generators of the lategame, along with power storage, grid management, and efficiency strategies.

### Power Consumption Overview

| Machine | Power Consumption |
|---------|-----------------|
| Miner Mk.1 | 5 MW |
| Constructor | 4 MW |
| Assembler | 15 MW |
| Refinery | 30 MW |
| Manufacturer | 40–75 MW |
| Blender | 75 MW |
| Particle Accelerator | 250–1,500 MW |
| Convert-o-tron | 100 MW |

A single Manufacturer running at 100% consumes as much power as **ten Constructors**. Always check your power budget before adding new production lines.

---

## 2. Biomass Burners — The Early Struggle

Biomass Burners are your first power source, unlocked at Tier 0. They burn organic materials — leaves, wood, mycelia, and alien remains — to generate electricity.

### Biomass Burner Specs

| Stat | Value |
|------|-------|
| Power Output | 30 MW |
| Fuel Types | Leaves, Wood, Biomass, Solid Biofuel, Fabric, Mycelia |
| Burn Time (Wood) | 3 seconds per unit |
| Burn Time (Solid Biofuel) | 12 seconds per unit |
| Automation | None — must be refuelled manually |

### Limitations

- **No automation.** You must physically collect fuel and refill each burner. This becomes tedious very quickly.
- **Low energy density.** Leaves burn out in 1.5 seconds. Even Wood lasts only 3 seconds per unit.
- **Scalability wall.** The time spent gathering fuel grows linearly with your power needs, while factory expansion is exponential.

### Strategy

1. **Convert everything to Solid Biofuel.** The Biomass → Solid Biofuel recipe in the Constructor (Tier 1) gives you 4× the burn time per unit of Biomass. Processing Wood into Biomass and then into Solid Biofuel yields the best energy density.
2. **Build 6–8 Biomass Burners** to support early production lines (smelters, constructors, assemblers).
3. **Rush to Coal Power.** Consider Biomass Burners a temporary measure. Your goal should be Coal Power (Tier 3) as quickly as possible.

!!! tip "Pro Tip"
    Keep a storage container full of Solid Biofuel near your burners and set up a Constructor to make more automatically. Even though you have to hand-feed the burners, you can automate fuel *production*.

---

## 3. Coal Power — Your First Automated Power

Coal Generators mark the transition from manual to automated power. They consume Coal and Water to generate electricity without any player intervention.

### Coal Generator Specs

| Stat | Value |
|------|-------|
| Power Output | 75 MW |
| Fuel | Coal (15 Coal/min) |
| Water | 45 m³/min |
| Pipe Connections | 1 Water input |
| Overclocking | Up to 2.5× (187.5 MW at 250%) |

### The 8:3 Ratio

The classic Coal Generator ratio is the foundation of reliable coal power:

| Component | Count | Notes |
|-----------|-------|-------|
| Coal Generators | 8 | Produces 600 MW total |
| Water Extractors | 3 | Each produces 120 m³/min water |
| Coal Consumption | 120 Coal/min | One Mk.2 Miner on a pure node |
| Water Requirement | 360 m³/min | 3× Extractors = 360 m³/min |

**How to build it:**

1. Place **8 Coal Generators** in a row.
2. Run one Mk.1 Pipeline along the back with Water Extractors feeding in.
3. Run one Conveyor Belt along the front delivering Coal.
4. Connect 3 Water Extractors — each one feeds **120 m³/min**. With Mk.1 pipes (300 m³/min capacity), you need to split the water feed. A common approach is to connect each Water Extractor to two pipe junctions feeding the generator bank from both ends.

### Water Setup Tips

- **Mk.1 Pipes** carry 300 m³/min. The full 360 m³/min from 3 Extractors exceeds a single Mk.1 pipe. Use two pipes feeding from opposite ends, or upgrade to Mk.2 pipes (600 m³/min) once available.
- **Head lift matters.** Water Extractors produce 10m of head lift. If your generators are higher than the extractors, add pumps.
- **Valves prevent backflow** and help balance water distribution between generator groups.

### Scaling Up

| Generator Count | Water Extractors | Coal/min | Total Power |
|----------------|-----------------|----------|-------------|
| 8 | 3 | 120 | 600 MW |
| 16 | 6 | 240 | 1,200 MW |
| 24 | 9 | 360 | 1,800 MW |
| 32 | 12 | 480 | 2,400 MW |

A 32-generator plant produces **2.4 GW** — enough to power you through Tiers 4–6 with comfortable headroom.

---

## 4. Fuel Generators — Entering the Oil Age

Fuel Generators run on Fuel (produced from Crude Oil in Refineries) and represent a significant power density improvement over Coal.

### Fuel Generator Specs

| Stat | Value |
|------|-------|
| Power Output | 150 MW |
| Fuel | Fuel (12 m³/min) |
| Automation | Fully automatic |
| Overclocking | Up to 2.5× (375 MW at 250%) |

### Basic Fuel Setup

| Component | Count | Production |
|-----------|-------|------------|
| Oil Extractor | 1 | 120 m³/min Crude Oil |
| Refinery (Fuel) | 2 | Produces 80 m³/min Fuel total |
| Refinery (Polymer Resin) | 2 | Byproduct: 60 Polymer Resin/min |
| Fuel Generators | 6 | Consumes 72 m³/min |
| Excess Fuel | — | ~8 m³/min available |

**Important:** Standard Fuel refining produces **Polymer Resin** as a byproduct. If the resin output backs up, your refineries stop producing Fuel. Always sink the excess resin into an AWESOME Sink or process it into Plastic/Rubber.

### Diluted Fuel — The Game Changer

The **Diluted Fuel** alternate recipe (found in crash site hard drives) doubles your Fuel output from the same crude oil input. This is arguably the most important alternate recipe in the entire game.

| Recipe | Crude Oil | Output | Efficiency |
|--------|-----------|--------|------------|
| Standard Fuel | 60 m³/min | 40 m³/min Fuel | 1× |
| Diluted Fuel | 60 m³/min | 80 m³/min Fuel | 2× |

**Diluted Fuel chain:**

1. Refinery: Crude Oil → Heavy Oil Residue (alternate recipe)
2. Refinery: Heavy Oil Residue + Water → Diluted Fuel (with Polymer Resin byproduct)

This chain produces **twice the Fuel** from the same crude oil, effectively doubling your power generation per oil node. A single pure oil node (600 m³/min) with Diluted Fuel can power **up to 100 Fuel Generators** (15 GW) — enough to carry you to nuclear power.

---

## 5. Turbofuel — Maximum Refinement

Turbofuel is a refined fuel type made by combining standard Fuel with Compacted Coal (Coal + Sulfur). It burns much more efficiently in Fuel Generators.

### Turbofuel Specs

| Stat | Standard Fuel | Turbofuel |
|------|--------------|-----------|
| Energy per m³ | 750 MJ | 2,000 MJ |
| Generator consumption | 12 m³/min | ~4.5 m³/min |
| Generators per 100 m³/min | ~8 | ~22 |

### Turbofuel Production Chain

| Step | Machine | Input | Output |
|------|---------|-------|--------|
| 1 | Refinery | Crude Oil | Heavy Oil Residue + Polymer Resin |
| 2 | Refinery | Heavy Oil Residue + Water | Diluted Fuel |
| 3 | Assembler | Coal + Sulfur | Compacted Coal |
| 4 | Refinery | Diluted Fuel + Compacted Coal | Turbofuel |

A full Turbofuel plant is complex but rewarding. A single pure oil node (600 m³/min) can produce enough Turbofuel for **~133 Fuel Generators**, generating roughly **20 GW** — a massive leap.

### Is Turbofuel Worth It?

| Factor | Assessment |
|--------|------------|
| Power density | ✅ 2.6× more power per oil node than standard Fuel |
| Complexity | ⚠️ Requires sulfur logistics (often from distant nodes) |
| Setup cost | ⚠️ Significant refinery count and piping |
| Endgame value | ✅ Transitions well if you eventually go nuclear |

For many players, **Diluted Fuel** alone provides enough power to skip straight to Nuclear. Pursue Turbofuel if you want maximum power from oil before tackling nuclear logistics.

---

## 6. Nuclear Power — Endgame Energy

Nuclear Power Plants produce massive amounts of energy but introduce **Nuclear Waste** — a byproduct that must be managed permanently.

### Nuclear Power Plant Specs

| Stat | Value |
|------|-------|
| Power Output | 2,500 MW |
| Fuel | Uranium Fuel Rods (0.2/min) |
| Water | 240 m³/min |
| Waste Produced | 10 Nuclear Waste/min |

### Uranium Refinement Chain

| Step | Machine | Input | Output |
|------|---------|-------|--------|
| 1 | Miner | Uranium Node | Uranium Ore |
| 2 | Refinery | Uranium Ore + Sulfuric Acid | Uranium Hexafluoride Gas |
| 3 | Blender | Uranium Hexafluoride + Water | Uranium Tetrafluoride + Water byproduct |
| 4 | Blender | Uranium Tetrafluoride + Electromagnetic Control Rod | Encased Uranium Cell |
| 5 | Manufacturer | Encased Uranium Cell + Steel Beam + Electromagnetic Control Rod + Crystal Oscillator | Uranium Fuel Rod |

### Waste Management

Each Nuclear Plant produces **10 Nuclear Waste per minute**. Unprocessed waste accumulates indefinitely and emits radiation. You have two options:

**Option A: Storage (Temporary)**
Use **Industrial Storage Containers** to store waste. One container holds 48 stacks (2,400 items). A single nuclear plant fills one container every 4 hours. Build a massive, distant waste storage facility and forget about it — for a while.

**Option B: Plutonium Reprocessing (Permanent)**
Unlocked later in Tier 8, Plutonium refinement converts Nuclear Waste into **Plutonium Fuel Rods**, which can be burned in additional Nuclear Power Plants. Critically, Plutonium waste **cannot be reprocessed further**, but Plutonium Fuel Rods produce **no waste** when burned in FICSIT's special non-fissile configuration (effectively, the waste from Plutonium is vastly less, but it still exists — you must sink the rods or store them).

### Nuclear Power Plant Ratios

| Setup | Power | Notes |
|-------|-------|-------|
| 1 Plant | 2.5 GW | Simple, manageable waste |
| 4 Plants | 10 GW | Requires significant uranium node |
| 10 Plants | 25 GW | Full pure uranium node utilization |
| 10 Plants + Plutonium | ~30 GW+ | Reprocessing for maximum output |

!!! warning "Radiation"
    Nuclear production chains emit radiation. Wear a Hazmat Suit (or better, Iodine-Infused Filter) when working in the nuclear facility. Build your nuclear plant away from your main base.

---

## 7. Geothermal Generators — Set-and-Forget

Geothermal Generators harvest heat from **Geyser nodes** scattered across the map. They require no fuel, produce no waste, and run silently forever.

### Geothermal Generator Specs

| Stat | Value |
|------|-------|
| Power Output | 200–400 MW (varies by geyser) |
| Fuel | None |
| Waste | None |
| Set cost | 1 Geothermal Generator + 1 Portable Miner |

### Geyser Output Variations

Each geyser has a randomly assigned power output between 200 MW and 400 MW. To find the best ones:

- Explore the map with the **Resource Scanner** set to Geothermal
- Mark geysers on your map and check output before committing resources
- Prioritize geysers with 300+ MW output

### Strategy

Geothermal power is **passive** and **maintenance-free** — it just works. Build it whenever you find a geyser and have spare materials. While individual output is modest (200–400 MW), finding 10 geysers can add 2–4 GW to your grid with zero ongoing cost. It pairs excellently with battery storage for base load coverage.

| Map Zone | Approximate Geyser Count | Total Potential |
|----------|------------------------|-----------------|
| Grass Fields | 2–3 | 600–1,000 MW |
| Rocky Desert | 3–4 | 800–1,400 MW |
| Northern Forest | 2 | 500–800 MW |
| Dune Desert | 4–5 | 1,000–1,800 MW |
| Swamp | 3 | 700–1,200 MW |
| Red Jungle | 2–3 | 600–1,000 MW |

---

## 8. Power Storage — Batteries & Peak Shaving

Power Storages (batteries) store excess energy and release it when demand spikes. They are essential for handling variable loads.

### Power Storage Specs

| Stat | Value |
|------|-------|
| Max Power Group Storage | 100 MWh per battery |
| Max Charge/Discharge Rate | 100 MW per battery |
| Charge Priority | After generators supply demand |
| Discharge Priority | Before generators throttle down |

### Battery Strategy

| Use Case | How Many | Benefit |
|----------|----------|---------|
| Peak shaving | 4–8 | Absorbs spikes from Particle Accelerators |
| Grid stability | 10–20 | Prevents brownouts during expansion |
| Backup power | 20–50 | Survives fuel supply interruptions |
| Megabase | 100+ | Cushions massive load changes |

**Example:** A Particle Accelerator running at 250% draws up to 1,500 MW in pulses. Without batteries, you need 1,500 MW of spare generation capacity. With batteries, you can have 1,000 MW of generation plus 500 MW of battery discharge — much cheaper.

### Charge/Discharge Behavior

```
Grid Load < Generation → Batteries charge (up to 100 MW each)
Grid Load = Generation → Batteries idle
Grid Load > Generation → Batteries discharge (up to 100 MW each)
```

Batteries **always discharge before generators overload**. This means a small generation deficit is automatically covered by battery power, giving you time to react.

!!! tip "Rule of Thumb"
    Build **1 battery per 500 MW** of peak power consumption. This gives you roughly 2 minutes of full-load backup time to fix fuel issues.

---

## 9. Grid Management & Power Priorities

Satisfactory's power grid has a simple but important priority system:

### Power Priority Order

| Priority | Element | Behavior |
|----------|---------|----------|
| 1 (Highest) | Power Storages | Charge first, discharge to cover deficits |
| 2 | Geothermal | Always on — no fuel cost |
| 3 | Nuclear | Always on — waste accumulates regardless |
| 4 | Fuel Generators | Variable — fuel-dependent |
| 5 | Coal Generators | Variable — water/coal-dependent |
| 6 | Biomass Burners | Variable — manual fuel only |
| 7 (Lowest) | AWESOME Sink | Runs only when surplus exists |

### Grid Failure (Brownout)

When demand exceeds supply, generators throttle down to match production to consumption. This creates a **death spiral**:

1. Coal Generators lose power → Water Extractors slow down
2. Less water → Less coal power → Even less power for water extractors
3. Entire grid collapses

**To recover:** Disconnect most of your factory, let the remaining grid stabilize, then gradually reconnect sections. **Always keep a backup power switch** — build a separate, isolated power plant with its own grid that you can use to restart the main grid.

### Priority Power Switches

Use **Priority Power Switches** (unlocked in the AWESOME Shop for 1 ticket) to segment your grid:

| Switch | Connected To | Priority |
|--------|-------------|----------|
| Main Switch | Entire factory | — |
| Production Switch | All production buildings | Low |
| Power Plant Switch | Water extractors + miners only | Critical |
| Base Switch | Hub, M.A.M., equipment workshop | Essential |

With this setup, a brownout automatically disconnects production while keeping the power plant running — preventing the death spiral.

### Monitoring Tools

| Tool | Function |
|------|----------|
| **Power Graph** (in HUD) | Real-time consumption vs production |
| **Statistics** (in HUD) | Detailed breakdown by building type |
| **Power Poles** | Shows local grid stability on hover |
| **Priority Power Switch** | Manual disconnect of grid sections |

---

## 10. Power Progression Summary

| Tier | Power Source | Typical Capacity | Key Milestone |
|------|-------------|-----------------|---------------|
| 0–2 | Biomass Burners | 30–180 MW | Survive to coal |
| 3–4 | Coal Generators | 600–2,400 MW | First automated power |
| 5–6 | Fuel Generators | 2–6 GW | Oil refinement |
| 5–6 | Diluted Fuel | 4–15 GW | Double oil efficiency |
| 6–7 | Turbofuel | 8–20 GW | Maximum oil output |
| 7–8 | Nuclear Power | 10–50 GW | Endgame energy |
| 7–9 | Geothermal | 1–4 GW | Passive supplement |
| 8–9 | Nuclear + Plutonium | 20–80 GW | Ultimate power |

### Final Tips

1. **Overbuild power.** Build 50% more generation than you think you need. Power demand always surprises you.
2. **Underclock production.** Running two Constructors at 50% each uses 50% less power than one Constructor at 100% — for the same output.
3. **Separate your power grid.** Always keep your power plant on an isolated circuit with priority switches.
4. **Plan for expansion.** Leave room for 2× your current generator count. You will need it.
5. **Use batteries.** Even 10 batteries prevent brownouts and give you reaction time.

---

## 🔗 Get Satisfactory

Ready to put these power systems to work? Grab Satisfactory on Steam:

[**🎮 Satisfactory on Steam — $34.99**](https://store.steampowered.com/app/526870)

*This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*

---

*Last updated: June 2026 — Compatible with Satisfactory 1.0. Guide by [Factory Game Guides](https://game-guide.club)*
