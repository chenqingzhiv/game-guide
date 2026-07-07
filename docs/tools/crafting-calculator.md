---
title: "Survival Crafting Calculator & Recipe Reference"
description: "Interactive crafting calculator for 5 survival games — plan materials, check recipes, and calculate required quantities for Valheim, Enshrouded, V Rising, Sons of the Forest & Grounded."
tags: [crafting, calculator, survival, valheim, enshrouded, v rising, sons of the forest, grounded, guide]
---

# 🛠️ Survival Crafting Calculator & Recipe Reference

**Plan your next crafting run across 5 survival games.** Select a game, pick an item, and see exactly what materials you need. All data sourced from official game Wikis, verified July 2026.

> **Data source:** Official game Wikis, verified as of July 2026

---

<style>
.tool-tabs {
  display: flex;
  gap: 0;
  margin: 0 0 24px;
  border-bottom: 2px solid rgba(255,255,255,0.08);
}
.tool-tabs input[type="radio"] { display: none; }
.tool-tabs label {
  padding: 12px 24px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: all 0.2s;
}
.tool-tabs label:hover { color: rgba(255,255,255,0.8); }
.tool-tabs input:checked + label { color: #22c55e; border-bottom-color: #22c55e; }
.tool-tab-content { animation: fadeIn 0.2s ease; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}
.calc-card {
  padding: 20px;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  margin: 16px 0;
}
.calc-card label {
  display: block;
  font-weight: 600;
  margin-bottom: 6px;
  font-size: 0.9rem;
  color: rgba(255,255,255,0.8);
}
.calc-card select, .calc-card input {
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 0.95rem;
  background: #1a1a2e;
  color: #e8e6e3;
  border: 1px solid rgba(255,255,255,0.1);
  margin-bottom: 10px;
}
.calc-card button {
  padding: 10px 24px;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  background: rgba(34,197,94,0.15);
  border: 1px solid rgba(34,197,94,0.3);
  color: #22c55e;
  transition: all 0.2s;
}
.calc-card button:hover {
  background: rgba(34,197,94,0.25);
}
#calc-result {
  margin-top: 16px;
  padding: 16px;
  border-radius: 8px;
  background: rgba(34,197,94,0.06);
  border: 1px solid rgba(34,197,94,0.1);
  min-height: 60px;
}
.calc-result-item {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid rgba(255,255,255,0.04);
}
.calc-result-item:last-child { border-bottom: none; }
.calc-result-mat { color: #22c55e; font-weight: 600; }
.calc-result-qty { color: #e8e6e3; }
</style>

<div class="tool-tabs">
  <input type="radio" name="tooltab" id="tab-calc" checked>
  <label for="tab-calc">📊 Calculator</label>
  <input type="radio" name="tooltab" id="tab-guide">
  <label for="tab-guide">📖 Quick Guide</label>
  <input type="radio" name="tooltab" id="tab-faq">
  <label for="tab-faq">❓ FAQ</label>
</div>

<div class="tool-tab-content" id="content-calc">

<div class="calc-card">
  <label>🎮 Select Game</label>
  <select id="cc-game">
    <option value="">— Select a game —</option>
    <option value="valheim">🌲 Valheim</option>
    <option value="enshrouded">🔥 Enshrouded</option>
    <option value="vrising">🩸 V Rising</option>
    <option value="sons">🌲 Sons of the Forest</option>
    <option value="grounded">🐞 Grounded</option>
  </select>

  <label>📂 Category</label>
  <select id="cc-category">
    <option value="weapon">⚔️ Weapons</option>
    <option value="armor">🛡️ Armor</option>
    <option value="tool">🛠️ Tools</option>
  </select>

  <label>🎯 Item</label>
  <select id="cc-item">
    <option value="">— Select game first —</option>
  </select>

  <label>🔢 Quantity</label>
  <input type="number" id="cc-qty" value="1" min="1" max="100">

  <button onclick="calculateCrafting()">🔨 Calculate Materials</button>
</div>

<div id="calc-result">
  <p style="color: rgba(255,255,255,0.4);">Select a game, item, and quantity, then click Calculate.</p>
</div>

</div>

<div class="tool-tab-content" id="content-guide" style="display:none">

### 📖 Survival Crafting Quick Guide

**Valheim:** Build a Workbench (10 Wood) first. Upgrade it with a Chopping Block and Tanning Rack for better gear. Always keep a Forge near your base for metal processing. Bronze is 2 Copper + 1 Tin.

**Enshrouded:** Start with the Workbench, then build the Blacksmith (rescue him first). The Altar of Flame unlocks larger base areas. Rescuing NPCs unlocks entire crafting categories — prioritize them.

**V Rising:** Castles need Blood Altars and Prison Cells. Unlock recipes by defeating V Blood carriers. Paper presses convert wood into paper. Gem cutting stations convert raw gems.

**Sons of the Forest:** Use the Survival Book (press B) to view all recipe categories. GPS trackers mark cave entrances. The 3D Printer uses Printer Resin found in bunkers.

**Grounded:** Build the Field Station first for research. Scanning resources at the Field Station unlocks recipes. Hide and weed stems are your main building materials. The Spinning Wheel converts plant fiber into rope.

</div>

<div class="tool-tab-content" id="content-faq" style="display:none">

### ❓ Frequently Asked Questions

**Why are my crafting stations showing locked recipes?**
Most games require you to unlock recipes by finding schematics (Sons of the Forest), defeating bosses (V Rising), scanning items (Grounded), or crafting upgrades (Valheim). Check the progression guide for each game.

**What should I craft first in a new game?**
A basic weapon, a repair tool, a bedroll/spawn point, and storage. In Valheim: Workbench + Hammer. In Enshrouded: Workbench + Glider. In V Rising: Copper Weapons + Castle Heart.

**How do I get more inventory space?**
Valheim: Megingjord belt from Haldor the trader. Enshrouded: Upgrade your character skills. V Rising: Book of the Dead boss drop. Sons of the Forest: Craft a backpack. Grounded: Upgrade the Backpack at the Field Station.

**Can I recycle or deconstruct items?**
Valheim: No, but items can be stored indefinitely. Enshrouded: Yes, use the Salvage option at crafting stations. V Rising: Destroy items at the Castle Heart for partial material return. Sons of the Forest: Items can be stored but not recycled. Grounded: Items can be analyzed for unlocks but not deconstructed.

</div>

<script>
(function() {
  // Tab switching logic
  var tabRadios = document.querySelectorAll('.tool-tabs input[name="tooltab"]');
  var tabContents = {
    'tab-calc': document.getElementById('content-calc'),
    'tab-guide': document.getElementById('content-guide'),
    'tab-faq': document.getElementById('content-faq')
  };
  function switchTab(tabId) {
    Object.keys(tabContents).forEach(function(id) {
      tabContents[id].style.display = (id === tabId) ? 'block' : 'none';
    });
  }
  tabRadios.forEach(function(radio) {
    radio.addEventListener('change', function() {
      if (this.checked) switchTab(this.id);
    });
  });
  // Ensure initial state
  switchTab('tab-calc');

  // Recipe data: game -> category -> items
  var recipes = {
    valheim: {
      weapon: {
        "Stone Axe": {"Wood": 5, "Stone": 4},
        "Flint Axe": {"Wood": 4, "Flint": 6},
        "Bronze Axe": {"Wood": 4, "Bronze": 8},
        "Iron Mace": {"Wood": 3, "Iron": 7},
        "Draugr Fang (Bow)": {"Fine Wood": 10, "Silver": 10, "Deer Hide": 2, "Guck": 10},
        "Frostner (Mace)": {"Ancient Bark": 10, "Silver": 30, "Freeze Gland": 5, "Ymir Flesh": 5}
      },
      armor: {
        "Leather Tunic": {"Deer Hide": 6, "Bone Fragments": 2},
        "Bronze Plate Chest": {"Bronze": 20, "Deer Hide": 2},
        "Iron Scale Mail": {"Iron": 20, "Deer Hide": 2, "Chain": 1},
        "Wolf Armor Chest": {"Wolf Pelt": 20, "Silver": 30, "Chain": 1, "Wolf Fang": 2}
      },
      tool: {
        "Hammer": {"Wood": 3, "Stone": 2},
        "Cultivator": {"Bronze": 5, "Core Wood": 5},
        "Pickaxe (Antler)": {"Hard Antler": 1, "Wood": 10},
        "Iron Pickaxe": {"Wood": 3, "Iron": 20}
      }
    },
    enshrouded: {
      weapon: {
        "Scrapper Sword": {"Scrap Metal": 5, "String": 2},
        "Bone Sword": {"Bone": 8, "String": 3},
        "Fungal Sword": {"Fungal Wood": 10, "Resin": 5, "String": 3},
        "Wand of the Ancients": {"Twisted Bone": 8, "Charcoal": 5, "Resin": 5}
      },
      armor: {
        "Rags": {"Plant Fiber": 10, "String": 2},
        "Scavenger Chest": {"Scrap Metal": 8, "Animal Hide": 5, "String": 3},
        "Bone Armor Chest": {"Bone": 15, "Animal Hide": 8, "String": 5}
      },
      tool: {
        "Scrappy Pickaxe": {"Scrap Metal": 5, "Wood": 5},
        "Bone Pickaxe": {"Bone": 8, "Wood": 5, "Animal Hide": 2},
        "Grappling Hook": {"Scrap Metal": 10, "String": 10, "Animal Hide": 3}
      }
    },
    vrising: {
      weapon: {
        "Copper Sword": {"Copper": 12, "Plank": 4},
        "Iron Sword": {"Iron": 12, "Plank": 8},
        "Dark Silver Sword": {"Dark Silver": 12, "Plank": 12, "Gem Dust": 4}
      },
      armor: {
        "Copper Chest": {"Copper": 16, "Animal Hide": 8, "Plank": 4},
        "Iron Chest": {"Iron": 16, "Animal Hide": 12, "Plank": 8},
        "Dark Silver Chest": {"Dark Silver": 16, "Primal Leather": 12, "Gold": 4}
      },
      tool: {
        "Copper Axe": {"Copper": 8, "Plank": 4},
        "Iron Axe": {"Iron": 8, "Plank": 4},
        "Merciless Axe": {"Dark Silver": 8, "Plank": 8, "Gem Dust": 2}
      }
    },
    sons: {
      weapon: {
        "Crafted Spear": {"Stick": 3, "Duct Tape": 2, "Rope": 1},
        "Bow": {"Stick": 3, "Rope": 2, "Duct Tape": 1},
        "Slingshot": {"Stick": 2, "Rope": 1, "Duct Tape": 1},
        "Machete": {"Scrap": 4, "Stick": 2, "Rope": 2, "Duct Tape": 2}
      },
      armor: {
        "Hide Armor": {"Deer Hide": 4, "Rope": 2, "Duct Tape": 1},
        "Tech Armor": {"Circuit Board": 3, "Scrap": 6, "Wire": 4, "Duct Tape": 3}
      },
      tool: {
        "Survival Axe": {"Stick": 3, "Rope": 2, "Scrap": 2, "Duct Tape": 1},
        "Shovel": {"Stick": 3, "Scrap": 3, "Rope": 2, "Duct Tape": 2},
        "Repair Tool": {"Scrap": 2, "Wire": 1, "Circuit Board": 1}
      }
    },
    grounded: {
      weapon: {
        "Pebblet Spear": {"Pebblet": 3, "Sprig": 2, "Gnat Fuzz": 1},
        "Bone Dagger": {"Bone": 3, "Eelgrass Strand": 2, "Gnat Fuzz": 1},
        "Red Ant Club": {"Red Ant Part": 3, "Sprig": 2, "Gnat Fuzz": 1},
        "Mosquito Needle": {"Mosquito Beak": 2, "Mosquito Wing": 1, "Eelgrass Strand": 2}
      },
      armor: {
        "Clover Armor": {"Clover Leaf": 6, "Petal": 3, "Sprig": 3},
        "Acorn Armor": {"Acorn Shell": 6, "Petal": 2, "Eelgrass Strand": 4},
        "Ladybug Armor": {"Ladybug Head": 1, "Ladybug Shell": 3, "Ladybug Leg": 3}
      },
      tool: {
        "Pebblet Axe": {"Pebblet": 2, "Sprig": 2, "Gnat Fuzz": 1},
        "Pebblet Hammer": {"Pebblet": 3, "Sprig": 2, "Gnat Fuzz": 1},
        "Insect Axe": {"Stinkbug Part": 2, "Bombardier Part": 1, "Sprig": 2, "Gnat Fuzz": 1}
      }
    }
  };

  var gameSelect = document.getElementById('cc-game');
  var catSelect = document.getElementById('cc-category');
  var itemSelect = document.getElementById('cc-item');
  var qtyInput = document.getElementById('cc-qty');

  function updateItems() {
    var game = gameSelect.value;
    var cat = catSelect.value;
    itemSelect.innerHTML = '';
    if (!game || !recipes[game] || !recipes[game][cat]) {
      itemSelect.innerHTML = '<option value="">— Select game first —</option>';
      return;
    }
    var items = Object.keys(recipes[game][cat]);
    items.sort();
    items.forEach(function(name) {
      var opt = document.createElement('option');
      opt.value = name;
      opt.textContent = name;
      itemSelect.appendChild(opt);
    });
  }

  gameSelect.addEventListener('change', updateItems);
  catSelect.addEventListener('change', updateItems);

  window.calculateCrafting = function() {
    var game = gameSelect.value;
    var item = itemSelect.value;
    var qty = parseInt(qtyInput.value) || 1;
    var resultDiv = document.getElementById('calc-result');

    if (!game || !item) {
      resultDiv.innerHTML = '<p style="color: rgba(255,255,255,0.4);">Please select a game, category, and item.</p>';
      return;
    }

    var materials = recipes[game][catSelect.value][item];
    var totalHtml = '<div style="font-weight:600; margin-bottom:12px;">🔨 <strong>' + item + '</strong> × ' + qty + '</div>';
    totalHtml += '<div class="calc-result-item"><span>Material</span><span>Total Needed</span></div>';

    var matNames = Object.keys(materials);
    matNames.forEach(function(mat) {
      var total = materials[mat] * qty;
      totalHtml += '<div class="calc-result-item"><span class="calc-result-mat">' + mat + '</span><span class="calc-result-qty">× ' + total + '</span></div>';
    });

    resultDiv.innerHTML = totalHtml;
  };
})();
</script>

---

## Valheim — Forge Craftable Weapons

| Weapon | Materials | Skill Requirement | Base Damage |
|--------|-----------|-------------------|-------------|
| Bronze Sword | 3 Bronze, 2 Wood | 1 | 55 |
| Iron Sword | 2 Iron, 2 Wood, 1 Leather | 1 | 65 |
| Silver Sword | 3 Silver, 2 Wood, 1 Leather, 1 Iron | 1 | 82 |
| Blackmetal Sword | 3 Blackmetal, 2 Fine Wood, 1 Linen | 60 Forge | 100 |
| Porcupine (Mace) | 5 Iron, 5 Needle, 1 Linen, 5 Fine Wood | 1 | 82 |
| Draugr Fang (Bow) | 10 Fine Wood, 10 Silver, 2 Deer Hide, 10 Guck | 1 | 50 (+ poison) |

## Grounded — Tier 2 Tools

| Tool | Materials | Harvest Level | Base Damage |
|------|-----------|---------------|-------------|
| Insect Axe | 2 Stinkbug Part, 1 Bombardier Part, 2 Sprig, 1 Gnat Fuzz | Tier 2 | 25 (chopping) |
| Insect Hammer | 2 Stinkbug Part, 2 Bombardier Part, 3 Sprig | Tier 2 | 30 (busting) |
| Bone Dagger | 3 Bone, 2 Eelgrass Strand, 1 Gnat Fuzz | Tier 2 | 20 (stabbing) |
| Sprig Bow | 5 Sprig, 3 Gnat Fuzz, 2 Woven Fiber | — | 20 (ranged) |
| Red Ant Club | 3 Red Ant Part, 2 Sprig, 1 Gnat Fuzz | — | 25 (smashing) |

## V Rising — Castle Building Materials

| Item | Materials | Unlock Source |
|------|-----------|---------------|
| Castle Heart | 8 Blood Essence, 4 Stone, 4 Plank | Start (from tutorial) |
| Vermin Nest | 4 Animal Hide, 4 Plank | Kill wolves in Farbane Woods |
| Prison Cell | 8 Stone, 4 Iron, 4 Blood Essence | Defeat Tristan the Vampire Hunter |
| Servant Coffin | 12 Plank, 8 Leather, 4 Blood Essence | Defeat Beatrice the Tailor |

---

> 🛒 [**Buy Valheim on Steam**](https://store.steampowered.com/app/892970/) | [**Enshrouded**](https://store.steampowered.com/app/1203620/) | [**V Rising**](https://store.steampowered.com/app/1604030/) | [**Sons of the Forest**](https://store.steampowered.com/app/1326470/) | [**Grounded**](https://store.steampowered.com/app/962130/)
>
> *Affiliate links — we earn a small commission at no extra cost to you.*
