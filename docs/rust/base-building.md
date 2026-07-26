---
title: Rust Base Building Guide — Designs, Honeycombing, TC Placement & Upkeep
description: Complete Rust base building guide. All base designs from 1×2 to clan compounds, honeycombing strategies, TC coverage, upkeep costs, and raid-proofing tips.
---

# 🏠 Rust Base Building Guide

> Data version: Rust 2026 | Last updated: 2026-07

Your base is your home, your loot stash, and your survival in Rust. A well-designed base can repel solos and discourage clans. This guide covers everything from your first 1×2 to compound-scale raid bases.

---

## 🪵 Core Building Concepts

### Building Basics

| Mechanic | Detail |
|:---------|:--------|
| **Building privilege** | Placed by Tool Cupboard (TC) — covers a 50-block radius from center |
| **Upkeep cost** | Base decays without TC having required materials every 24h |
| **Building block limit** | 64 blocks per foundation (spread out) |
| **Stability** | Blocks checked every 10 seconds. Unstable blocks break. |
| **Auth list** | Anyone on TC's auth list can build. TC locks after 3 minutes of placement. |

### Tool Cupboard (TC) Rules

| Rule | Detail |
|:-----|:--------|
| Placement | Must be inside a closed room |
| Coverage | 50-block spherical radius |
| Auth | Authorized players can build; unauthorized cannot |
| Raid target | TC is **priority target** — raiders destroy it to build into your base |
| Trick | Place TC **under the floor** or behind a false wall |

---

## 🏗️ Base Designs (Ranked by Size)

### 1×2 Starter Base

| Aspect | Details |
|:-------|:--------|
| Cost | 1,200 stone, 200 wood |
| Space | 1 airlock + 1 loot room |
| Upkeep | ~100 stone/day |
| Raid cost | 4 satchels, 1 C4 |
| Best for | First night only, solo |

**Layout:**
```
[Wood Door] → [Airlock] → [Sheet Door] → [Main Room with TC]
```

### 2×1 Starter (Better)

| Aspect | Details |
|:-------|:--------|
| Cost | 2,400 stone, 400 wood |
| Space | 1 airlock, 1 loot room, 1 sleeping bag room |
| Upkeep | ~200 stone/day |
| Raid cost | 6 satchels, 1 C4 |
| Best for | Solo first 2 days |

### 2×2 "The Standard"

| Aspect | Details |
|:-------|:--------|
| Cost | 8,000 stone, 1,000 wood |
| Space | 3 rooms + honeycomb |
| Upkeep | ~600 stone/day |
| Raid cost | 8 satchels, 2 C4 (honeycombed) |
| Best for | Solo/duo main base |

**Layout:**
```
[2x2 square base]
  ↙
[Entrance] → [Airlock] → [Kitchen/Crafting] → [TC room (center)]
                ↓
              [Loot room]
```

### 2×2 with HQM Bunker (Solo Raid Base)

| Aspect | Details |
|:-------|:--------|
| Cost | 16,000 stone, 2,000 HQ metal |
| HQM walls | 6 walls surround TC vault |
| Upkeep | ~300 HQM/day |
| Raid cost | 32+ rockets (with HQM layer) |
| Best for | Solo who plays 4+ hrs/day |

### Shooting Floor (Compound Base)

| Aspect | Details |
|:-------|:--------|
| Height | 3+ stories above ground floor |
| Cover | High external walls + compound gate |
| Defenses | SAM sites, auto turrets, shotgun traps |
| Upkeep | ~3,000 stone + 300 HQM/day |

---

## 🧊 Honeycombing: The Secret to a Strong Base

### What is Honeycombing?

Honeycombing is adding an **extra layer of walls** around your base's core. Every wall you add forces raiders to spend more explosives to reach your TC.

### Honeycomb Layouts

| Layer | Raw stone walls | Explosive cost per layer |
|:------|:----------------|:------------------------|
| Core (TC room) | 4 walls | 4 C4 (or 8 rockets) |
| +1 honeycomb layer | +8 walls | +8 C4 |
| +2 honeycomb layers | +12 walls | +12 C4 |
| +3 honeycomb layers | +16 walls | +16 C4 |
| Total (3 layers) | 40 walls | 40 C4  

### Honeycomb Rules

1. **Every wall counts** — raiders must destroy **every layer** to reach the core
2. **Triangle honeycombing** — use triangle foundations between square foundations for extra walls
3. **False walls** — add empty rooms that look like they might contain loot (waste raider resources)
4. **Stability check** — honeycomb must be attached to stable foundations or it'll collapse

---

## 🔨 Upkeep Costs (Stone Base Example)

### Daily Upkeep Table

| Base Type | Stone/day | Wood/day | Metal Frags/day | HQM/day |
|:----------|:----------|:---------|:----------------|:--------|
| 1×2 (no honeycomb) | 180 | 40 | 20 | 0 |
| 2×2 (no honeycomb) | 620 | 140 | 80 | 0 |
| 2×2 (1 honeycomb layer) | 1,120 | 260 | 140 | 0 |
| 2×2 (2 honeycomb layers) | 1,860 | 420 | 240 | 0 |
| 2×2 (HQM core) | 1,120 | 260 | 140 | 125 |
| Compound (2×2 + walls + turrets) | 4,500 | 1,200 | 600 | 400 |

### Upkeep Tips

| Tip | Why |
|:----|:----|
| Keep a **tool cupboard chest** filled with 3 days of upkeep | Prevents decay during offline |
| Upgrade core to **stone** first, then metal, then HQM | Stone is cheap, HQM takes time |
| **Metal doors** are priority | Wooden doors break with 2 satchel charges |
| Upgrade **foundations** first | If foundation breaks, everything above collapses |
| Armored doors > garage doors | 2 C4 vs 1 C4 (garage doors are cheaper to raid) |

---

## 🚪 Doors & Entry Points

### Door Comparison

| Door Type | Health | Explosive Cost | Crafting |
|:----------|:-------|:---------------|:---------|
| Wooden | 200 | 2 satchels (1,200 sulfur) | 1,000 wood |
| Sheet metal | 400 | 4 satchels (2,400 sulfur) | 3 frags |
| Garage door | 600 | 1 C4 (2,200 sulfur) | 5 gears + frags |
| Armored double door | 800 | 2 C4 (4,400 sulfur) | 25 HQM |

> 💡 **Pro Tip:** Use **garage doors** for your main entrance (faster to open/close, smaller profile) and **armored doors** for TC room access.

### Airlock Design

An **airlock** is essential for not dying when you open your base door.

```
[Outside] → [Wood Door] → [Tiny room] → [Sheet Door] → [Inside]
```

**Rules:**
- Never open both doors at once
- 2 airlocks minimum for main entrance
- Add shotgun traps in airlock (facing inward)

---

## 🛡️ Base Defense Tips

### Turret Placement

| Location | Turrets | Ammo per Day |
|:---------|:--------|:-------------|
| Roof | 2 | 500 |
| Entrance | 1–2 (facing outward) | 300 |
| Compound perimeter | 2–4 on towers | 1,000 |
| Interior (TC room) | 1 hidden | 200 |

### Trap Placement

| Trap | Effect | Ammo per Week |
|:-----|:-------|:--------------|
| Shotgun trap | 2–3 pellets per shot (kills naked raiders) | 200 shells |
| Flame turret | 5–10 fire damage per tick | 500 low-grade fuel |
| Tesla coil | Electric shock (needs power source) | None |
| Landmines | 20 damage per mine | None (reusable if found) |

### Compound Defenses

| Defense | Cost | Effect |
|:--------|:-----|:--------|
| High external stone wall | 300 stone | Block line of sight |
| High external gate | 20 HQM | Vehicle entry point |
| Watch tower | 2,000 stone | Roof camping spot |
| Bunkers | Hidden rooms | Surprise escape routes |
| External TC | 1 TC + walls | Prevents raiders from building over walls |

---

## 🚨 Raid-Proofing Your Base

### Do's and Don'ts

| ✅ Do | ❌ Don't |
|:------|:---------|
| Honeycomb every layer | Leave foundation exposed |
| Place TC in center | Put TC on ground floor (easy breach) |
| Use garage doors for entrance | Use wooden doors after day 1 |
| Add false walls + empty rooms | Make base look small/underbuilt |
| Build on uneven terrain | Build on flat open ground |
| Add external TC + compound walls | Rely on just honeycomb |
| Bury loot in separate 1×1 stashes | Keep all eggs in one basket |

### Splash Damage Protection

| Technique | How It Works |
|:----------|:-------------|
| **Staggered walls** | Walls offset by 1 block — rocket splash hits air instead of next wall |
| **Triangle walls** | Triangle foundation walls absorb more splash than square |
| **Bunkers** | Separate sealed rooms with independent SPLASH damage path |
| **External stashes** | Hidden stashes in bushes / under rocks with key lock |
| **Spread loot rooms** | Don't put all loot in one room — spread across 3+ rooms |

---

## ⚡ Quick Build Steps (New Player)

1. **Place foundation** (2×1 or 2×2, on flat terrain)
2. **Place walls** (stone if possible)
3. **Add doorways** for entrance + airlock
4. **Place TC** in center room, authorize yourself
5. **Add ceiling** (stone ceiling tiles)
6. **Build second floor** (sleeping bags, furnaces)
7. **Honeycomb** outer walls with triangle foundations
8. **Upgrade** core to metal, doors to sheet metal
9. **Place traps** (shotgun trap above airlock)
10. **Add compound** (external walls + gate when secure)
