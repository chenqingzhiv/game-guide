# Satisfactory Factory Building Guide

A practical guide to building efficient, scalable factories in Satisfactory — from your first iron plate to a mega-factory fed by trains and drones.

---

## Why Foundations Matter

New players often snap machines directly to the terrain, only to discover what veterans call "the spaghetti." Belts refuse to line up, splitters fight gravity, and expanding a section means rebuilding half the factory. **Foundations solve all of this.**

| Benefit | Why It Matters |
|---|---|
| Grid alignment | Machines snap to the world grid, making parallel belts and perfect manifold layouts effortless. |
| Vertical stacking | Stacking machines upward is only possible on foundations. |
| Clean logistics | Belts run straight, splitters align, and you never chase a belt through a forest. |

Place your first 4m x 4m concrete foundation at World Grid origin (press **Ctrl** while placing to snap). From that single tile, build out in any direction — every future foundation will align perfectly. **Always start every factory with one snapped-to-grid foundation.**

Blueprints (detailed below) also require a foundation surface to be placed on, so establishing a solid floor early pays off massively later.

---

## Build Up, Not Out

The biggest mistake new factory builders make is sprawling horizontally. Building up is almost always better:

- **Compact footprint**: A 4-story factory fits in the space of a 1-story one, leaving room for trains, belts, and nature.
- **Gravity-fed logistics**: Items flow down via lift, reducing belt complexity on lower floors.
- **Easier expansion**: Add another floor instead of clearing more forest.
- **Performance**: One tall building renders better than twenty scattered sheds (Satisfactory's engine handles vertical density well).

A common mid-game layout:

| Floor | Purpose |
|---|---|
| Ground | Raw material input (miners, resource wells) |
| Floor 1 | Primary smelting / refinement |
| Floor 2 | Intermediate parts (rods, plates, screws) |
| Floor 3 | Advanced assembly (modular frames, motors) |
| Floor 4 | Final products → storage or logistics |

Conveyor lifts between floors replace dozens of meters of horizontal belts.

---

## Logistics Floors (The Hidden Belt Trick)

This is the single most impactful technique in Satisfactory: **hide your messy belts between floors**.

Build your production floor on top of a 4m-high foundation layer, then snap a second layer of foundations **two wall heights (8m)** below it. Route all your belts, splitters, and mergers in the gap between the two floors. On the production floor above, you only see clean machines with lift inputs popping up through the floor.

**How to execute:**

1. Build a 4m foundation at working height (your "logistics floor").
2. Place all belts, splitters, mergers, and storage on this layer.
3. Snap another 4m foundation 4m above it (use walls or frame floors as guides).
4. Place production machines on the upper floor, feeding them with conveyor lifts from the logistics layer below.

The result: a factory floor with zero visible belts. Item inputs/outputs come through neat 1x1 floor holes. This isn't just cosmetic — it makes debugging and expanding dramatically easier since you can see every machine clearly.

---

## Train Logistics

Trains become available in Tier 6 and completely change how you think about logistics. They are the right solution when:

- **Distance > 1 km** between resource nodes and factory.
- **Throughput > 1 belt** (a single freight car holds 32 stacks, and trains run fast).
- **Multiple resources** share a route (one train can haul copper, iron, and coal in different cars).

### Rail Layout Tips

- **Always build double-track** (one rail each direction). Single-track with passing loops works but kills throughput as your network grows.
- **4m foundation width per track** — build your rail bed 2 foundations wide for bi-directional.
- **Minimum turn radius**: 10 foundation tiles for 300 km/h path signals; tighter turns force speed limits and introduce throughput bottlenecks.
- **Signals**: Use **Block Signals** between stations and **Path Signals** on intersections. Path signals let multiple trains share an intersection simultaneously if their paths don't conflict.
- **Station placement**: Put stations on a *branch* off the main line, not inline. An inline station forces following trains to wait.

### The Train Logistics Floor Trick

Since train stations are 9 foundations long (station + 2 supports), build them on a raised foundation platform and run your factory logistics *under* the rail bed — belts from station outputs feed directly down into your factory below.

---

## Truck & Tractor Routes

Trucks and tractors are excellent mid-game alternatives to long conveyor belts (Tier 3–5), especially for resources spread across moderate distances (200 m – 1 km).

**Setting up a reliable route:**

1. Place a **Truck Station** at pickup and drop-off.
2. Drive the route manually — the vehicle records the path while you drive.
3. Press **R** to record, drive the full loop, press **R** again to stop recording.
4. Set the vehicle to **"Autopilot"** and load/unload settings.

**Common pitfalls:**

- **Fuel starvation**: Send a second truck with fuel, or belt-pack coal/compacted coal to the station. Trucks also accept batteries (late game).
- **Path drift**: Vehicles are physics objects — bumps, collisions, or creatures can push them off course. Build a simple 2-foundation-wide road for critical routes.
- **Throughput math**: A truck moving 30 m/s carries ~9 stacks per trip. Check the travel time vs. production rate before scaling.

When you unlock **Exploration**, upgrade to trucks over tractors for higher cargo capacity and better terrain handling.

---

## Drone Ports (Late Game Logistics)

Drones unlock at Tier 8 and are the ultimate "set and forget" logistics for low-volume, high-value items.

**Best uses for drones:**

- Shipping Supercomputers, Radio Control Units, or other high-end parts to the Space Elevator.
- Supplying low-volume inputs like Quartz Crystals or Alumina to remote factories.
- Quick player resupply — a single drone port with a hover-pack-ready parts crate.

**Design rules:**

- Drones consume **batteries** (or **packaged fuel** with a later upgrade) per trip. The receiving port also needs a battery supply.
- One drone per port. Multiple ports = multiple drones. A single drone can service multiple ports, but that gets complicated — stick to one-to-one for sanity.
- **Range**: Drones fly ~1.5 km by default, extended with the Explorer drone milestone. Don't try to cross the entire map with one drone hop.
- Build drone ports on **rooftops** — that space above your factory is wasted otherwise. A flat foundation roof with 4–6 drone pads makes an excellent distribution hub.

---

## The Blueprint System

Blueprints unlock in the **MAM** under the **Blueprint** research chain (requires 500 concrete and 100 Iron Rods). They are the single biggest time saver in Satisfactory.

**What to blueprint:**

| Blueprint | Why |
|---|---|
| 3x3 Manifold (smelters/constructors) | Drop 9 smelters perfectly aligned with belts in one click. |
| 1x1 Logistics Floor Tile | Pre-built 4m foundation with lift hole and belt feed underneath. |
| Train Station + Unloader | The full 9-tile station with outputs routed to a logistics floor. |
| 4x4 Power Plant | Coal/generator arrays with water extractor plumbing. |
| 5x5 Storage Wall | Wall-to-wall storage containers with belt bus underneath. |

**Pro tip:** The blueprint designer can be upgraded to larger sizes (up to 5x5) by researching in the MAM. Always use the largest available size — you can always leave space empty, but you can't fit more into a small designer.

Build your blueprints on a flat foundation inside the designer. Use **World Grid snap** (Ctrl-click) so every blueprint aligns perfectly regardless of where you drop it.

---

## Building Aesthetics vs. Efficiency

Satisfactory is uniquely rewarding for builders who care about looks. The game's structural pieces (walls, roofs, pillars, windows, catwalks) are versatile enough to make factories that genuinely look like real industrial architecture.

**When to prioritize efficiency:**

- Early game (Tier 1–3): Box it in and move on. Your early buildings will be replaced.
- Intermediate (Tier 4–6): Add structural columns and glass walls — still fast but looks clean.
- Late game (Tier 7+): Go wild. Color-code floors, add catwalks, use painted beams for exposed structural framing.

**Practical aesthetic tips:**

- **Color gun**: Assign a factory color (Ctrl-click a building, set the color). Color-code by production tier: gray for smelting, yellow for parts, green for electronics, etc.
- **Windows**: Use 2m glass walls for observation decks and natural light.
- **Signage**: The in-game sign system can create "floor directories" — place a tall sign at each elevator bank listing what's on that floor.
- **Interior lighting**: Add wall lights or ceiling lights to factory floors. Dark factories hide belt errors.
- **Roofs**: A flat roof is wasted. Put drone ports, storage buffers, or a viewing platform up there.

**The golden rule:** A factory that looks good is easier to debug. When belts and machines are neatly arranged, spotting a missed connection or underclocked machine takes seconds instead of a guided tour.

---

## Summary Checklist

| Phase | Action |
|---|---|
| First foundation | Snap to World Grid (hold Ctrl). |
| Tier 1–3 | Box building, spaghetti belts, get through it. |
| Tier 4–5 | Start logistics floors. Make blueprints for your manifold designs. |
| Tier 6 | Build your first double-track rail line. Branch stations off the main line. |
| Tier 7–8 | Add drone ports on rooftops. Color-code and polish aesthetics. |
| Endgame | Blueprint everything. Build a dedicated storage/transfer building with train input. |

---

*Satisfactory is available on Steam.*  
[**Support the developer — get Satisfactory on Steam**](https://store.steampowered.com/app/526870/Satisfactory/)

---

*Guide last updated for Update 8 / 1.0 release. ~1650 words.*
