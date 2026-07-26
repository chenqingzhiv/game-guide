---
title: "Satisfactory Train Guide"
description: "Complete railway logistics guide — track building, signaling, station design, and throughput optimization."
date: 2026-07-06
tags: [Satisfactory, trains, logistics]
---

## Train Basics

Trains unlock at **Tier 6 — Railway** and transport items across the map with massive throughput.

### When to Use Trains

| Distance | Best Method |
|----------|-------------|
| < 200m | Conveyor belt |
| 200-500m | Truck (rough) or belt (flat) |
| 500-2000m | Single train line |
| 2000m+ | Dual-track main line |

### Train Specs

| Type | Top Speed | Cargo | Fluid |
|------|-----------|-------|-------|
| Standard Loco | 120 km/h | 48 stacks (4×12) | 1,600 m³ |
| Electric Loco | 150 km/h | Same | Same |

**Power:** A 4-car + 2-loco train draws ~100 MW. Add locos for uphill hauling.

## Track Building

### Foundation Alignment

Build on foundations for perfect alignment. Float tracks 2m above foundations for clean curves.

| Parameter | Spec |
|-----------|------|
| Min turn radius | 8 foundations |
| Max grade | 20° (~1:3 slope) |
| Recommended grade | 10° max for heavy freight |
| Support spacing | Every 6-8 foundations |

### Track Architecture

**Dual-track main line** for all long-distance routes — keep 2 foundation gaps between opposing rails for signal clearance.

**Single-track branches** are fine for low-traffic outposts. Add a passing siding if two trains share the same single track.

**Grade management:** Curves + steep grades = massive speed loss. Flat routes need fewer locomotives.

## Stations

### Platform Types

| Platform | Function |
|----------|----------|
| Freight Platform | Load/unload items (set Load/Unload mode) |
| Fluid Platform | Load/unload fluids |
| Empty Platform | Pass-through for dock connections |
| Train Station | Defines name + docking location |

### Optimal Design

3-4 platforms per station is optimal. Place on **straight, flat** track — curved approaches cause docking failures.

**Cargo handling at outpost:** Miner → Industrial Container → Freight Platform (Load). Use two containers per resource for buffering.

**Cargo handling at factory:** Freight Platform (Unload) → Industrial Container → Production. Use smart splitters for mixed loads. Overflow to AWESOME Sink.

### Train Timetable

1. Open Locomotive UI → Add station (Load: **Wait until fully loaded**)
2. Add second station (Unload: **Wait until fully unloaded**)
3. Repeat for multi-drop routes

## Signaling

### Signal Types

| Signal | Function |
|--------|----------|
| Block Signal | Divides track into blocks. One train per block. |
| Path Signal | Reserves path through an intersection. |
| Chain Signal | Forwarding signal — shows status of next signal. |

### Signaling Rules

1. **Path Signal** at every intersection entrance
2. **Chain Signal** 2-3 car lengths before the Path Signal
3. **Block Signal** at every intersection exit
4. **Block Signals** every 8-10 foundations on main lines

### Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Train stops at green signal | Path can't find clear route | Extend exit block for train length |
| Deadlock at T-junction | Missing Block at exit | Add Block Signal on every outgoing track |
| Station approach jam | No Chain Signal before station | Add Chain Signal before station block |
| Trains wait forever | Block too short for train | Enlarge block to fit longest train |

## Advanced — Multi-Train Networks

**Train stacker (waiting bay):** 4-6 parallel bays before high-traffic stations. Chain Signal at stacker exit, Path Signal at main-line merge.

**Throughput estimates:**

| Setup | Items/min | Trains |
|-------|-----------|--------|
| Single train, 1 platform | ~240 (Mk.3 belt) | 1 |
| Dual train, 2 platforms | ~960 (2× Mk.4) | 2-3 |
| Multi-train, 4 platforms | ~2,400 (4× Mk.5) | 4-6 |

Actual throughput depends on route length and station wait times. Buffer containers smooth out intermittent supply.
