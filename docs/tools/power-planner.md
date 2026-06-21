---
title: "Factory Power Grid Planner"
description: "Interactive power grid planner for Satisfactory, Factorio, and Dyson Sphere Program — compare coal, fuel, nuclear, and renewable power sources."
---

# ⚡ Power Grid Planner

Design a stable power grid. Calculate total MW draw, fuel consumption rates, and generator counts for Satisfactory and Dyson Sphere Program.

> 📐 **Data source:** Satisfactory Wiki (v1.0) & DSP Wiki. Factorio not included — its boiler → steam engine chain requires a different calculation model. We'll add a dedicated Factorio power tool separately.

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
