---
title: "DSP Logistics Guide — Interplanetary Transport"
description: "Master Dyson Sphere Program logistics — conveyor belts, PLS, ILS, logistics vessel management, and hub design."
---

# 🚚 DSP Logistics Guide — Interplanetary Transport

Efficient logistics is the difference between a thriving interstellar empire and a spaghetti nightmare. Dyson Sphere Program gives you three escalating tiers of material transport — from simple belts to planet-spanning drone networks to interstellar vessel fleets. Master all three, and your factory will scale from a handful of miners to a galaxy-spanning megabase without ever running dry.

This guide covers every logistics tool in detail: exactly what each unlocks, how many items per second it moves, what it costs to build, and how to design a hub that keeps everything flowing.

---

## 📦 The Three Logistics Systems

DSP's logistics stack is deliberately layered. You use belts (free, infinite throughput per tile) while you unlock the techs that let you replace belts with bots, and then replace planetary bots with interstellar vessels.

### 1. Conveyor Belts (Planet-Level)

Belts are your workhorse from the first minute to the endgame. Each tier doubles or quintuples throughput and introduces new crafting complexity.

| Tier  | Speed   | Material                                    | Best Used For                |
| :---- | :------ | :------------------------------------------ | :--------------------------- |
| MK.I  | 6/s     | 2× Iron Ingot                               | Early-game spaghetti         |
| MK.II | 12/s    | 1× Steel + 2× Titanium Ingot + 1× Gear      | Mid-game main bus            |
| MK.III | 30/s   | 1× Particle Broadband + 1× Titanium Glass   | Late-game megabase arteries  |

**MK.I Belt (6 items/s):** Crafted from 2 iron ingots per 3 belts. You'll lay thousands of these before you hit yellow science. Use them for ore feeds from miners, early smelting columns, and temporary builds you know you'll tear down.

**MK.II Belt (12 items/s):** Available alongside titanium smelting. The jump from 6→12 items/s is enough for mid-game production lines making blue/red/yellow matrices. The steel and titanium gear requirements mean you need a dedicated steel foundry and a gear assembler running constantly — these belts consume materials fast.

**MK.III Belt (30 items/s):** The endgame belt. 30 items/s can feed an entire row of fully-upgraded smelters from a single belt segment. Particle Broadband requires a full green-science production chain (fractal silicon + carbon nanotubes + plastic), so MK.III belts don't appear until you have a mature factory. One fully saturated MK.III belt can deliver enough copper ingots to feed 60+ circuit assemblers — plan your bus accordingly.

**Sorter throughput note:** Sorters have their own tiers (MK.I–III, plus Pile Sorter). A MK.III sorter using a MK.III belt moves 30 items/s only when stack count upgrades are maxed. Check your sorter tech level before assuming full throughput.

---

### 2. Planetary Logistics Station (PLS)

| Property          | Value                             |
| :---------------- | :-------------------------------- |
| **Unlock**        | Yellow Science (Planetary Logistics) |
| **Range**         | Single planet only                |
| **Unit**          | Logistics Drone (stack carrier)    |
| **Drone capacity** | 1 stack (default 100–200 items)   |
| **Slots**         | 3 storage, 3 drone               |
| **Power drain**   | 2.4 MW active, 30 kW idle         |

The PLS is the mid-game revolution. Once unlocked, you can build a single PLS at each mining patch set to **Supply**, a PLS in your factory set to **Demand**, and drones will auto-balance the two — no belts needed.

**How drone mechanics work:**
- Each drone carries exactly one stack of the requested item.
- Drones charge at the station (4.8 MW charging power per station slot).
- Drone speed starts at 60 m/s; orbital speed upgrades (in the Logistics tech tree) raise this to 90 m/s, then 120 m/s.
- Drones automatically split between multiple stations — if two demand stations request iron ore, drones distribute proportionally.
- Drone count per station can be upgraded to 10 once you research Drone Engine upgrades.

**Common PLS configurations:**

| Station Type    | Slots Used                  | Notes                             |
| :-------------- | :-------------------------- | :-------------------------------- |
| Mining outpost  | 1 supply slot for ore       | Belt from miners → PLS storage    |
| Smelter input   | 1 demand slot for ore       | Output ingots to 2nd supply slot  |
| Component mall  | 3 demand (ore/ingot/plastic) | Mini-bus replacement in one tile  |
| Buffer depot    | Supply + Demand same item    | Keeps N stacks in reserve         |

**When to use PLS vs belts:** Run the numbers. A single MK.II belt (12/s) costs only steel and titanium and provides infinite throughput with zero power. A PLS with 10 drones moving 1 stack each of iron ore (100/stack) at 60 m/s over a 500 m round trip moves roughly 1,000 items per minute (≈17/s) — better than a belt, but at significant power cost. Use PLS when you value **compactness** and **flexibility** over raw belt throughput. Use belts for high-volume, short-distance flows (smelter input lines, mall feeds).

---

### 3. Interstellar Logistics Station (ILS)

| Property          | Value                              |
| :---------------- | :--------------------------------- |
| **Unlock**        | Purple Science (Interstellar Logistics) |
| **Range**         | Any star system (with warpers)     |
| **Unit**          | Logistics Vessel (200+ items)      |
| **Vessel capacity** | 200 items (upgradable to 400)    |
| **Slots**         | 5 storage, 3 vessel, 3 drone      |
| **Power drain**   | 12 MW active, 90 kW idle          |
| **Warper slot**   | Dedicated slot (stack of 50)      |

The ILS is how you unify your entire interstellar empire. One ILS on a planet in one system can request iron ore from a mining outpost in another system entirely — as long as both have warpers.

**Warpers and fuel:**
- Warpers are crafted from Graviton Lenses (or the alternate recipe using Green Science + Graviton Lenses for 8 warpers per craft).
- Each interstellar trip consumes **one warper** per vessel per trip (not per item).
- Vessels will only warp if the destination is beyond their **max warp distance** (default 6 light-years, upgradable to 12 and 24 with Drive Engine tech).
- Within the same star system, vessels fly at sub-warp speed (≈1000 m/s default) — no warper consumed.
- Always dedicate one ILS slot to warpers via local demand + remote supply, or ship them by belt.

**Vessel mechanics:**
- Each vessel carries 200 items base, 400 with Vessel Cargo Capacity upgrade.
- Vessel speed starts at 1000 m/s, upgradeable to 2000 m/s and 3000 m/s via Drive Engine upgrades.
- ILS charging power is 12 MW per slot — a fully-loaded ILS charging 3 vessels can draw 36 MW. Plan your power grid accordingly.
- Vessels auto-launch when demand exceeds supply thresholds (configurable in the station UI).
- You can manually set **Min Vessel Load** (default 100%) — at 25%, a vessel will depart with as few as 50 items (for long-distance high-demand items). Lowering this increases trips and warper consumption.

**Best ILS patterns:**

| Pattern                       | Config                                   | Example                               |
| :---------------------------- | :--------------------------------------- | :------------------------------------ |
| **Rare ore import**           | Remote Demand (local planet ore station) | Organic Crystal, Kimberlite, Fractal Silicon |
| **Smelter hub feed**          | Local Demand (ore) + Local Supply (ingot) | Iron ore in, iron ingot out          |
| **Matrix factory supply**     | Local Demand (ingots, circuits, etc.)    | Feed all component inputs in one ILS |
| **Research hub output**       | Local Demand (empty) + Remote Supply     | Collect white matrices from outposts  |
| **Warper distribution**       | Remote Demand + Local Supply loop        | Each ILS requests warpers from a central warper factory |

**Orbital Collector logistics:** When you build Orbital Collectors around gas giants, their harvested hydrogen, deuterium, and fire ice can be transported by ILS vessels. Either ship directly to your factory ILS or use a dedicated gas-processing station on a nearby planet.

---

## 🌟 Hub Design Pattern

A well-designed logistics hub keeps your factory organized through purple science and beyond. The idea is simple: centralize smelting, distribute ingots, and collect finished matrices.

```
     [ILS: Rare Ore Imports] ← Warpers in, ore out
              ↓
   [Smelter Array: All ores → Ingots]
              ↓
     [ILS: Ingot Buffer] ← Distributes across factory blocks
              ↓
   [Factory Block 1]   [Factory Block 2]   [Factory Block 3]
   (Blue & Red Matrix)  (Yellow & Purple)   (Green & White)
              ↓
     [ILS: Matrix Output] ← Ships to research hub
```

**Detailed block breakdown:**

1. **Rare Ore Imports (ILS):** Set to Remote Demand for every rare ore in the game. Run the output belts into a unified smelter column. The ILS requests warpers via local demand from a central warper hub station.

2. **Smelter Array:** Dedicate 4–6 rows of smelters (Arc Smelters late-game). Ingest ores from the import ILS, output ingots to a row of output belts feeding the Ingot Buffer ILS. Use two levels: top belt = input ore, bottom belt = output ingot, or use a splitter bus.

3. **Ingot Buffer ILS:** Set this station to Local Demand (ingots) + Local Supply (ingots). It buffers a full load of every common ingot (iron, copper, steel, titanium, silicon, stone brick). Each factory block then has its own ILS that requests the ingots it needs.

4. **Factory Blocks:** Each block is self-contained. One ILS at the block entrance requests ingots/components and supplies finished products. For example, the Blue + Red block requests iron ingots and copper ingots and supplies magnetic coils, circuit boards, and blue/red matrices.

5. **Matrix Output ILS:** The final block in the chain. One ILS set to Local Demand (matrices) + Remote Supply (matrices). It collects from all factory blocks and feeds into the research lab cluster or the white matrix array.

---

## 🧠 Advanced Logistics Tips

**Slot management:** Both PLS and ILS let you configure each slot as Storage, Supply, Demand, or a combination. A slot set to **Supply + Demand** acts as a buffer — it will take from drones/belts and provide to drones/belts. Use this for intermediate buffers in your hub.

**Orbital vs. planetary prioritization:** When an ILS has both a local demand slot (PLS drones) and a remote demand slot (vessels), local drones are checked first. If local supply meets demand, vessels won't launch. This is great for in-system logistics: ship from a nearby planet before sending a warper-consuming inter-system trip.

**The spaghetti vs. bots tradeoff:** Belts are free throughput. PLS/ILS cost power and have slot limits. A single MK.III belt (30/s) carries 1,800 items per minute — it takes 20 fully-upgraded drones or 9 vessels to match that. Don't replace belts with stations for high-volume lines. Do replace belts with stations for low-volume, long-distance, or multi-ingredient lines (e.g., a mall that needs 10 different components).

**Upgrade priority for logistics:**
| Tech                        | Effect                             | Priority |
| :-------------------------- | :--------------------------------- | :------- |
| Logistics Drone Engine      | Drone speed 60 → 90 → 120 m/s      | High     |
| Logistics Drone Cargo       | Drone stack 1 → 2 → 3              | High     |
| Logistics Carrier Engine    | Vessel speed 1k → 2k → 3k m/s      | Medium   |
| Logistics Carrier Cargo     | Vessel capacity 200 → 300 → 400    | Medium   |
| Logistics Vessel Drive (warp) | Warp range 6 → 12 → 24 LY        | Low (upgrade when expanding) |

**Common mistakes to avoid:**

- **No warper distribution:** Your ILS will sit idle with "No warper" status. Always configure an ILS to supply warpers (local supply) and have every remote-demand ILS request them locally.
- **Ore colocation:** Don't place ILS right on top of ore patches. You lose the miner footprint. Belt the ore 3–4 tiles over to a PLS/ILS.
- **Over-requesting:** An ILS requests up to its slot capacity. If you set demand to 10,000 iron ore but only need 1,000, the station will hoard ore and other demand stations starve. Set reasonable limits.
- **Forgetting charging power:** A cluster of 4 ILS each charging 3 vessels can draw 144 MW. If your power grid isn't ready, vessel trips stall mid-charge.

---

## 🛒 Start Your Factory

Logistics is the backbone of every successful Dyson Sphere Program playthrough. Whether you're layering belts for your first mall or warping deuterium across 20 light-years, the principles are the same: move items efficiently, buffer where it matters, and always leave room to expand.

Ready to build your interstellar empire?

> 🛒 [**Buy Dyson Sphere Program on Steam**](https://store.steampowered.com/app/1366540/)
