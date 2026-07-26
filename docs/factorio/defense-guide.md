---
title: "Factorio Defense Guide"
description: "Complete defense guide — evolution factor, turret configurations, wall designs, artillery, and pollution management."
date: 2026-07-06
tags: [Factorio, defense, combat]
---

## Evolution Factor

Evolution starts at 0 and climbs to 1.0. Three sources increase it:

| Source | Rate | You Control |
|--------|------|-------------|
| Time | +0.0005%/sec (passive) | Nothing |
| Pollution | +2.0 per 1M generated | Miners, power, efficiency modules |
| Nest destruction | +0.4% per nest | Which nests to clear |

### Thresholds

| Evolution | Biters | Spitters | HP | Ammo Needed |
|-----------|--------|----------|-----|-------------|
| 0-25% | Small | None | 10-15 | Yellow |
| 25-50% | Medium | Small | 75 | Red (piercing) |
| 50-75% | Big | Medium | 375 | Piercing + flame |
| 75-90% | Behemoth | Big | 3,000 | Uranium |
| 90-100% | All behemoth | Behemoth | 5,000+ | Full grid |

**Key insight:** Nest destruction is the fastest evolution driver. Only clear bases inside your pollution cloud.

## Turret Stats

| Turret | Damage | Range | Ammo | Best Use |
|--------|--------|-------|------|----------|
| Gun Turret | 5-10 | 18 | Yellow/Red/Uranium | Early-mid backbone |
| Laser Turret | 15 | 24 | Electricity (1.2 MW) | Late-game with nuclear |
| Flamethrower | 25 DPS | 30 | Crude/heavy oil | Melts biter clumps |
| Artillery | 1,500 | 224-448 | Shells | Nest clearing at range |

## Defense Tiers by Phase

### Early (Evo 0-15%) — Pillbox

4 gun turrets behind 1 layer of stone wall. One pillbox every 15 tiles on the pollution-facing edge. Hand-feed yellow ammo (200+ mags buffered).

### Mid (Evo 15-50%) — Perimeter Wall

3 wall layers + turrets every 6 tiles (piercing ammo) + flamethrowers every 10 tiles. Run crude oil pipe behind the wall. Laser turrets on flanks for cleanup.

### Late (Evo 50-75%) — Dragon's Teeth

Staggered wall segments 5-6 tiles before your main wall. Biters path around them, clumping up, making flamethrower AOE devastating. Configuration:

```
[Dragon's teeth maze] → [3× Wall] → [Gun][Flame][Gun][Flame] → [Lasers row 2]
```

Use requester chests or ammo belt loops to auto-feed. A yellow belt of piercing ammo feeds ~20 gun turrets.

### Megabase (Evo 75-100%) — Full Fortress

- 2 layers of dragon's teeth (10 tiles deep)
- 2 rows of land mines
- 4 wall layers + uranium turrets
- Flamethrower at 5-tile intervals
- Roboport with repair packs every 15 tiles
- Construction bots auto-repair walls

**Uranium ammo:** One gun turret kills a behemoth in 2 shots. 10× stronger than piercing.

### Artillery Outpost

Place 6 cannons + 20 lasers + 10 uranium gun turrets + 6 flamethrowers + 4 wall layers. Supply shells by train. Artillery auto-targets nests within 448 tiles (with upgrades).

## Pollution Management

Pollution triggers attacks. Reducing it is often cheaper than fighting.

### Efficiency Modules

| Machine | Base Pollution | 2× Eff1 |
|---------|---------------|---------|
| Electric Miner | 10/m | 5/m (-50%) |
| Electric Furnace | 1/m | 0.5/m |
| Assembler 2 | 2/m | 1/m |

### Zero-Pollution Power

**Solar:** 1,400 panels + 1,200 accumulators for 60 MW. Zero pollution, permanent.
**Nuclear:** 0.1 pollution/m per reactor. One 2-reactor setup (160 MW) replaces 4,000 panels.

### Natural Absorbers

| Tile | Absorption |
|------|-----------|
| Trees | 0.002/m (best, but die at 20 pollution) |
| Grass | 0.0015/m |
| Sand/Dirt | 0.001/m |
| Water/Concrete | 0/m |

Preserve trees between your base and biter nests — they absorb 33% more pollution than grass.

## Final Tips

1. **Wall chokepoints** — narrow terrain between cliffs/water needs 80% fewer defenses
2. **Lay your defense** — single wall + single turret dies to behemoths
3. **Efficiency before productivity** — 30% less pollution is huge
4. **Don't overclear** — destroying bases speeds evolution
5. **Artillery warns you** — when shells fire, biters are coming. Be ready.
6. **Perimeter alert** — speaker + biter proximity sensor = early warning
