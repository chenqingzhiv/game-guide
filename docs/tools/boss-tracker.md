---
title: "Valheim Boss Progression Tracker"
description: "Interactive Valheim boss tracker — track kill status, boss drops, spawn items, and recommended gear for all 6 Forsaken."
---

# ⚔️ Valheim Boss Progression Tracker

Track which bosses you've defeated, see spawn requirements, loot drops, and recommended gear for each biome.

<div id="boss-tracker">
  <div style="display:grid; gap:12px; margin:20px 0;">
    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">🌲 Eikthyr</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Meadows</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="eikthyr">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 2 Deer Trophy + 1 Greydwarf Eye</div>
        <div><span style="color:#64748b;">Drops:</span> Hard Antler, Deer Trophy</div>
        <div><span style="color:#64748b;">Power:</span> +60% Run Speed (3 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Leather / Flint weapons</div>
      </div>
    </div>

    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">🦌 The Elder</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Black Forest</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="elder">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 3 Ancient Seed at Altar</div>
        <div><span style="color:#64748b;">Drops:</span> Elder Trophy, Swamp Key</div>
        <div><span style="color:#64748b;">Power:</span> +35% Wood Cutting (5 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Bronze weapons / Finewood bow</div>
      </div>
    </div>

    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">🐍 Bonemass</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Swamp</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="bonemass">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 10 Withered Bone at Skull</div>
        <div><span style="color:#64748b;">Drops:</span> Bonemass Trophy, Wishbone</div>
        <div><span style="color:#64748b;">Power:</span> +75% Resist Blunt/Pierce (3 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Iron weapons / Poison resist mead</div>
      </div>
    </div>

    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">🔥 Moder</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Mountain</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="moder">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 3 Dragon Tear at Altar</div>
        <div><span style="color:#64748b;">Drops:</span> Moder Trophy, Dragon Tear</div>
        <div><span style="color:#64748b;">Power:</span> Wind always at your back (3 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Silver weapons / Wolf fur chest</div>
      </div>
    </div>

    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">💀 Yagluth</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Plains</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="yagluth">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 5 Fuling Totem at Altar</div>
        <div><span style="color:#64748b;">Drops:</span> Yagluth Trophy, Yagluth Thing</div>
        <div><span style="color:#64748b;">Power:</span> +75% Resist Magic (3 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Blackmetal / Padded armor</div>
      </div>
    </div>

    <div class="boss-card" style="padding:16px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <div>
          <span style="font-weight:700; font-size:1.1rem;">🕯️ The Queen</span>
          <span style="font-size:0.75rem; color:#475569; margin-left:8px;">Mistlands</span>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <span class="boss-status" style="padding:3px 10px; border-radius:999px; font-size:0.7rem; font-weight:600; background:rgba(34,197,94,0.1); color:#22c55e;">Undefeated</span>
          <button class="toggle-boss" style="padding:6px 14px; border-radius:6px; font-size:0.75rem; cursor:pointer; background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.2); color:#f97316;" data-boss="queen">Toggle</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:10px; font-size:0.8rem;">
        <div><span style="color:#64748b;">Spawn:</span> 9 Seal Fragment at Infested Citadel</div>
        <div><span style="color:#64748b;">Drops:</span> Queen Trophy, Seal Breaker</div>
        <div><span style="color:#64748b;">Power:</span> +50% Mining / +5 Comfy (3 min)</div>
        <div><span style="color:#64748b;">Gear:</span> Carapace / Mage weapons</div>
      </div>
    </div>
  </div>

  <div id="progress-bar" style="padding:16px; background:rgba(255,255,255,0.03); border-radius:12px; text-align:center;">
    <div style="font-size:0.85rem; color:#64748b; margin-bottom:8px;">🏆 Boss Progression</div>
    <div style="height:24px; background:rgba(255,255,255,0.05); border-radius:12px; overflow:hidden; max-width:400px; margin:0 auto;">
      <div id="progress-fill" style="height:100%; width:0%; background:linear-gradient(90deg,#f97316,#ea580c); border-radius:12px; transition:width 0.5s;"></div>
    </div>
    <div id="progress-text" style="font-size:0.8rem; color:#64748b; margin-top:8px;">0 / 6 defeated</div>
  </div>
</div>

<script src="../assets/js/tools/boss-tracker.js"></script>
