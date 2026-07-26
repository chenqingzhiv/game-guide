---
title: Rust Raid Guide — Tools, Explosives, Splash Damage, Raid Bases & Counters
description: Complete Rust raiding guide. Raid tool comparisons, explosive costs per wall type, splash damage mechanics, raid base builds, counters, and defense strategies.
---

# 💥 Rust Raid Guide

> Data version: Rust 2026 | Last updated: 2026-07

Raiding is how you progress in Rust. Destroy walls, break into bases, steal everything. This guide covers raid tools, explosive economics, splash mechanics, raid base strategies, and how to defend against raiders.

---

## 🧨 Raid Tools Comparison

### Full Explosive Table

| Tool | Sulfur Cost | Damage per Wall Type | Range | Craft Time |
|:-----|:------------|:---------------------|:------|:-----------|
| Satchel Charge | 480 sulfur | Wood: 1, Stone: 3, Metal: 5, HQM: 8 | 3m | 30s |
| C4 | 2,200 sulfur | Wood: 1, Stone: 1, Metal: 2, HQM: 4 | 5m | 60s |
| Rocket | 1,400 sulfur | Wood: 1, Stone: 1, Metal: 2, HQM: 4 | 15m | 10s |
| HE Grenade | 200 sulfur | Wood: 2, Stone: 4, Metal: 8, HQM: 16+ | 8m | 20s |
| Explosive 5.56 | 10 sulfur/round | Wood: 10, Stone: 30, Metal: 50, HQM: 100+ | 50m | 1s |

### Cost per Wall Type

| Wall Type | HP | Satchels | C4 | Rockets | HE Grenades | Explosive 5.56 |
|:----------|:---|:---------|:---|:--------|:------------|:---------------|
| Wood | 250 | 2 (960 sulfur) | 1 (2,200 S) | 1 (1,400 S) | 3 (600 S) | 25 (250 S) |
| Stone | 500 | 4 (1,920 S) | 2 (4,400 S) | 2 (2,800 S) | 5 (1,000 S) | 50 (500 S) |
| Metal | 1,000 | 6 (2,880 S) | 4 (8,800 S) | 3 (4,200 S) | 10 (2,000 S) | 100 (1,000 S) |
| HQM | 2,000 | 10 (4,800 S) | 8 (17,600 S) | 6 (8,400 S) | 20 (4,000 S) | 200 (2,000 S) |

> 💡 **Cheapest per wall:** Satchel Charge (lowest sulfur per 500 HP). But they're unreliable (10s fuse timer with random detonation).
> **Fastest:** Rockets (high velocity, long range).

### Door Breaking Costs

| Door Type | HP | Satchels | C4 | Rockets | Notes |
|:----------|:---|:---------|:---|:--------|:------|
| Wooden door | 200 | 1 (480 sulfur) | 1 | 1 | Break with 3 hatchet hits too |
| Sheet metal door | 400 | 2 (960) | 1 | 1 | Standard door |
| Garage door | 600 | 3 (1,440) | 2 (4,400 S) | 1 (1,400 S) | **Most efficient per HP** |
| Armored double door | 800 | 4 (1,920) | 2 (4,400 S) | 2 (2,800 S) | Expensive door |

---

## 💥 Splash Damage Mechanics

### How Splash Works

| Explosive | Splash Radius | Damage Falloff | Notes |
|:----------|:--------------|:---------------|:-------|
| Rocket | 3m (explosion) + 5m (shrapnel) | 25% per meter | **Best for splash** |
| C4 | 4m | 50% per meter | Moderate splash |
| HE Grenade | 5m | 40% per meter | Area denial + trap kill |
| Satchel | 4m | 50% per meter | Random spread |

### Rocket Splash Direction

Rockets travel and detonate on impact. The **splash cone** is directional — it does more damage on the side of the wall that the rocket hits.

```
Rocket → Wall → Explosion (3m sphere)
         Back wall takes ~50% splash damage
         Adjacent walls take ~50% splash damage
         Floor/ceiling take ~20% splash damage
```

### Raiding Through Splash

| Technique | How | Damage Efficiency |
|:----------|:-----|:-----------------|
| **Rocket splash through walls** | Fire rocket at wall → adjacent wall takes 50% splash | 2 walls per rocket if placed correctly |
| **Staircase splash** | Destroy stairs with floor splash → fall damage kills loot room access | 1 rocket per floor |
| **Ceiling splash** | Rocket at wall → splash damages floor above | 1 rocket damages 2 surfaces |
| **Door splash** | Door destroyed → splash hits room behind | 1 C4 for door + loot room damage |

### Splash Protection (for builders)

| Defense | How It Works |
|:--------|:-------------|
| **Staggered walls** | Offset walls by 1 block — splash hits air between them |
| **Honeycomb with air gap** | 1 block gap between honeycomb and core absorbs splash |
| **Triangle walls** | Triangle walls provide 0.75 block surface — less splash transfer |
| **Metal barricade** | Placed inside walls absorbs some splash damage |
| **Multi-TC bunker** | Separate bunkers per loot room — splash can't reach all |

---

## 🚧 Raid Base Setup

### What You Need

| Item | Qty (Medium Raid) | Qty (Large Raid) |
|:-----|:------------------|:-----------------|
| TC + tool cupboard | 1 | 2+ |
| Wooden boxes | 6 | 20+ |
| Sleeping bags | 3 | 6+ |
| Furnace | 1 | 2 |
| Refinery | 1 | 2 |
| Doors (sheet metal) | 4 | 10+ |
| Lock (code lock) | 4 | 10+ |
| Explosives + ammo | Full inventory | Full inventory + boxes |

### Raid Base Design

```
    [Raid TC] — 2 walls + garage door
        ↓
    [Airlock 1] — Wood door → Sheet door
        ↓
    [Furnace room] — Smelting HQ, storing explosives
        ↓
    [Ammo room] — Boxes of rockets/C4
        ↓
    [Fighting position] — Window frames facing enemy base
```

**Placement:** Build raid base **within 50 blocks** of target base (TC range). Ensure no splash from your raid can hit your own raid base.

### Raid Base Rules

1. **Metal doors only** — wooden doors break with 1 satchel
2. **Every room has a bag** — respawn close to action
3. **Furnace running** — smelt ore to HQM during raid downtime
4. **Garage door on outer wall** — quick escape if counter-raid comes
5. **2-floor design** — shooting floor on top, storage below

---

## ⚔️ Raid Strategies by Base Type

### Small Base (1×2 / 2×1)

| Approach | Cost | Risk |
|:---------|:-----|:-----|
| **Roof entry** | 2 C4 (ceiling) | Medium — they might have roof traps |
| **Door path** | 1 C4 per door | Low — cheapest, but doors may be armored |
| **Wall punch** | 2 C4 per wall | Medium — predictable |

**Best method:** Find the TC room (usually center). Blast through ceiling from roof. TC destroyed → they can't build. Loot everything.

### Medium Base (2×2 honeycomb)

| Approach | Cost | Risk |
|:---------|:-----|:-----|
| **Staircase up** | 4 C4 | High — usually camped |
| **Foundation entry** | 6 C4 (foundation + wall) | Medium — trolling their floor |
| **Splash through honeycomb** | 6 rockets (staggered) | Medium — efficient |
| **Loot room first** | 8 C4 | High risk — but you hit the jackpot |

**Best method:** Go **through multiple walls** in a zigzag — not straight to TC. They'll camp the TC path.

### Compound / Clan Base

| Approach | Cost | Strategy |
|:---------|:-----|:---------|
| **External wall breach** | ~10 C4 for walls | Slow but safe |
| **Compound gate** | 2 C4 for gate + turrets | Fast but suicidal |
| **Sneak in** | Social engineering | Low cost, high risk |
| **Raid tower** | 5 rocket salvo from 100m | Expensive but safe |

**Clan base strategy:** If it's a 10+ man compound, **don't solo raid it**. Get 3+ friends.

---

## 🛡️ Defending Against Raiders

### Counter-Raid Tools

| Tool | Effect | Cost |
|:-----|:-------|:------|
| Auto turrets | 20 damage/bullet, 500 ammo capacity | 40 HQM + tech trash |
| Shotgun traps | 2–3 pellets × 200 shells | 250 metal frags |
| Flame turret | 5 fire damage/tick × 500 fuel | 50 metal frags + tech trash |
| SAM site | Shoot down mini-copters | 35 HQM + tech trash |
| Tesla coil | 10 damage per zap (needs battery) | Rare component |

### Defensive Strategies

| Tactic | How | When |
|:-------|:-----|:------|
| **Peek shoot** | Window frame from top floor | They're focused on breaking walls |
| **Flank from outside** | Exit through secret tunnel | They're at your front wall |
| **Counter-raid base** | Build your own raid base behind theirs | They committed to one angle |
| **Call allies** | Discord group or ally clan | They outnumber you |
| **Despawn loot** | Throw loot in fire | They're about to break in — deny them |

### Raid Alarms

| Alarm Type | Signal | Detection |
|:-----------|:-------|:----------|
| **HBHF sensor** | Looks for living entities | Moving players 30m |
| **Pressure pad** + speaker | Footsteps trigger alarm | 3×3 area |
| **Door sensor** | Door opened alarm | On any door |
| **Turret + alarm combo** | Turret fires → alarm sounds | Turret range |

---

## 📊 Cost-Benefit Analysis

### Is This Raid Worth It?

| Target Base | Likely Loot Value | Cost to Raid | Verdict |
|:------------|:-----------------|:-------------|:--------|
| 1×2 wood starter | ~1,000 scrap | 2 satchels (960 sulfur) | **Not worth** |
| 2×2 stone (honeycomb) | ~10,000 scrap | 4 C4 (8,800 sulfur) | **Maybe** |
| 2×2 HQM core | ~50,000 scrap | 6 C4 (13,200 sulfur) | **Probably** |
| Compound (6+ players) | 100k+ scrap | 20+ C4 | **Only with allies** |
| Oil Rig loot base | 200k+ scrap | 15+ C4 | **If you know it's stacked** |

### When NOT to Raid

| Situation | Why |
|:----------|:-----|
| Server wipe is tomorrow | Loot will be gone in hours |
| No furnace/refinery near target | Can't smelt ore during raid |
| You're outnumbered | Counter-raid = you lose everything |
| Target is online (10+ players) | They'll fight back — costly |
| You have < 50% of estimated cost | Running out of explosives mid-raid = disaster |

---

## 🧰 Raid Preparation Checklist

- [ ] Target base scouted (wall type, door type, likely TC room)
- [ ] Explosives crafted (rockets + C4 + ammo)
- [ ] Med syringes (12+)
- [ ] Bandages (2 stacks)
- [ ] Armor (full metal/HQM)
- [ ] Weapon (AK/M249 + bolt action)
- [ ] Ammo for weapons (3+ stacks)
- [ ] Raid base built within TC range
- [ ] Sleeping bags in raid base
- [ ] Furnace running in raid base
- [ ] Escape plan (if counter-raid comes)
- [ ] Loot transport plan (horse, boat, mini-copter)
- [ ] Check server time (avoid peak hours if outnumbered)
