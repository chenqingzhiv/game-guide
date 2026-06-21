---
title: "Factory Production Ratio Calculator"
description: "Interactive production ratio calculator for Satisfactory, Factorio, and Dyson Sphere Program — plan machine counts, belt speeds, and input materials."
---

# 🧮 Production Ratio Calculator

Plan the perfect production line. Select your game, target item, and desired output, then get the exact machine counts, input materials, and belt requirements.

> 📐 **Data source:** Satisfactory Wiki (v1.0), Factorio Official Wiki, DSP Wiki — all base recipes. Alt/advanced recipes not included yet.

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
