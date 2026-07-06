---
title: "DSP Dark Fog Expansion"
description: "Ground bases, space hives, resource farming, combat buildings, and hive brain fight."
date: 2026-07-06
tags: [DSP, dark-fog, expansion, combat]
---

## Dark Fog Overview

Two layers: **ground bases** (mine resources, attack factory) and **space hives** (coordinate attacks). Destroying ground bases weakens the hive; killing the hive makes ground bases decay.

## Ground Bases

| Type | Difficulty | Defenders | Loot |
|------|-----------|-----------|------|
| Scout Outpost | Easy | 2-4 scouts | Iron/copper, early tech |
| Mining Base | Medium | 6-12 + 2 turrets | Processed ores |
| Military Base | Hard | 12-20 + 4 turrets + shield | Combat tech components |
| Relay Station | Very Hard | 20+ + 8 turrets + shield | Rare components |

Each base: Relay tower (brain) → Mining drills → Spawning pools → Shield gen → Depot (loot).

### Expansion

| Difficulty | New Relay | Expansion | Military Upgrade |
|-----------|-----------|-----------|-----------------|
| Low | Never | 2+ hours | 10+ hours |
| High | 15-30 min | 20 min | 1.5 hours |

### Assault Strategy

Scout from altitude → clear outer ring → destroy spawning pools → kill relay tower (disables ~20 min) → mine depot. Loadout: Tesla Tower, Rifle + explosive ammo, 40 foundations, 20 repair packs.

## Space Hives

| Part | HP | Priority |
|------|-----|----------|
| Relay Docking | 5,000 | First (stops expansion) |
| Fighter Hangar | 10,000 | Second (reduces waves) |
| Bomber Bay | 15,000 | Third (stops heavy attacks) |
| Energy Core | 50,000 | Later |
| Hive Brain | 100,000+ | Last (final boss) |

### Strength by Distance

| Distance | Relays | Fighters | Core HP |
|----------|--------|----------|---------|
| Home | 2-3 | 10-20 | 50,000 |
| Adjacent | 4-5 | 20-40 | 75,000 |
| Mid-range | 6-8 | 40-80 | 100,000 |
| Far edge | 10+ | 80-150 | 200,000+ |

### Weakening the Hive

- Clear all ground bases: -20% HP, -1 relay spawn
- Kill relay stations: -30% shield recharge
- Destroy fighter hangars: -60% fighter spawn
- Planetary shield per planet: prevents new relays

## Resource Farming

**Loop:** Clear base to relay tower → regenerate (20-30 min) → re-kill → collect loot.

| Evolution | Loot Mult | Drops |
|-----------|-----------|-------|
| 0-20% | 1× | Iron, copper |
| 20-40% | 1.5× | + Circuit boards |
| 40-60% | 2× | + Processors |
| 60-80% | 3× | + Quantum chips |
| 80-100% | 4× | + Dark matter |

Keep evolution at 40-70% for optimal farming.

## Tech Priority

| Tech | Cost | Key Unlock | Rush |
|------|------|-----------|------|
| Basic Combat | 10R+10B | Gauss turret | Yes |
| Energy Weapons | 20R+20B+10Y | Laser turret (no ammo!) | Yes |
| Explosives | 30R+20B+15Y | Missile launcher | Yes |
| Shield Tech | 40R+30B+20Y | Shield gen + plasma turret | **Highest** |
| Fleet Command | 50R+40B+30Y+10P | Ships | Mid |
| Planetary Fortress | 60R+50B+40Y+20P | Planet shield, implosion | Late |
| Hive Analysis | 70R+60B+50Y+30P | Hive scanner | Pre-assault |

Path: Basic → Energy → Explosives → Shield → Fleet → Fortress → Hive Analysis.

## Buildings

| Building | Cost | Power | Purpose |
|----------|------|-------|---------|
| Gauss Turret | 20 iron + 10 copper | 0.5 MW | Point defense |
| Laser Turret | 30 titanium + 15 circuit | 1.5 MW | No ammo needed |
| Missile Launcher | 20 steel + 10 processor | 2.0 MW | AOE splash |
| Plasma Turret | 30 Ti-alloy + 10 proc | 3.0 MW | Anti-fleet piercing |
| Implosion Turret | 50 Ti-alloy + 20 proc | 5.0 MW | Burst AOE |
| Shield Generator | 20 steel + 10 proc + 5 magnet | 50 MW | Local shield (20m) |
| Planetary Shield | 100 frame + 50 proc + 20 quantum | 500 MW | Full planet shield |
| Combat Logistics | 50 steel + 20 proc + 10 frame | — | Ammo + repair drones |
| Battle Analysis | 30 proc + 10 quantum chip | — | Predicts attacks |

## Endgame: Hive Brain

**Prereqs:** Hive Analysis, 200+ ships (100 corvs + 50 dest + 50 cruisers), Planetary Shield on all planets, forward base with 500+ missiles.

**Phase 1 (100%→60% HP):** Destroy relay docks + fighter hangars. 30-50 fighter waves.

**Phase 2 (60%→25%):** Bomber bays active — kill first. Core shield activates (100,000 HP).

**Phase 3 (25%→0%):** All defenders swarm. Core regens 500 HP/sec. Focus fire the core.

| Reward | Source | Use |
|--------|--------|-----|
| Hive Core | Final kill | Cosmology catalyst |
| Dark Matter Crystal | Hangar kills | Graviton lens |
| Research Data (×10,000) | Full clear | Hidden tech tree |

**After victory:** No new relays. Ground bases decay. Hive does not respawn. Each kill boosts Cosmology research (final tech category).
