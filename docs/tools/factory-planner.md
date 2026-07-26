---
title: "Factory Planner — Production Line Visualizer"
description: "Interactive production line visualizer for Satisfactory, Factorio, Dyson Sphere Program, and Timberborn — step-by-step vertical production chains with raw input calculations."
---

# 🔧 Factory Planner / Production Line Visualizer

**See the full production chain, step by step.** Select your game and target item, then walk through every stage from raw ore to finished product. Enter your desired output rate to get exact raw material requirements.

> 📐 **Data source:** Satisfactory Wiki (v1.0), Factorio Space Age Wiki, DSP Wiki (v0.10), Timberborn Wiki (v0.5)

<div id="fp-planner">
  <div style="display:flex; flex-wrap:wrap; gap:16px; margin:20px 0; padding:20px; background:rgba(255,255,255,0.05); border-radius:12px;">
    <div>
      <label><strong>🎮 Game</strong></label><br>
      <select id="fp-game-select" style="padding:8px 16px; border-radius:8px; font-size:1em; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="">— Select a game —</option>
        <option value="satisfactory">⚙️ Satisfactory</option>
        <option value="factorio">💡 Factorio</option>
        <option value="dsp">🌌 Dyson Sphere Program</option>
        <option value="timberborn">🌳 Timberborn</option>
      </select>
    </div>
    <div>
      <label><strong>🏭 Target Item</strong></label><br>
      <select id="fp-item-select" style="padding:8px 16px; border-radius:8px; font-size:1em; min-width:240px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="">— Select a game first —</option>
      </select>
    </div>
    <div>
      <label><strong>📊 Desired Output Rate</strong></label><br>
      <div style="display:flex; gap:8px; align-items:center;">
        <input type="number" id="fp-target-rate" value="60" min="0.1" max="100000" step="0.1" style="padding:8px; border-radius:8px; font-size:1em; width:120px; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <span id="fp-rate-unit" style="opacity:0.7;">/ min</span>
      </div>
    </div>
    <div style="display:flex; align-items:flex-end;">
      <button id="fp-calc-btn" style="padding:8px 24px; border-radius:8px; font-size:1em; font-weight:600; background:linear-gradient(135deg,#f97316,#ea580c); color:#fff; border:none; cursor:pointer;">Calculate</button>
    </div>
  </div>

  <div id="fp-results" style="display:none;">
    <h3>📋 Production Chain</h3>
    <div id="fp-chain-display" style="margin-bottom:24px;"></div>

    <h3>📊 Resource Summary</h3>
    <div id="fp-summary" style="padding:16px; background:rgba(249,115,22,0.05); border:1px solid rgba(249,115,22,0.2); border-radius:12px;"></div>
  </div>
</div>

---

## How It Works

1. **Select a game** — the item dropdown fills with end-game and advanced items
2. **Pick your target item** — see the full step-by-step vertical production chain
3. **Enter your desired output rate** — raw material requirements are calculated automatically

### Games & Items Included

| Game | End-Game / Advanced Items |
|------|--------------------------|
| ⚙️ **Satisfactory** | Supercomputer, Turbo Motor, Assembly Director System, Magnetic Field Generator, Thermal Propulsion Rocket, Automated Wiring, Modular Engine, Adaptive Control Unit |
| 💡 **Factorio** | Science Packs (Red, Green, Military, Purple, Yellow, Space), Green Circuit, Red Circuit, Blue Circuit, Engine Unit, Electric Engine Unit |
| 🌌 **Dyson Sphere Program** | Processor, Quantum Chip, Titanium Alloy, Particle Container, Graviton Lens |
| 🌳 **Timberborn** | Mechanical Pump, Large Water Wheel, Engine, Mine, Deep Mine, Observatory |

---

**Data source:** Satisfactory Official Wiki (v1.0), Factorio Official Wiki (Space Age), Dyson Sphere Program Official Wiki (v0.10), Timberborn Official Wiki (v0.5)

<script src="../assets/js/tools/factory-planner.js"></script>
