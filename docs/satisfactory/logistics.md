---
title: Satisfactory Logistics Optimization Guide — Belt, Pipe, Train & Drone Systems
description: Master Satisfactory logistics. Belt throughput calculations, fluid mechanics and pumps, railway signalling, drone networks, and factory topology optimization.
date: 2026-07-05
---

# 🚚 Satisfactory Logistics Optimization Guide

*Last updated: July 2026 | Game version: 1.0+*

Logistics is the heart of Satisfactory. Moving items efficiently from A to B — across belts, pipes, rails, or through the air — determines whether your factory hums at full capacity or sputters on bottlenecks.

This guide covers every logistics system in depth: throughput math, fluid physics, rail networks, drone routing, and factory-scale topology decisions.

---

## 1. Conveyor Belts — Throughput & Selection

### Belt Speed Comparison

| Belt Tier | Tier Unlocked | Items/min | Items/sec | Splits Into 3 | Max Miner Input |
|-----------|---------------|-----------|-----------|---------------|-----------------|
| **Mk.1** | 0 | 60 | 1 | 20 each | Manual miner |
| **Mk.2** | 2 | 120 | 2 | 40 each | Mk.1 on pure (60/min) |
| **Mk.3** | 4 | 270 | 4.5 | 90 each | Mk.2 on pure (120/min) — needs OC |
| **Mk.4** | 6 | 480 | 8 | 160 each | Mk.3 on pure (240/min) |
| **Mk.5** | 7 | 720 | 12 | 240 each | Mk.3 on pure 250% OC (600/min) |
| **Mk.6** | 9 (post-1.0) | 1,200 | 20 | 400 each | Any miner |

**Belt upgrade urgency:**

```
Tier 0-2:  Mk.1  (60/min) — fine for starter base
Tier 3-4:  Mk.3  (270/min) — critical upgrade before oil
Tier 6:    Mk.4  (480/min) — matches Mk.2 miner on pure
Tier 7:    Mk.5  (720/min) — needed for aluminum
Tier 9:    Mk.6 (1,200/min) — endgame throughput
```

### Belt Throughput Math

Each belt segment has a **maximum throughput**. Exceeding it creates a silent bottleneck — machines at the end starve while the belt is visually full.

**Formula:**

```
Bottleneck = min(Belt Speed, Upstream Production, Downstream Consumption)
```

**Example:** 3 Mk.3 miners at 240 ore/min each = 720 ore/min total.

| Belt | Max | Can handle 720? |
|------|-----|----------------|
| Mk.4 (480/min) | ❌ No | Bottlenecks at 480/min |
| Mk.5 (720/min) | ✅ Yes | Perfect fit |
| Mk.6 (1,200/min) | ✅ Yes | Headroom for expansion |

### Belt Manifold Saturation Time

A manifold feeds machines sequentially. The last machine gets items last.

```
Saturation Time ≈ (Total Buffer ÷ Item Rate) × Machine Count

Example: 10 smelters, each with 100-stack input buffer,
  fed by 480 items/min:
  = (10 × 100 × 1) / 480 = ~2 minutes to fully saturate
  But realistic (with stack size 50) ≈ 1 minute
```

> 💡 **Tip:** Pre-fill manifolds by hand-feeding the last 2-3 machines while the factory warms up. This cuts saturation time by 70%.

### Belt Compression

**Belt compression** ensures items are touching (no gaps) on the belt for maximum throughput.

| Technique | How | Effect |
|-----------|-----|--------|
| **Ore feed from miner** | Natural — miner output is compressed | Perfect |
| **Splitter cascade** | Split a high-rate belt into sub-belts | Maintains compression |
| **Merger cascade** | Merge sub-belts into main line | Gaps may appear |
| **Side-loading** | Feed into the side of a belt segment | Fills gaps, improves compression |
| **Industrial Container buffer** | Buffer before main line | Smooths peaks |

---

## 2. Pipes & Fluid Mechanics

Fluids in Satisfactory are simulated with **volume, head lift, and pressure**. This is more complex than belts.

### Pipe Throughput

| Pipe Tier | Tier Unlocked | Max Flow (m³/min) | Best For |
|-----------|---------------|-------------------|----------|
| **Mk.1 Pipe** | 3 | 300 | Water for generators, early oil |
| **Mk.2 Pipe** | 6 | 600 | High-volume oil, aluminum, nuclear |

**Critical limitation:** A Mk.1 pipe (300 m³/min) can feed at most **6.67 Coal Generators** (each consumes 45 water/min). To feed 8 generators, you need either Mk.2 pipes or a dual-pipe manifold.

### Pump Mechanics

| Pump Type | Max Head Lift | Power | Unlock |
|-----------|---------------|-------|--------|
| **Pump** | 20 m | 8 MW | Tier 3 |
| **Mk.2 Pump** | 50 m | 12 MW | Tier 6 |
| **Valve** | N/A (regulates flow) | 1 MW | Tier 6 |

**Head lift rules:**

1. Every pipe segment has a **maximum height** it can push fluid upward
2. One pump provides 20 m / 50 m of head lift from its placement point
3. **Multiple pumps stack** — place a second pump at the height limit of the first
4. Pumps only lift upward; they do NOT affect horizontal flow

**Pump spacing for vertical pipes:**

```
Vertical rise (m)    Pump Type    Spacing
0-20                Mk.1 Pump    1 pump at bottom
0-50                Mk.2 Pump    1 pump at bottom
20-40               Mk.1 Pump    2 pumps (at 0m, 20m)
50-100              Mk.2 Pump    2 pumps (at 0m, 50m)
```

### Gravity & Fluid Flow

Fluids flow **downhill** naturally — no pump needed downward. But there's a catch:

| Terrain | Flow Direction | Pump Required? |
|---------|---------------|----------------|
| Flat | Both directions | Only for flow rate boost |
| Uphill | Upward | ✅ Required (head lift) |
| Downhill | Downward | ❌ Not needed (gravity) |
| Downhill then uphill | Both | ✅ Pump at lowest point |

### Fluid Buffer Strategy

| Buffer Size | Use Case |
|-------------|----------|
| **Small tank** (1×1, 400 m³) | Byproduct storage, pressure stabilization |
| **Big tank** (2×2, 1,600 m³) | Water for nuclear, main oil storage |
| **Multiple tanks** | Reserve supply for fluctuating demand |

**Best practice:** Place a buffer tank at the **high point** of your pipe system. Gravity feeds machines below. The buffer dampens flow fluctuations from machine cycling.

### Managing Byproduct Fluids

Byproduct fluids (water from aluminum, heavy oil residue from refineries) cause deadlocks when output pipes fill up.

**Solution 1 — Priority valve:** Place a valve on the byproduct return line set to slightly less than the consumption rate. Fresh water input fills the gap.

**Solution 2 — Recycling overflow:** Use a **Junction + Pump** to prioritize using byproduct over fresh input:
```
Fresh water ──[Valve set to 50%]──→ Mixing point → Machine
Return water ──[Pump]──→ Mixing point (pump is free-flow)
```

**Solution 3 — Fluid sink:** Pack the byproduct into containers and send to AWESOME Sink. Wastes resources but never deadlocks.

---

## 3. Railway System

Trains unlock at Tier 6 and are the only logistics system that scales to **continent-wide** distances.

### Track Laying Fundamentals

| Component | Description | Max Speed |
|-----------|-------------|-----------|
| **Railway** | Standard track | 120 km/h |
| **Electric Rail** | Faster track (Tier 7) | 200 km/h |
| **Train Station** | Loading/unloading point | — |
| **Freight Platform** | Cargo loading | — |
| **Fluid Platform** | Fluid loading | — |

**Track topology rules:**

```
✅ Dual-track (one per direction): Maximum throughput
✅ Single-track with passing loops: Lower throughput, simpler
✅ Loops at ends: Trains turn around automatically
❌ Dead-end stations without loops: Trains get stuck
```

### Railway Signalling

| Signal Type | Purpose | When To Use |
|-------------|---------|-------------|
| **Block Signal** | Divides track into blocks | Standard signal between stations |
| **Path Signal** | Complex intersections | At junctions, crossings |
| **No signal** | Single train, single loop | Simplest setup |

**Signal placement rules:**

1. **Block signals every 2-3 train lengths** on mainlines
2. **Path signal at intersection entrance**, Block signal at exit
3. **Signal after every station** — never leave a station without an exit signal
4. **Chain signals** prevent deadlocks at complex junctions

### Train Timetable — Beyond Basics

A good timetable is not just "go from A to B." Optimize with:

| Strategy | Effect |
|----------|--------|
| **Load until full** | Simplest, but wastes time waiting for fill |
| **Time-based departure** | Set a departure timer (e.g., 120 sec) — predictable intervals |
| **Circuit-driven** | Use station outputs → circuit → departure when stock below threshold |
| **Round-robin (multiple stations)** | One train serves 3 stations by order of need |

**Standard timetable pattern:**

```
1. Go to Station A (wait until fully loaded OR 120s timeout)
2. Go to Station B (wait until fully unloaded OR 120s timeout)
3. Go to Station C (wait until fully loaded OR 120s timeout)
4. Go to Station A (wait until fully unloaded OR 120s timeout)
→ Repeat
```

### Train Throughput Calculation

```
Train throughput (items/min) = 
  (Wagon count × Stack size × Item per stack slot) ÷ (Round trip time in minutes)

Example: 4 wagons × 48 slots × 100 items (iron plate) = 19,200 items
  Round trip: 8 minutes
  Throughput: 19,200 ÷ 8 = 2,400 items/min
```

**Compare with belt:** 2,400 items/min = 4 Mk.5 belts or 2 Mk.6 belts. For distances >500m, trains win on throughput per material cost.

---

## 4. Drone Logistics

Drones unlock at Tier 7 and provide **direct point-to-point aerial transport** without tracks.

### Drone Stats

| Stat | Value |
|------|-------|
| **Speed** | ~120 km/h (varies by cargo) |
| **Range** | ~1.5 km without battery recharge |
| **Capacity** | 9 stack slots (variable by item stack size) |
| **Battery consumption** | 1 battery per round trip |

### Drone Port Setup

| Port Type | Function |
|-----------|----------|
| **Drone Port** | Landing pad, cargo exchange, battery charging |
| **Cargo input** | Items to be shipped (belt-fed) |
| **Cargo output** | Received items (belt-fed) |
| **Battery input** | Drone Port needs batteries to operate |

**Minimum drone port setup:**

```
┌──────────────────────┐
│    Drone Port        │
│  ┌──────┐ ┌──────┐   │
│  │Input │ │Output│   │
│  └──────┘ └──────┘   │
│       ▲ Battery ▲     │
└──────────────────────┘
         │
    (battery factory)
```

### Drone Network Design

| Topology | Use Case | Pros | Cons |
|----------|----------|------|------|
| **Point-to-point** | One resource, one destination | Simple, reliable | Doesn't scale |
| **Hub-and-spoke** | Central drone port serves outposts | Efficient for multiple inputs | Hub becomes bottleneck |
| **Round-robin** | One drone serves 3+ ports | Fewer drones | Complex scheduling |

**Best practice:** Drones excel at **low-volume, long-distance** transport — skip belts and trains for items like:

- Supercomputers (2/min from a single manufacturer)
- Radio Control Units (slow production)
- Batteries (for other drones)
- Packaged nitrogen gas (long-distance fluid without pipes)

---

## 5. Factory Logistics Topology

How you organize logistics at the factory scale — **distributed vs. centralized** — dramatically affects throughput and expandability.

### Decentralized (Distributed) Factory

Each production stage has its own dedicated resource nodes:

```
[Iron Node A] → Smelt → Construct → Assembler → Storage (Iron Plates)
[Iron Node B] → Smelt → Construct → Assembler → Storage (Rods)
[Copper Node] → Smelt → Construct → Wire → Storage
```

| Pros | Cons |
|------|------|
| No long belt runs | Harder to balance resources |
| Easy to expand per line | More total buildings/space |
| Clear ownership of resources | Over- or under-producing individual items |
| Good for early game | Late game node shortage becomes complex |

### Centralized (Main Bus) Factory

All raw materials ship to a central processing plant:

```
          ┌─────────────────────────────┐
          │     Central Factory         │
          │  [Smelting] → [Parts] → ...  │
          └─────────────────────────────┘
             ▲              ▲
             │              │
          [Iron Ore]    [Copper Ore]
```

| Pros | Cons |
|------|------|
| Single location, easy to manage | Massive belt throughput required |
| Efficient resource sharing | One bottleneck halts everything |
| Good for UPS/performance | Gigantic building footprint |
| Endgame scalable | Requires trains to feed |

### Hybrid (Recommended)

A mix of both — process raw ore into ingots at the mine, ship ingots to central, then distribute final parts:

```
[Mine] → Smelt on-site → Train Ingots → Central Factory →
  → Make parts → Train to satellite factories → Final assembly
```

| Pros | Cons |
|------|------|
| Best of both worlds | More complex to plan |
| No raw ore transport needed | Requires both trains + belts |
| Easy to scale each satellite | Higher initial infrastructure cost |
| Good UPS (less belt travel) | |

---

## 6. Load Balancers vs Manifolds (Advanced)

### When to Use Each

| Scenario | Manifold | Load Balancer |
|----------|----------|---------------|
| Large array of same machines (8+ smelters) | ✅ Best choice | ❌ Too complex |
| Small array (2-4 machines) | ✅ Fine | ✅ Also fine |
| One belt feeds different item types | ❌ Wrong tool | ❌ Wrong tool (use smart splitter) |
| Nuclear fuel rod production | ❌ Inconsistent flow | ✅ **Mandatory** |
| Perfect ratio factory (no warm-up) | ❌ Slow saturation | ✅ Instant |
| Space-constrained build | ✅ Compact | ❌ Bulky |
| Scalable to N machines | ✅ Just extend belt | ❌ Redesign needed |

### Power of 2 Load Balancer

A 1→4 load balancer (using only splitters):

```
          ┌──[Splitter]──┐
          │              │
     [Splitter]      [Splitter]
       │      │        │      │
      Out1   Out2     Out3   Out4
```

Each output receives exactly **25%** of input. Works perfectly for 2, 4, 8, 16... machine counts.

### Non-Power-of-2 Load Balancer (e.g., 1→3)

```
          ┌──[Splitter]───────┐
          │                   │
       Out1 (33%)         [Splitter]
                            │      │
                          Out2    Out3
                           (33%)  (33%)
```

This balances 1 input to 3 outputs evenly. The concept extends to any N-machine count using combinations of splitters and mergers.

### Hybrid Approach — Clustered Manifold

Use a load balancer to distribute to **clusters** of machines, then manifold inside each cluster:

```
Input → [1→3 Load Balancer]
          ├── Cluster 1: Manifold → 8 Smelters
          ├── Cluster 2: Manifold → 8 Smelters
          └── Cluster 3: Manifold → 8 Smelters
```

This gives faster saturation than a pure manifold and simpler belts than a pure load balancer.

---

## 7. Logistics Decision Matrix

Choosing the right transport method:

| Distance | Volume | Best Method | Why |
|----------|--------|-------------|-----|
| <100m | Any | Belts | Simple, reliable, zero power for passive belts |
| 100-500m | High | Belts | Still efficient, belt cost is low |
| 100-500m | Low | Tractors/Trucks | Fun, no track needed, but fuel cost |
| 500-2000m | High | Trains | Best throughput per infrastructure cost |
| 500-2000m | Low | Drones | No tracks, no fuel (just batteries) |
| 2000m+ | High | Trains | Trains only realistic option |
| 2000m+ | Low | Drones | Cheaper than building 2km of track |
| Intercontinental | Any | Drones + Trains | Drone to shore, train across continent |

### Bottleneck Troubleshooting Flowchart

```
Is a machine getting enough input?
├─ Yes → Check output (is output belt full?)
│        ├─ Yes → Check downstream consumption
│        └─ No → Upgrade output belt
└─ No → Follow the supply chain backward
         ├─ Belt? → Check belt speed vs required throughput
         ├─ Splitter? → Check if split is balanced
         ├─ Pipe? → Check pump head lift + pipe flow rate
         ├─ Train? → Check station loading/unloading speed
         └─ Drone? → Check battery supply + drone port throughput
```

---

## 8. Performance (UPS) Considerations

Logistics systems affect game performance differently:

| System | Performance Cost | Notes |
|--------|-----------------|-------|
| **Belts** | Low-Medium | 1000+ belt segments = measurable cost |
| **Pipes** | Medium | Fluid simulation is more expensive than belts |
| **Trains** | Low | One train = ~few belts' worth |
| **Drones** | Medium | Pathfinding for airborne entities |
| **Vehicles (trucks)** | High | Physics simulation for each vehicle |

**For megabases:**
- Prefer **trains** over vehicles (trucks have full physics)
- Use **belts** for short distances, trains for long
- Minimize **pipe segments** — use barreled delivery or trains for fluid
- **Drones** are fine for low-count operations (5-10 drones)

---

## 🔗 Related Guides

- [Satisfactory Complete Guide](/satisfactory/) — Main hub
- [Production Line Guide](/satisfactory/lines/) — Belts, manifolds, ratios
- [Blueprint System Guide](/satisfactory/blueprints/) — Save time with modules
- [Tier Progression](/satisfactory/tiers/) — When each logistics option unlocks
- [Power Systems](/satisfactory/power/) — Power for your logistics

---

## 🎮 Get Satisfactory

[**🎮 Satisfactory on Steam — $34.99**](https://store.steampowered.com/app/526870)

*This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*

---

*Last updated: July 2026 | Game version: Satisfactory 1.0+*
