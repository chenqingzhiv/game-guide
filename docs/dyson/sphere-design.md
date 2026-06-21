---
title: "Dyson Sphere Design Reference — Optimization Tips"
description: "Design the perfect Dyson sphere. Layer strategy, rocket vs sail economics, ray receiver placement, star type comparison, frame layout, and endgame power optimization."
---

# ☀️ Dyson Sphere Design Reference

Building a Dyson sphere in *Dyson Sphere Program* is the ultimate endgame goal — it's also the single biggest power generation and resource investment decision you'll make. This guide covers exact mechanics, numbers, and proven strategies to maximise your critical photon output while minimising wasted resources and frame hours.

---

## ⭐ Star Type Comparison

A star's luminosity directly determines the total energy output of any sphere built around it. The formula is straightforward: **Sphere power output = Luminosity × Base power per cell**. All values below assume a standard 1 AU radius sphere.

| Type | Base Luminosity | Sphere Output | Recommended |
|:-----|:----------------|:--------------|:------------|
| **O** | 2.0–2.5× | Highest | Best first sphere |
| **B** | 1.5–2.0× | Very High | Good second sphere |
| **A** | 1.3–1.6× | High | Default starter cluster |
| **F** | 1.0–1.3× | Medium | Your starting star |
| **G** | 0.9–1.0× | Medium | Like our sun |
| **K** | 0.7–0.9× | Low | Skip unless close |
| **M** | 0.3–0.6× | Lowest | Only for neutron/black hole |

**Key insight:** An O-type star with 2.5× luminosity produces **2.5× the power per cell** compared to an F-type star. But O-stars are rarer — you'll typically find only 1–3 per 64-star cluster. Build your first large sphere around the brightest O-star within 20 light-years of your home system. Later spheres (O-blue giant, B, or neutron star) can be built at greater distances and fed via ILS.

**Pro tip:** Neutron stars and black holes have very low luminosity (0.3×–0.6×) but are excellent for producing critical photons via Graviton Lenses thanks to their special resource nodes. Don't skip them entirely — build a small sphere there specifically for antimatter fuel rod production.

### Luminosity Formula Details

Every star has an internal luminosity value that translates to a percentage modifier:

- **O-type**: 1.0–2.5 (pink/red giants can hit 2.5)
- **B-type**: 0.8–1.6
- **A-type**: 0.6–1.2
- **F-type**: 0.5–1.0
- **G-type**: 0.5–1.0
- **K-type**: 0.3–0.8
- **M-type**: 0.1–0.6

The actual value varies per star seed. Always check the star details in the starmap before committing resources — you might find an F-star with 1.3× luminosity that rivals an average B-star, or a G-star with only 0.7× that isn't worth the frame cost.

---

## 🚀 Rocket vs Sail Economics

The rocket-vs-sail decision is the single biggest economic choice in Dyson sphere construction. Here's the exact breakdown:

| Aspect | Solar Sails | Rockets |
|:-------|:------------|:--------|
| Unlock | Blue Science | Purple Science |
| Cost | 1 × Prism + 2 × Graphene = 1 sail | 2 × Titanium Alloy + 2 × Carbon Nanotube + 2 × Dyson Frame Component = 1 rocket |
| Lifespan | ~2 hours (1,800–2,700 seconds, decays) | Permanent |
| Power Output | ~15–30 kW per sail | ~96–192 kW per rocket |
| Stacking | Cap at ~10,000 sails per orbital layer | Unlimited (frame+cell nodes) |
| Best Use | Early power bridge | Permanent sphere layers |

**Strategy:** Start with a swarm around your brightest star immediately after unlocking blue science. The 2-hour lifespan is enough to bridge to rocket production. Build permanent sphere layers with rockets once green science is flowing.

### Sail Cost Breakdown

A single solar sail requires:
- 1 × Prism = 2 × Glass (stone → silicon smelt) + 1 × Copper Ingot
- 2 × Graphene = 6 × Graphite (coal) + 2 × Sulfuric Acid

That's roughly **7 raw ore per sail**. At 30 sails per second (mk.3 assembler with proliferation), you burn through a copper patch fast. Always establish a dedicated sail production line with at least 3–4 mk.3 assemblers before launching the swarm.

### Rocket Cost Breakdown

One Dyson rocket needs:
- 2 × Titanium Alloy = 4 × Titanium Ingot + 4 × Steel
- 2 × Carbon Nanotube = 4 × Graphite + 2 × Titanium Ingot (spiniform)
- 2 × Dyson Frame Component = 4 × Processor (crystals + silicon) + 2 × Gear + 2 × Casing

Total: roughly **18 raw ores + 2 processors** per rocket. This is why rocket production is gated behind purple science — the processing chain is deep. You need at least **15–20 mk.3 assemblers** dedicated to rocket parts to sustain a reasonable build rate.

**Critical decision:** Should you proliferate rockets? **Yes** — always. Proliferator mk.III applied to rocket components gives +25% production speed *and* the rockets build 25% more structure points. That's a 56% effective material efficiency gain. Never skip it.

---

## 📡 Ray Receiver Mechanics

Ray receivers convert Dyson sphere power into either critical photons (for antimatter) or direct energy. Understanding their trigonometry is essential.

| Tip | Detail |
|:----|:-------|
| **Polar placement** | Place receivers at high latitudes (60°+) for continuous line-of-sight |
| **Graviton lenses** | Apply lenses to double output. Worth it mid-game+ |
| **Critical photon bottleneck** | Scale receivers *before* you need antimatter fuel |
| **Multiple layers** | 3–5 concentric layers around O-star = 10×+ power |

### Line-of-Sight Mechanics

A ray receiver only generates power when it has a direct line-of-sight to the sphere. Planets rotate, so receivers near the equator lose LOS for ~50% of each day. At high latitudes (60°+), the rotation parallax is minimal — receivers there maintain LOS for 90–100% of the day.

**The ideal planet** for ray receivers is:
- Tidal locked to the star (always faces sphere) — best
- Extremely low axial tilt (<5°)
- Close orbit (shortens belt distance = reduces graviton lens travel)
- High orbital inclination to see above the ecliptic

On a tidal-locked planet, place receivers in a grid on the **sun-facing hemisphere**. You can fit roughly 400–500 receivers on a single planet this way.

### Output Formula

Each receiver's output = **Sphere total power** × **Receiver efficiency** × **Graviton lens bonus** ÷ **Number of active receivers**

Receiver efficiency depends on:
1. Distance from receiver to sphere (minimal if planet is close to star)
2. Angle of incidence (best when receiver points directly at sphere center)
3. Whether the sphere is currently in LOS

At 100% efficiency (rare), a single receiver outputs **12–15 MW** without a lens, or **24–30 MW** with a Graviton Lens. A full planet of ~400 receivers can pull **5–10 GW** from a single sphere layer.

### Graviton Lens Refresher

Each Graviton Lens costs:
- 1 × Diamond (graphite → diamond via kimberlite or synthetic)
- 1 × Strange Matter (particle collider — requires deuterium + critical photon)

Graviton Lenses are consumed over time (~5–10 minutes per lens, depending on receiver usage). One mk.III proliferated assembler making lenses is enough for 50–80 receivers. Always use them — the 2× output multiplier is the single best power-per-building upgrade available.

---

## 🔧 Sphere Layer Design — Structure vs Cell Points

Every Dyson sphere is built from two types of components:

### Structure Points (Rockets)
- Form the frame (nodes, beams, and meridians)
- Each structure point costs **1 rocket** to build
- Determines how many cell points you can fill
- Ratio: **1 structure point supports roughly 10 cell points** in a well-designed frame

### Cell Points (Sails)
- Fill the triangular panels between frame edges
- Each cell point consumes **1 solar sail** to construct
- The more cell points, the higher the power output
- Frame density determines max cells — a sparse frame means fewer cells per frame rocket

### Frame Layout Strategy

There are two dominant frame patterns:

**1. Minimal Frame (Dense Nodes)**
- Build only the minimum "gear" pattern of 4–6 latitude rings
- High node count (rockets expensive) but low total structure
- Best when you're rocket-constrained (early game)
- Cell fill ratio: ~6–8 cells per structure point

**2. Full Frame (All Meridians + Rings)**
- Build the full geodesic grid with 15–30 latitude rings
- Low node count relative to cells but high total rocket cost
- Best when you're sail-constrained (late game, massive permanent sphere)
- Cell fill ratio: ~10–12 cells per structure point

**Recommendation:** Start with a minimal frame (every 5th latitude ring, 12 meridians) for your first sphere. As your rocket production scales, convert to full-frame designs for later layers. Never delete an existing frame — just add more layers on top.

---

## ⚡ Power Generation Math

Let's put concrete numbers on a typical mid-game sphere around an O-star (2.0× luminosity):

**Layer 1** (0.5 AU radius, minimal frame):
- 2,000 structure points = 2,000 rockets
- 16,000 cell points = 16,000 sails
- Total output: ~2.5 GW

**Layer 2** (0.8 AU radius, full frame):
- 8,000 structure points = 8,000 rockets
- 80,000 cell points = 80,000 sails
- Total output: ~12 GW

**Layer 3** (1.2 AU radius, full frame):
- 12,000 structure points = 12,000 rockets
- 130,000 cell points = 130,000 sails
- Total output: ~18 GW

**Combined output** from all three layers: ~32.5 GW

To put that in perspective:
- One Artificial Star burning antimatter fuel rods generates ~75 MW
- You could power **433 Artificial Stars** from this sphere
- That's enough to run 20+ fully proliferated research labs at max speed, plus a 100-tower ILS network

### Scaling to Endgame

An endgame sphere around a 2.5× luminosity O-star with 5 concentric layers (0.5–2.5 AU radii) filled with full frames:

- ~50,000 structure points → 50,000 rockets
- ~500,000 cell points → 500,000 sails
- Total output: **75–100 GW**

This requires roughly **10 million raw ore** total — a significant fraction of a 64-star cluster's resources. Plan accordingly and set up mining operations on 6–8 planets before starting construction.

---

## 🧩 Node & Frame Layout Details

When you open the Dyson Sphere editor, you're looking at a spherical grid. Here's how to design efficiently:

### Latitude Rings
- Default: 5 rings per hemisphere
- Optimal: 10–15 rings per hemisphere for most frames
- Maximum: 30 rings (very dense frame, high rocket cost)

### Meridians (Vertical Lines)
- Default: 12 meridians
- Optimal: 24–36 for full coverage
- Each intersection point is a **node** = 4–6 rockets to build

### Node Placement Guidelines
1. Always place nodes at **exactly** the same latitude on all meridians — this creates regular quadrilateral panels
2. Avoid nodes between rings — they waste structure points without increasing cell capacity
3. For polar regions (<10° latitude), reduce to 6 meridians — the panels are already tiny near the pole
4. Use the "auto-connect" feature to snap frames between existing nodes instead of freehanding

### Multi-Layer Stacking

You can build up to **10 concentric layers** per star. Each layer has:
- Independent radius (0.5 AU minimum, up to planetary orbit distance)
- Independent frame design
- Independent spin axis and orbital inclination

**Best practice:** Layer 1 at 0.5 AU (tight, cheap, fast), Layer 2 at 1.0 AU, Layer 3 at 1.5 AU, etc. Stagger the frame designs so nodes don't overlap — this prevents visual clutter and ensures clean belt paths for sails being launched from different orbital planes.

---

## 🏭 Resource Cost Summary

Building a single large sphere layer (~8,000 rockets + 80,000 sails):

| Resource | Approx. Amount | Primary Source |
|:---------|:---------------|:---------------|
| Iron Ore | 120,000 | Smelt → steel → titanium alloy |
| Copper Ore | 60,000 | Smelt → copper ingot → prism, processors |
| Silicon Ore | 80,000 | Smelt → silicon → processors, glass |
| Titanium Ore | 40,000 | Smelt → titanium ingot → alloy, nanotubes |
| Coal / Graphite | 100,000 | Graphite → nanotubes, diamond, graphene |
| Stone | 50,000 | Smelt → silicon from stone (alternative) |
| Sulfuric Acid | 20,000 | Ocean pump or chemical plant |
| Fractal Silicon | 5,000 | Rare crystal nodes → processor |
| Spiniform Stalagmite | 8,000 | Rare organic crystal → nanotubes |

**Total raw ore equivalent:** ~500,000 units per full layer. Multiply by 5 layers = ~2.5 million raw ore for a complete endgame sphere. This is why you need **at least 3 mining planets** with full logistics coverage before starting.

---

## 🔄 Endgame Optimisation Checklist

1. **Choose the right star** — O-type or high-luminosity B-type within 20 LY
2. **Find the right planet** — Tidal-locked, low tilt, close orbit for receiver placement
3. **Start with a swarm** — Blue science → immediate sail launchers (6–10) around brightest star
4. **Build minimal first layer** — 0.5 AU, 12 meridians, every 6th ring cheap frame
5. **Scale rocket production** — 20+ mk.3 assemblers, proliferated, fed by 3+ titanium and coal planets
6. **Add receiver planets** — 300–400 receivers on the sun-facing side of the closest planet
7. **Apply graviton lenses** — Once critical photon demand exceeds raw output, lens every receiver
8. **Stack layers outward** — Add concentric layers at 0.5 AU intervals up to the planet's orbit
9. **Convert to critical photons** — Use ray receivers set to photon mode; ship to a dedicated antimatter processing planet
10. **Celebrate** — You've built a megastructure. Your factory is now effectively power-unlimited

---

> 🛒 [**Buy Dyson Sphere Program on Steam**](https://store.steampowered.com/app/1366540/)
