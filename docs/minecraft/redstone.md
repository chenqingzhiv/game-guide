---
title: Minecraft Redstone Guide — Basics, Circuits, Farms & Contraptions
description: Master Minecraft redstone from the ground up. Signal strength, logic gates, pistons, observers, clocks, automatic farms, item sorters, and mega-contraptions.
---

# 🔴 Minecraft Redstone Guide

> Data version: Minecraft 1.21 | Last updated: 2026-07

Redstone is Minecraft's version of electricity. It powers doors, traps, farms, sorting systems, and contraptions that do the work for you. This guide takes you from your first redstone torch to complex automatic farms.

---

## 🔌 Redstone Basics

### Core Components

| Component | Function | Max Range |
|:----------|:---------|:----------|
| **Redstone Dust** | Carries signal along ground | 15 blocks (signal fades) |
| **Redstone Torch** | Constant power source (inverted input) | Ulimited (with repeater) |
| **Redstone Block** | Constant power (no decay), not movable | Adjacent blocks only |
| **Lever** | Toggle on/off | Adjacent only |
| **Button** | Pulse on click (0.5–1 second) | Adjacent only |
| **Pressure Plate** | Pulse when entity stands on it | Adjacent only |

### Signal Propagation

| Rule | Detail |
|:-----|:--------|
| Signal strength | 0 = off, 1–15 = on |
| Fade | Every block of redstone dust drops strength by 1 |
| Repeater | Restores to full strength (15) + adds delay |
| Comparator | Reads signal strength from containers + comparators |
| Through blocks | Glass, slabs, stairs block redstone. Full blocks pass through. |

### Redstone Repeater

| Setting | Delay (redstone ticks) | Real Delay |
|:--------|:----------------------|:-----------|
| 1 tick | 1 | 0.1 seconds |
| 2 ticks | 2 | 0.2 seconds |
| 3 ticks | 3 | 0.3 seconds |
| 4 ticks | 4 | 0.4 seconds |

> 💡 **Pro Tip:** Right-click a repeater to change its delay. Use 2-tick delay for most piston doors to let blocks settle.

---

## ⚡ Essential Circuits

### 1. Pulse Extender (Hold Signal)

Makes a short button press last longer. Useful for lights, doors that need to stay open.

```
Button → Repeater (delay 3) → Comparator (subtract mode) → Loop
```

**Output:** Pulse held for 1–15 seconds depending on repeater delay.

### 2. T-Flip Flop (Toggle Switch)

Turns a button press into a toggle (push on, push off).

```
Design: 2 observers facing each other → 1 redstone block in loop
Simpler: Lever (but buttons are cleaner for builds)
```

**Classic piston-based T-flip-flop:**

```
Button → Piston pushes block → Pulses line → Block covers torch → Toggle
```

### 3. Piston Door (2×2)

The iconic secret door. Here's the compact 2×2 design:

```
Top view:
[P][P]
[P][P]

P = sticky piston facing inward

Trigger: Button → pulse extends all 4 pistons → block wall slides
```

**Wiring rules:**
- All 4 pistons must extend simultaneously
- Use repeaters to sync signal delay
- Signal must go behind the wall — hide redstone under slabs

### 4. Item Elevator (Vertical Transport)

| Height | Design |
|:-------|:-------|
| 1–5 blocks | Water stream + signs |
| 5–15 blocks | Dropper chain (22 droppers facing up) |
| 15+ blocks | Bubble column (soul sand + water source) |

**Bubble column elevator:** Place soul sand at bottom of water column → rising bubbles pull items up.

---

## 🔄 Redstone Clocks (Pulse Generators)

### Hopper Clock (Most Reliable)

```
Hopper A → Hopper B (facing each other)
Hopper A has 1 comparator reading → pulse loop
Items: 1 stack of anything
```

**Cycle time:** 1 stack of items = ~11 seconds per full cycle.

### Observer Clock (Simplest)

```
Observer → comparator → observer (1-tick loop)
Output: Very fast pulses (~0.05 seconds)
```

| Clock Type | Period | Best Use |
|:-----------|:-------|:---------|
| Hopper clock | Variable (11s+ per stack) | Farms, auto-harvest timers |
| Observer clock | 0.1s (2 gt) | Fast pistons, zero-tick machines |
| Etho hopper clock | 8s per item | Long delay timers |
| Repeater clock | 0.1–0.8s | Slow pulse generators |

---

## 🚜 Automatic Farm Designs (Redstone)

### Auto-Crop Harvester

| Component | Purpose |
|:----------|:---------|
| Observer | Detects crop growth |
| Piston + water | Releases water to break crops |
| Timer | Re-tills farmland + replaces water |
| Hopper line | Collects all drops |

**How it works:**

1. Observer watches crop row
2. Any crop fully grown → observer triggers piston
3. Piston retracts water block → water flows over crops
4. Crops break → hoppers collect
5. Timer turns off water after 10 seconds
6. Player (or dispenser) replants

### Auto-Fishing Farm

| Component | Count | Purpose |
|:----------|:------|:--------|
| Note block | 1 | Makes sound to trigger bobber detection |
| Observer | 1 | Detects bobber state change |
| Tripwire hook | 1 | Right-click cast (fishing rod in dispenser) |
| Dispenser | 1 | Holds and casts fishing rod |

**Yield:** ~12 stacks of fish + enchanted books + junk per 8 hours (AFK).

### Super Smelter

| Size | Furnaces | Items per Hr | Fuel Need |
|:-----|:---------|:-------------|:----------|
| Small | 8 | 1,440 | 1 stack coal/hr |
| Medium | 32 | 5,760 | 4 stacks coal/hr |
| Large | 64 | 11,520 | 8 stacks coal/hr |

**Design rules:**
- Hopper chain feeds items into furnaces
- Another hopper chain extracts smelted items
- Comparator reads furnace → signal when done
- Use bamboo or lava buckets as fuel (lava = 100 items per bucket)

---

## 🗄️ Item Sorting System

### Single Item Sorter

```
Layout (from top):
1. Water stream → items flow over hoppers
2. Hopper 1: Filter items (1 comparator + 1 repeater)
3. Hopper 2: Lock hopper 1 unless full
4. Chest: Below hopper 1
```

**Filter setup (per chest):**

| Hopper Slot | Items | Qty |
|:------------|:------|:----|
| 1–4 | Filter item (same item you're sorting) | 1 each (4 total) |
| 5 | Any junk item (don't change) | 1 |
| Comparator output | Signal = items flowing → full signal | Unlocks hopper |

### Stackable Sorting System

Build 54 sorters (one per chest type) in a row. Use 1 water stream running above all hoppers.

**Sort order (recommended):** Most common items first (cobblestone → dirt → wood → stone → ores → food → rare drops)

---

## 🤖 Advanced Contraptions

### Trident Killer

| Component | Count | Purpose |
|:----------|:------|:--------|
| Tridents | 4+ | Floating, spinning, dealing damage |
| Water stream | 1 | Pushes tridents in circle |
| Entity cramming | — | Mobs take damage from trident collision |

**Use case:** AFK XP farm. Stand in the kill chamber with a Looting III sword; tridents do 1 HP damage per tick → you get the kill XP.

### Flying Machine

```
Piston → Observer → Slime block → Piston → Observer (repeat every 2 blocks)
Power piston with redstone block → machine flies in one direction
```

| Design | Speed | Use |
|:-------|:------|:----|
| Simple | 1 block/cycle | Item transport |
| Quad piston | 2 blocks/cycle | Player transport |
| Wide | 3-wide | Perimeter wall builder |

### Bomb (Cannon)

| Type | Projectile | Range | Design |
|:-----|:-----------|:------|:--------|
| TNT cannon | TNT | 15–100 blocks | Water-filled chamber + redstone delay |
| End Crystal | Explosion | Short | Crystal placed on obsidian in range |
| Wither | Skull (not controllable) | 30 blocks | Unreliable, don't use |

---

## 🧪 Redstone Components Quick Reference

| Block | When Powered | Notes |
|:------|:-------------|:------|
| Piston | Extends forward | Max push = 12 blocks |
| Sticky Piston | Extends + retracts | Retracts attached block |
| Dispenser | Shoots item/potion/arrow | Faces outward |
| Dropper | Ejects item (no velocity) | Can feed into chests |
| Observer | One-tick pulse on block update | Best detector in game |
| Comparator | Reads container fullness | Subtract mode = difference |
| Repeater | Delays + resets signal | Can also lock other repeaters |
| Redstone Lamp | Lights up | Glowstone-equivalent light |
| Bell | Rings + sends vibration | Detects mobs near village |
| Target Block | Pulse on hit (strength = distance) | Archery target practice |

---

## 🔧 Redstone Troubleshooting

| Problem | Likely Cause | Fix |
|:--------|:-------------|:----|
| Signal stops at 5 blocks | Repeater needed | Place repeater every 15 blocks |
| Piston won't extend | Signal too weak | Check redstone connection |
| Pistons fire in wrong order | Timing mismatch | Add repeaters for sync |
| Items get stuck in hopper | Wrong filter item | 1 filter item in 4 slots, all same type |
| Comparator output too low | Wrong mode | Right-click to toggle subtract mode |
| Observer keeps pulsing | Block update loop | Break the observer-block cycle |
| Farm harvests constantly | Clock too fast | Use longer delay on hopper clock |

---

## 📐 Project Ideas by Difficulty

| Difficulty | Project | Time |
|:-----------|:--------|:-----|
| ★☆☆☆☆ | Automatic door (wooden) | 5 min |
| ★★☆☆☆ | 2×2 piston door | 15 min |
| ★★☆☆☆ | Item sorter (1 chest) | 20 min |
| ★★★☆☆ | Auto chicken cooker | 30 min |
| ★★★☆☆ | Sugar cane farm | 20 min |
| ★★★★☆ | Iron farm | 1–2 hrs |
| ★★★★☆ | Super smelter (32 furnaces) | 1 hr |
| ★★★★★ | Item sorting system (full) | 3–4 hrs |
| ★★★★★ | Flying machine | 30 min |
| 🌟 | Redstone computer (calculator) | Days |
