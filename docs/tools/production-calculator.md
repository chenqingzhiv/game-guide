---
title: "Production Ratio Calculator & Guide"
description: "Interactive production ratio calculator for Satisfactory, Factorio, and Dyson Sphere Program — plan machine counts, belt speeds, and input materials. Includes game-specific ratio tables and optimization tips."
---

# 🧮 Production Ratio Calculator & Guide

*Last updated: June 2026*

---

The Production Ratio Calculator helps you plan optimized production lines across three factory games. Input a target output rate and get exact machine counts, input material requirements, and belt throughput recommendations. This page includes the interactive calculator below, plus comprehensive ratio reference data for each game.

---

## How to Use the Calculator

The interactive tool below works in three simple steps:

1. **Select a Game** — Choose Satisfactory, Factorio, or Dyson Sphere Program from the dropdown. The recipe list updates automatically for each game's unique item set.
2. **Choose an Item / Recipe** — Pick the item you want to produce. The calculator uses base recipes only (alt/advanced recipes are not yet included).
3. **Set Your Target Rate** — Enter the desired output per minute (or per second for Factorio). The minimum is 1, maximum is 10,000.
4. **Click "Calculate"** — The results panel shows:
   - **Number of machines** required (Constructors, Assemblers, Smelters, etc.)
   - **Input material rates** — exactly how much of each ingredient you need per minute
   - **Belt requirements** — which belt tier can handle each material flow
   - **Total power consumption** for the production line
   - **Space estimate** — approximate footprint in foundation tiles

**Pro Tip:** For multi-step production chains (e.g., Reinforced Iron Plates in Satisfactory), calculate each step separately. Start with the raw input stage (smelters), then work forward through each assembly tier.

---

## 🏭 Satisfactory Ratio Reference

### Base Smelting Ratios

| Input | Output | Smelters per Belt | Belt Tiers |
|:------|:-------|:-----------------|:-----------|
| Iron Ore → Iron Ingot | 30 → 30/min | 1 Mk.1 belt feeds 1 smelter | Mk.1 (60/min) supports 2 smelters |
| Copper Ore → Copper Ingot | 30 → 30/min | Same as iron | Mk.2 (120/min) supports 4 smelters |
| Limestone → Concrete | 45 → 15/min | 1 smelter per 45 ore input | Mk.3 (270/min) supports 9 smelters |
| Caterium Ore → Caterium Ingot | 45 → 30/min | 2 smelters per Mk.2 belt | Mk.4 (480/min) supports 16 smelters |

### Key Production Ratios

| Item | Machines Required | Input Rate | Output Rate | Power (MW) |
|:-----|:-----------------|:-----------|:------------|:-----------|
| Iron Plate (30/min) | 2 Constructors | 60 Iron Ingots/min | 30 Plates/min | 8 MW |
| Screw (120/min) | 2 Constructors | 40 Iron Rods/min | 120 Screws/min | 8 MW |
| Reinforced Iron Plate (5/min) | 1 Assembler | 30 Plates + 60 Screws/min | 5 RIPs/min | 15 MW |
| Rotor (4/min) | 1 Assembler | 20 Rods + 100 Screws/min | 4 Rotors/min | 15 MW |
| Cable (60/min) | 2 Constructors | 60 Copper Ingots/min | 60 Cables/min | 8 MW |
| Wire (60/min) | 2 Constructors | 60 Copper Ingots/min | 60 Wire/min | 8 MW |
| Modular Frame (2/min) | 1 Assembler | 12 RIPs + 24 Rods/min | 2 Frames/min | 15 MW |
| Steel Beam (15/min) | 1 Constructor | 45 Steel Ingots/min | 15 Beams/min | 8 MW |
| Steel Pipe (20/min) | 1 Constructor | 40 Steel Ingots/min | 20 Pipes/min | 8 MW |
| Motor (2/min) | 1 Assembler | 6 Rotors + 12 Stators/min | 2 Motors/min | 30 MW |

### Manufacturer Recipes

| Item | Inputs (per min) | Output | Power |
|:-----|:-----------------|:-------|:------|
| Heavy Modular Frame | 10 RIP + 30 Pipe + 10 Concrete + 40 Screw | 2/min | 75 MW |
| Computer | 20 Circuit Board + 28 Cable + 4 Plastic | 2.5/min | 75 MW |
| Supercomputer | 20 Computer + 10 AI Limiter + 60 High-Speed Connector + 20 Plastic | 1/min | 225 MW |

---

## 💡 Factorio Ratio Reference

### Smelting

| Ore | Furnace Type | Output per Furnace | Belt (Yellow) | Belt (Red) | Belt (Blue) |
|:----|:-------------|:------------------|:--------------|:------------|:------------|
| Iron Ore | Stone Furnace | 22.5/min | 13 furnaces | 26 furnaces | 39 furnaces |
| Iron Ore | Steel Furnace | 45/min | 7 furnaces | 13 furnaces | 20 furnaces |
| Copper Ore | Stone Furnace | 22.5/min | 13 furnaces | 26 furnaces | 39 furnaces |
| Copper Ore | Steel Furnace | 45/min | 7 furnaces | 13 furnaces | 20 furnaces |
| Steel | Steel Furnace | 22.5/min | 13 furnaces (5 iron:1 steel) | 26 furnaces | 39 furnaces |

### Core Production Chains

| Item | Machines | Input | Output | Notes |
|:-----|:---------|:------|:-------|:------|
| Copper Wire | 1 Assembler (T2) | 1 Copper Plate/s | 2 Wire/s | Speed module candidates |
| Electronic Circuit | 1 Assembler (T2) | 1.5 Wire + 1 Iron Plate/s | 1 Circuit/s | Your first production bottleneck |
| Iron Gear Wheel | 1 Assembler (T2) | 1 Iron Plate/s | 2 Gears/s | One gear assembler feeds ~10 red science assemblers |
| Iron Stick | 1 Assembler (T1) | 1 Iron Plate → 2 Sticks/s | 2 Sticks/s | Used in transport belts |
| Pipe | 1 Assembler (T1) | 1 Iron Plate/s | 2 Pipes/s | For fluid handling |
| Belt (Yellow) | 1 Assembler (T1) | 1 Iron Gear + 1 Plate/s | 2 Belts/0.5s | 1 assembler = 4 belts/s |
| Inserter | 1 Assembler (T2) | 1 Circuit + 1 Gear + 1 Plate/s | 1 Inserter/s | 

### Science Pack Ratios

| Science Pack | Recipe | Materials (per pack) | Optimal Ratio |
|:-------------|:-------|:--------------------|:--------------|
| Red (Automation) | 1 Gear + 1 Plate | 1 Iron Plate, 1 Gear | 5 assemblers (10/s for 1/s) |
| Green (Logistic) | 3 Inserter + 1 Belt | 1.5 Circuit + 1 Gear + 1 Plate | 6 assemblers (12/s for 2/s) |
| Gray (Military) | 1 Piercing Round + 1 Grenade | 1 Plate + 1 Copper + 1 Coal + 1 Iron + 1 Steel | 3 assemblers per 1/s |
| Blue (Chemical) | 1 Engine + 1 Red Circuit + 1 Sulfur | 2 Pipe + 1 Gear + 4.5 Copper + 2 Plastic + 1.5 Iron | 1 assembler per 1/s |
| Purple (Production) | 1 Electric Furnace + 1 Productivity 1 | 20 Iron + 5 Copper + 10 Circuit + 5 Plastic | 2/s requires 3 assemblers |
| Yellow (Utility) | 1 Express Splitter + 1 Speed 1 | 10 Iron + 7.5 Copper + 2 Circuit + 2 Plastic + 1 Battery | 1/s requires 2 assemblers |

### Classic 1 Science Per Second Setup

| Item | Assemblers Needed | Input Materials / min |
|:-----|:-----------------|:---------------------|
| Red Science | 5 | 60 Iron Plates, 60 Gears |
| Green Science | 6 | 90 Iron, 90 Copper, 45 Circuits |
| Total iron demand | — | ~150 Iron Plates/min (3 steel furnaces on iron) |
| Total copper demand | — | ~90 Copper Plates/min (2 steel furnaces on copper) |

---

## 🌌 Dyson Sphere Program Ratio Reference

### Basic Smelting

| Ore | Smelter Output | Smelters per Mk.I Belt | Smelters per Mk.II Belt |
|:----|:---------------|:----------------------|:-----------------------|
| Iron Ore → Iron Ingot | 60/min | 1 (60/min belt cap) | 2 (120/min) |
| Copper Ore → Copper Ingot | 60/min | 1 | 2 |
| Stone → Stone Brick | 60/min | 1 | 2 |
| Coal → Graphite | 60/min | 1 | 2 |

### Core Production Ratios

| Item | Machines | Input Rate | Output Rate | Notes |
|:-----|:---------|:-----------|:------------|:------|
| Magnetic Coil | 1 Assembler | 60 Iron + 30 Copper/min | 30 Coils/min | Early game bottleneck |
| Circuit Board | 1 Assembler | 60 Iron + 30 Copper/min | 30 Boards/min | Rush this |
| Gear | 1 Assembler | 60 Iron/min | 120 Gears/min | 2:1 ratio vs iron input |
| Prism | 1 Assembler | 30 Glass/min | 30 Prisms/min | Glass needs stone smelting first |
| Plasma Exciter | 1 Assembler | 30 Prism + 15 Coil/min | 15 Exciter/min | Mid-game component |
| Processor | 1 Assembler | 30 Board + 15 Microchip/min | 15 Processors/min | Your first big bottleneck |
| Particle Container | 1 Assembler | 30 Graphene + 15 Copper/min | 10 Containers/min | Unlock with yellow science |

### Matrix Lab (Science) Ratios

| Matrix | Color | Recipe | Labs for 1/s | Notes |
|:-------|:------|:-------|:-------------|:------|
| Energy Matrix | Blue | 1 Coal + 1 Magnet → 2 Matrix | 1 Lab | First science — rush to automate |
| Electromagnetic Matrix | Red | 2 Circuit + 1 Coil → 2 Matrix | 2 Labs | Requires circuit automation |
| Matter Matrix | Yellow | 1 Processor + 1 Prism + 1 Diamond → 2 Matrix | 2 Labs | Processor bottleneck is real |
| Information Matrix | Purple | 1 Chip + 1 Processor + 1 Plastic → 2 Matrix | 3 Labs | Endgame science requirement |
| Gravity Matrix | Green | 1 Graviton + 1 Processor + 1 Particle Container | 4 Labs | Endgame |

### Optimal Science Setup (1 Matrix / s each)

| Color | Labs | Supporting Factory Requirement |
|:------|:-----|:------------------------------|
| Blue | 1 | 60 Coal + 60 Magnet/min (one miner each) |
| Red | 2 | 120 Circuit + 60 Coil/min (4 assemblers) |
| Yellow | 2 | 30 Processor + 30 Prism + 15 Diamond/min |
| Purple | 3 | Heavy processor + microchip factory |
| Green | 4 | Full endgame factory with interstellar logistics |

---

## ⚡ Power Consumption Reference

### Satisfactory

| Building | Base Power (MW) | Clock Speed Scaling |
|:---------|:---------------|:-------------------|
| Constructor | 4 | Linearly proportional |
| Assembler | 15 | Linearly proportional |
| Manufacturer | 75 | Linearly proportional |
| Refinery | 30 | Linearly proportional |
| Smelter | 4 | Linearly proportional |
| Foundry | 16 | Linearly proportional |
| Miner Mk.1 | 5 | Fixed per node purity |
| Miner Mk.2 | 12 | Fixed per node purity |
| Miner Mk.3 | 30 | Fixed per node purity |
| Oil Extractor | 20 | Fixed per node purity |

### Factorio

| Building | Power (kW) | Power While Idle |
|:---------|:-----------|:-----------------|
| Stone Furnace | 90 kW | 6 kW |
| Steel Furnace | 180 kW | 12 kW |
| Assembling Machine 1 | 75 kW | 3.75 kW |
| Assembling Machine 2 | 150 kW | 7.5 kW |
| Assembling Machine 3 | 375 kW | 18.75 kW |
| Chemical Plant | 210 kW | 10.5 kW |
| Electric Mining Drill | 90 kW | 18 kW |

### Dyson Sphere Program

| Building | Power (MW) | Notes |
|:---------|:-----------|:------|
| Mining Machine | 0.5 | Per unit |
| Smelter | 0.3 | Base consumption |
| Assembler I | 0.3 | Early game |
| Assembler II | 0.5 | Upgraded version |
| Assembler III | 1.0 | Endgame |
| Oil Refinery | 1.0 | Fluid processing |
| Chemical Plant | 0.8 | Advanced refining |
| Matrix Lab | 1.5 | Science production |
| Energy Exchanger | 4.0 | Accumulator charging |

---

## Optimization Tips by Game

### Satisfactory

- **Underclock to save power.** A Constructor at 50% clock speed uses only 2.5 MW (not 50% of 4 MW — it's actually less!). Power scales with clock speed^1.3219.
- **Belt bottlenecks are common.** Always check the input/output rates in the calculator. A single Mk.1 belt (60/min) can only feed 2 smelters.
- **Use manifolds.** Instead of splitting belts evenly, let one long belt feed machines sequentially. It takes time to fill up but requires fewer splitters.

### Factorio

- **Direct insertion** saves belt throughput. Feed Copper Wire directly into Green Circuit assemblers without belting it.
- **Priority splitting** using splitter output filters helps manage multi-output production blocks.
- **Ratio perfection** matters for science. A 5:6:12 (Red:Green:Blue) ratio is a common early-game template.
- **Use the calculator** for complex chains like Purple/Yellow science where sub-component ratios multiply.

### Dyson Sphere Program

- **Smelters first.** Before building any complex chain, set up automated smelting of iron, copper, stone, and coal.
- **Interstellar logistics** changes everything. Once you have ILS towers, production becomes about throughput, not adjacency.
- **Matrix labs** consume massive power. A single 1/s science setup pulls 5+ MW from your grid.
- **Build ratios matter early.** A 2:1 assembler ratio (Circuit Board → Processor) is the most common bottleneck spot.

---

<div id="ratio-calc">
  <div style="display:flex; flex-wrap:wrap; gap:16px; margin:20px 0; padding:20px; background:rgba(255,255,255,0.05); border-radius:12px;">
    <div>
      <label><strong>Game</strong></label><br>
      <select id="game-select" style="padding:8px 16px; border-radius:8px; font-size:1em; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="satisfactory">⚙️ Satisfactory</option>
        <option value="factorio">💡 Factorio</option>
        <option value="dsp">🌌 Dyson Sphere Program</option>
      </select>
    </div>
    <div>
      <label><strong>Item / Recipe</strong></label><br>
      <select id="recipe-select" style="padding:8px 16px; border-radius:8px; font-size:1em; min-width:200px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="">— Select a game first —</option>
      </select>
    </div>
    <div>
      <label><strong>Target output rate</strong></label><br>
      <div style="display:flex; gap:8px; align-items:center;">
        <input type="number" id="target-rate" value="60" min="1" max="10000" style="padding:8px; border-radius:8px; font-size:1em; width:100px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <span id="rate-unit" style="opacity:0.7;">/ min</span>
      </div>
    </div>
    <div style="display:flex; align-items:flex-end;">
      <button id="calc-btn" style="padding:8px 24px; border-radius:8px; font-size:1em; font-weight:600; background:linear-gradient(135deg,#f97316,#ea580c); color:#fff; border:none; cursor:pointer;">Calculate</button>
    </div>
  </div>

  <div id="results" style="display:none;">
    <h3>📊 Results</h3>
    <div id="result-summary" style="padding:16px; background:rgba(249,115,22,0.05); border:1px solid rgba(249,115,22,0.2); border-radius:12px; margin-bottom:16px;"></div>
    <div id="recipe-detail" style="padding:16px; background:rgba(255,255,255,0.03); border-radius:12px;">
      <h4 style="margin-top:0;">📋 Production Chain</h4>
      <div id="chain-output"></div>
    </div>
  </div>
</div>

<script src="../assets/js/tools/production-calc.js"></script>
