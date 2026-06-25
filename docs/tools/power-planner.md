---
title: "Power Grid Planner & Guide"
description: "Interactive power grid planner for Satisfactory, Factorio, and Dyson Sphere Program — compare generators, fuel types, and consumption rates. Includes detailed power plant design tables."
---

# ⚡ Power Grid Planner & Guide

*Last updated: June 2026*

---

The Power Grid Planner helps you design stable power systems across factory games. Calculate total MW draw, fuel consumption rates, and generator counts. This page includes the interactive calculator and comprehensive reference tables for every power source type.

---

## How to Use the Planner

The interactive tool below simplifies power plant design:

1. **Select a Game** — Choose Satisfactory or Dyson Sphere Program (Factorio uses a different boiler→steam engine model coming in a separate tool).
2. **Pick a Power Source** — Options update based on the game: Coal, Fuel, Nuclear, Geothermal, or Solar.
3. **Set Your Target Power Draw** — Enter the total MW your factory needs (1 to 100,000 MW).
4. **Click "Calculate"** — The results show:
   - **Number of generators** needed
   - **Fuel consumption rate** (coal/min, fuel/m³, or uranium/min)
   - **Water requirements** (for steam-based power)
   - **Support buildings** (water extractors, miners, refineries)
   - **Total footprint** estimate

**Pro Tip:** Always build 20–30% over your current demand. Factory expansion happens faster than you expect, and a brownout cascade is hard to recover from.

---

## ⚙️ Generator Comparison by Game

### Satisfactory Power Sources

| Generator Type | Output per Unit | Fuel Type | Fuel Rate | Water Needed | Unlock Tier |
|:---------------|:---------------|:----------|:----------|:-------------|:------------|
| Coal Generator | 75 MW | Coal | 15 Coal/min | 45 m³/min | Tier 3 |
| Fuel Generator | 150 MW | Fuel (refined) | 12 m³/min | — | Tier 5 |
| Turbo Fuel Generator | 150 MW | Turbo Fuel | 4.5 m³/min | — | Tier 6 (alt recipe) |
| Nuclear Power Plant | 2500 MW | Uranium Fuel Rods | 0.2 Rods/min | 240 m³/min | Tier 8 |
| Geothermal Generator | Variable (100–630 MW) | Heat (geyser) | — | — | Tier 6 |

#### Coal Power Plant Design

| Target MW | Coal Generators | Water Extractors | Coal Miners (Normal) | Coal / min |
|:----------|:----------------|:-----------------|:---------------------|:-----------|
| 300 MW | 4 | 3 | 1 Mk.1 (60 coal) | 60 |
| 600 MW | 8 | 6 | 1 Mk.2 (120 coal) | 120 |
| 900 MW | 12 | 9 | 2 Mk.1 or 1 Mk.3 | 180 |
| 1500 MW | 20 | 15 | 2 Mk.2 (240 coal) | 300 |
| 3000 MW | 40 | 30 | 4 Mk.2 or 2 Mk.3 | 600 |

**Coal Plant Pipe Layout:** The classic ratio is **8 Coal Generators : 3 Water Extractors**. Each water extractor produces 120 m³/min, and each generator consumes 45 m³/min. 3 × 120 = 360 m³/min feeds exactly 8 generators (8 × 45 = 360). Use Mk.1 pipes (300 m³/min limit) with two separate water lines for groups of 4 generators.

#### Fuel Generator Plant Design

| Target MW | Fuel Generators | Fuel Refineries | Crude Oil Nodes | Fuel / min |
|:----------|:---------------|:----------------|:----------------|:-----------|
| 600 MW | 4 | 6 (heavy→fuel) | 1 Normal (120 crude) | 48 m³/min |
| 1500 MW | 10 | 15 | 1 Pure (240 crude) | 120 m³/min |
| 3000 MW | 20 | 30 | 2 Pure or 1 Impure | 240 m³/min |
| 6000 MW | 40 | 60 | 4 Pure or 2 Impure | 480 m³/min |

**Fuel Processing Chain:** Crude Oil → Refinery → Heavy Oil Residue (byproduct) + Fuel + Polymer Resin. Each refinery processing 60 crude/min produces 40 fuel/min + 30 HOR/min. The HOR can be recycled into more fuel using the Residual Fuel alt recipe (4 HOR → 2 Fuel).

#### Nuclear Power Plant Design

| Target MW | Plants | Water Extractors | Fuel Rods/min | Waste/min |
|:----------|:-------|:----------------|:--------------|:----------|
| 2500 MW | 1 | 5 (600 m³/min) | 0.2 | 10 |
| 5000 MW | 2 | 10 | 0.4 | 20 |
| 10,000 MW | 4 | 20 | 0.8 | 40 |
| 25,000 MW | 10 | 50 | 2.0 | 100 |

**Nuclear Warning:** Each plant produces 50 waste/min that must be stored or reprocessed. A single plant running for 10 hours = 500 waste canisters. Plan storage accordingly.

#### Geothermal Generator Output

| Geyser Purity | Generator Output | Number on Map |
|:--------------|:----------------|:--------------|
| Pure | 630 MW | 2 |
| High | 310 MW | 8 |
| Normal | 150 MW | 14 |
| Low | 100 MW | 10 |
| **Total** | **~5,780 MW** | **34 geysers** |

---

### Dyson Sphere Program Power Sources

| Generator Type | Output | Fuel Type | Consumption | Notes |
|:---------------|:-------|:----------|:-------------|:------|
| Wind Turbine | 0.3 MW | Wind | — | Wind % varies by planet (20%–100%) |
| Thermal Power Plant | 2.16 MW | Coal/Graphite/etc. | 10 Coal/min or 7 Graphite/min | Most common early power |
| Solar Panel | 0.36 MW | Solar | — | 100% on inner planets, 0% on dark side |
| Mini Fusion Power Plant | 9.0 MW | Deuterium Fuel Rods | 0.3 Rods/min | Mid-game stable power |
| Artificial Sun | 25.0 MW | Antimatter Fuel Rods | 0.15 Rods/min | Endgame power plant |
| Dyson Sphere Reception | Variable (100+ MW) | Ray receivers | — | Depends on sphere output |
| Energy Exchanger | Variable | Accumulators | — | Charge/discharge accumulators |

#### Thermal Power Plant Fuel Comparison

| Fuel Type | Energy per Item (MJ) | Burn Time | Power Plant Output | Items/min per Plant |
|:----------|:---------------------|:----------|:-------------------|:--------------------|
| Coal | 8 MJ | 3.7s | 2.16 MW | 16.2/min |
| Graphite | 16 MJ | 7.4s | 2.16 MW | 8.1/min |
| Crude Oil | 4 MJ | 1.85s | 2.16 MW | 32.4/min |
| Refined Oil | 8 MJ | 3.7s | 2.16 MW | 16.2/min |
| Hydrogen | 8 MJ | 3.7s | 2.16 MW | 16.2/min |
| Deuteron Fuel Rod | 600 MJ | 277s | 2.16 MW | 0.22/min |
| Antimatter Fuel Rod | 7500 MJ | 3472s | 2.16 MW | 0.017/min (1 per ~58 min) |
| Nuclear Fuel Rod | 6000 MJ | 2777s | 2.16 MW | 0.022/min |

**Early Game Power Strategy (DSP):**
- Start with 3–4 Wind Turbines (0.3 MW each, 1.2 MW total)
- Add 4 Thermal Power Plants burning coal (8.64 MW total) before your first major factory
- Transition to Mini Fusion (9 MW per plant) once you reach purple science
- Endgame: build Artificial Suns (25 MW each) and a Dyson Sphere

---

### Factorio Power Sources

Although the interactive calculator does not yet support Factorio (its boiler→steam engine model requires a separate calculation approach), here is the reference data for planning:

| Power Source | Output per Unit | Fuel | Optimal Ratio |
|:-------------|:---------------|:-----|:--------------|
| Boiler + Steam Engine | 1.8 MW (2 engines per boiler) | Any burnable fuel | 1 Offshore Pump : 20 Boilers : 40 Steam Engines |
| Nuclear Reactor | 40 MW (base, +300% adjacency) | Uranium Fuel Cells | 1 Reactor : 4 Heat Exchangers : 7 Steam Turbines |
| Solar Panel | 60 kW | Sunlight | 0.84 Solar : 1 Accumulator (day/night) |

#### Steam Power Layout (Classic 1:20:40)

| Target MW | Offshore Pumps | Boilers | Steam Engines | Fuel (Coal/min) |
|:----------|:---------------|:--------|:--------------|:----------------|
| 18 MW | 1 | 20 | 40 | 180 Coal/min |
| 36 MW | 2 | 40 | 80 | 360 Coal/min |
| 72 MW | 4 | 80 | 160 | 720 Coal/min |
| 180 MW | 10 | 200 | 400 | 1800 Coal/min |

**Rule of Thumb:** Each boiler consumes 3.6 Coal/min. One yellow belt of coal (480/min) feeds ~133 boilers = ~120 MW.

#### Nuclear Reactor Adjacency Bonus

| Reactor Configuration | Total Heat Output | Reactors | Heat per Reactor |
|:----------------------|:------------------|:---------|:-----------------|
| Single | 40 MW | 1 | 40 MW |
| 2×1 (side by side) | 120 MW | 2 | 60 MW |
| 2×2 (square) | 480 MW | 4 | 120 MW |
| 2×3 | 800 MW | 6 | 133 MW |

**Nuclear Heat Exchange Ratio:** Each Heat Exchanger needs 10 MW of heat. A 2×2 reactor (480 MW) needs exactly 48 Heat Exchangers, which produce 48 × 103.09 = ~4,950 steam/s. This needs 85 Steam Turbines (each consumes 60 steam/s).

#### Solar Panel & Accumulator Ratio

| Target MW | Solar Panels | Accumulators | Space Required |
|:----------|:-------------|:--------------|:---------------|
| 10 MW | 167 | 139 | ~400 tiles |
| 50 MW | 834 | 695 | ~2,000 tiles |
| 100 MW | 1,667 | 1,389 | ~4,000 tiles |
| 1 GW | 16,667 | 13,889 | ~40,000 tiles (10 chunks) |

---

## ⚡ Power Consumption Reference Tables

### Satisfactory Machine Consumption (MW)

| Machine | Power | Clock Speed Adjustment |
|:--------|:------|:----------------------|
| Constructor | 4 MW | P = 4 × (S/100)^1.3219 |
| Assembler | 15 MW | P = 15 × (S/100)^1.3219 |
| Manufacturer | 75 MW | P = 75 × (S/100)^1.3219 |
| Refinery | 30 MW | P = 30 × (S/100)^1.3219 |
| Blender | 75 MW | P = 75 × (S/100)^1.3219 |
| Particle Accelerator | 500–1500 MW | Mode dependant |
| Miner Mk.1 | 5 MW | Fixed per node |
| Miner Mk.2 | 12 MW | Fixed per node |
| Miner Mk.3 | 30 MW | Fixed per node |
| Oil Extractor | 10–40 MW | Purity dependant |
| Water Extractor | 20 MW | Fixed |

### Satisfactory Average Factory Consumption By Phase

| Phase | Typical MW Draw | Power Source Needed |
|:------|:----------------|:--------------------|
| Tier 1–2 (Hub upgrades) | 20–50 MW | Biomass (temporary) |
| Tier 3–4 (Coal power) | 50–200 MW | Coal generators |
| Tier 5–6 (Fuel power) | 200–1000 MW | Fuel generators |
| Tier 7–8 (Nuclear) | 1000–5000 MW | Nuclear plant(s) |
| Endgame mega-base | 10,000–50,000+ MW | Nuclear + Geothermal |

### DSP Planet Power Guide

| Planet Type | Recommended Power | Best Source |
|:------------|:------------------|:------------|
| Starting planet (Grass) | 10–30 MW | Coal thermal → Mini fusion |
| Desert planet | 30–100 MW | Solar (high wind/solar%) |
| Lava planet | 50–100 MW | Geothermal / Solar |
| Ice planet | 20–50 MW | Wind turbines + thermal |
| Ocean planet | 10–30 MW | Wind turbines |
| Sulfuric planet | 30–80 MW | Thermal (coal from imports) |

### DSP Machine Consumption (per unit)

| Machine | Power Draw |
|:--------|:-----------|
| Mining Machine | 0.5 MW |
| Smelter | 0.3 MW |
| Assembler Mk.I | 0.3 MW |
| Assembler Mk.II | 0.5 MW |
| Assembler Mk.III | 1.0 MW |
| Oil Refinery | 1.0 MW |
| Chemical Plant | 0.8 MW |
| Matrix Lab | 1.5 MW |
| Ray Receiver | 3.0–15.0 MW |
| Energy Exchanger | 4.0 MW |
| Orbital Collector | 5.0 MW |
| Vertical Launching Silo | 6.0 MW |

---

## Power Grid Design Tips

1. **Build in expandable blocks.** A modular power plant design (e.g., 4 coal generators + 3 water extractors + 1 miner in Satisfactory) lets you copy-paste the same blueprint as your factory grows.
2. **Over-provision by 30%.** If your factory draws 200 MW, build 260 MW of generation. Power spikes from Particle Accelerators (Satisfactory) or lab rushes (DSP/ Factorio) can cause instantaneous demand surges.
3. **Battery banks save factories.** In DSP, a bank of 100+ Accumulators (or an Energy Exchanger setup) smooths out demand. In Satisfactory, Power Storage buildings (100 MWh each) give you 30+ seconds to fix a brownout.
4. **Fuel logistics matter more than generators.** A full coal belt feeding 8 generators is useless if the miners run out of power (cascade failure). Solved in Satisfactory with a priority power switch for miners. In DSP, use separate power grids for miners and factories.
5. **Use priority switches.** If you have multiple power plants, use circuit conditions (Factorio's switch, Satisfactory's priority system) to ensure fuel production stays online even when the main grid is overloaded.

---

<div id="power-planner">
  <div style="display:flex; flex-wrap:wrap; gap:16px; margin:20px 0; padding:20px; background:rgba(255,255,255,0.05); border-radius:12px;">
    <div>
      <label><strong>Game</strong></label><br>
      <select id="game-select" style="padding:8px 16px; border-radius:8px; font-size:1em; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="satisfactory">⚙️ Satisfactory</option>
        <option value="dsp">🌌 Dyson Sphere Program</option>
      </select>
    </div>
    <div>
      <label><strong>Power Source</strong></label><br>
      <select id="power-select" style="padding:8px 16px; border-radius:8px; font-size:1em; min-width:180px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="">— Select a game first —</option>
      </select>
    </div>
    <div>
      <label><strong>Target power draw</strong></label><br>
      <div style="display:flex; gap:8px; align-items:center;">
        <input type="number" id="target-mw" value="100" min="1" max="100000" style="padding:8px; border-radius:8px; font-size:1em; width:120px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <span style="opacity:0.7;">MW</span>
      </div>
    </div>
    <div style="display:flex; align-items:flex-end;">
      <button id="calc-btn" style="padding:8px 24px; border-radius:8px; font-size:1em; font-weight:600; background:linear-gradient(135deg,#f97316,#ea580c); color:#fff; border:none; cursor:pointer;">Calculate</button>
    </div>
  </div>

  <div id="results" style="display:none;">
    <h3>📊 Results</h3>
    <div id="result-summary" style="padding:16px; background:rgba(249,115,22,0.05); border:1px solid rgba(249,115,22,0.2); border-radius:12px; margin-bottom:16px;"></div>
    <div id="detail-section" style="padding:16px; background:rgba(255,255,255,0.03); border-radius:12px;">
      <h4 style="margin-top:0;">📋 Fuel Requirements</h4>
      <div id="fuel-output"></div>
    </div>
  </div>
</div>

<script src="../assets/js/tools/power-planner.js"></script>
