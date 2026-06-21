---
title: "Interactive Map Preview — Region & Resource Guide"
description: "Interactive region map previews for Satisfactory, Factorio, and Dyson Sphere Program — explore biomes, resource nodes, and recommended starting locations."
---

# 🗺️ Interactive Map Preview

**Explore game regions and plan your next outpost.** Click on any region to see detailed resource information, node counts, and strategic tips. This is a simplified reference tool — not a real-time interactive game map.

> 📐 **Data source:** Satisfactory Wiki (v1.0), Factorio Official Wiki (Space Age), DSP Official Wiki (v0.10)

<div id="map-container">
  <div style="display:flex; flex-wrap:wrap; gap:16px; margin:20px 0; padding:20px; background:rgba(255,255,255,0.05); border-radius:12px;">
    <div>
      <label><strong>🎮 Game</strong></label><br>
      <select id="map-game-select" style="padding:8px 16px; border-radius:8px; font-size:1em; background:#1a1a2e; color:#e8e6e3; border:1px solid rgba(255,255,255,0.1);">
        <option value="">— Select a game —</option>
        <option value="satisfactory">⚙️ Satisfactory</option>
        <option value="factorio">💡 Factorio</option>
        <option value="dsp">🌌 Dyson Sphere Program</option>
      </select>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
    <div>
      <h3 style="margin-top:0;">🗺️ Regions</h3>
      <div id="map-grid" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:10px;">
        <p style="color:#64748b; grid-column:1/-1;">Select a game above to see the region map.</p>
      </div>
    </div>
    <div>
      <h3 style="margin-top:0;">ℹ️ Region Details</h3>
      <div id="map-region-info">
        <p style="color:#64748b;">Click a region to see detailed resource information.</p>
      </div>
    </div>
  </div>
</div>

---

## Games Included

### ⚙️ Satisfactory — 6 Regions

| Region | Key Resources | Difficulty |
|--------|--------------|-----------|
| 🌿 **Grass Fields** | Iron, Copper, Limestone | Easy |
| 🏜️ **Rocky Desert** | Iron, Copper, Coal | Medium |
| ⏳ **Dune Desert** | Oil, Quartz, Sulfur | Hard |
| 🌲 **Northern Forest** | Iron, Copper, Caterium | Medium |
| 🔵 **Blue Crater** | Nitrogen, Sulfur | Hard |
| 🟥 **Red Jungle** | Bauxite, Uranium | Very Hard |

### 💡 Factorio — Starting Area Layout

The default spawn generates with specific resource patch layouts:
- **Iron** to the north and south
- **Copper** to the east and west
- **Coal** nearby east
- **Stone** nearby west
- **Oil** further out in all directions

### 🌌 Dyson Sphere Program — Starter System (4 Bodies)

| Body | Key Resources | Role |
|------|--------------|------|
| 🌍 **Starting Planet (Gobi)** | Iron, Copper, Stone, Coal, Oil | Main base |
| 🌕 **Moon (Luna)** | Titanium, Silicon | Early expansion |
| 🏜️ **Desert Planet** | Coal, Oil | Fuel & plastic |
| ❄️ **Ice Planet (Glacio)** | Fire Ice, Kimberlite | Rare resources |

---

**Data source:** Satisfactory Official Wiki (v1.0), Factorio Official Wiki (Space Age), Dyson Sphere Program Official Wiki (v0.10)

<script src="../assets/js/tools/game-map.js"></script>
