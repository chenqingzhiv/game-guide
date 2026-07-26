---
title: Dyson Sphere Program Resources Database — All Raw and Refined Resources with Mining Rates and Production Chains
description: Complete reference for every raw and refined resource in Dyson Sphere Program, including mining rates, smelting ratios, and full production chains.
date: 2026-06-26
---

# Dyson Sphere Program Resources Database

Welcome to the definitive resource database for Dyson Sphere Program. This guide covers every raw material, refined product, and intermediate component in the game, along with their mining rates, smelting ratios, and production chain requirements. Whether you're planning your first factory or optimizing a late-game sphere, this reference will help you calculate throughput and balance your production lines.

## Raw Resources (Mined Directly)

Raw resources are extracted from planetary veins using Mining Machines or Advanced Mining Machines. Each vein has a base mining rate that can be increased by upgrading the Mining Speed technology in the Upgrade tree.

| Resource | Vein Type | Base Mining Rate (per second) | Stack Size | Notes |
|----------|-----------|-------------------------------|------------|-------|
| Iron Ore | Iron Vein | 0.5 | 100 | Most common metal |
| Copper Ore | Copper Vein | 0.5 | 100 | Used for circuits and cables |
| Stone | Stone Vein | 0.5 | 100 | Also found on barren planets |
| Coal | Coal Vein | 0.5 | 100 | Early fuel and graphite source |
| Crude Oil | Oil Seam | 3.0 (per oil extractor) | 100 | Requires Oil Extractor, not miner |
| Titanium Ore | Titanium Vein | 0.5 | 100 | Found on other planets |
| Silicon Ore | Silicon Vein | 0.5 | 100 | Found on other planets |
| Water | Water Seam | 3.0 (per water pump) | 100 | Requires Water Pump |
| Fire Ice | Fire Ice Vein | 0.5 | 100 | Gas giant resource |
| Fractal Silicon | Fractal Silicon Vein | 0.5 | 100 | Rare, high-purity silicon |
| Kimberlite Ore | Kimberlite Vein | 0.5 | 100 | Source of diamonds |
| Spiniform Stalagmite | Spiniform Stalagmite Vein | 0.5 | 100 | Organic crystal source |
| Optical Grating Crystal | Optical Grating Crystal Vein | 0.5 | 100 | Late-game optical component |
| Unipolar Magnet | Unipolar Magnet Vein | 0.5 | 100 | Extremely rare, used for particle containers |

**Mining Rate Calculation:**  
`Actual Mining Rate = Base Rate × (1 + Mining Speed Level × 0.1) × Vein Utilization Multiplier`

For example, at Mining Speed Level 10, an Iron Ore miner produces:  
`0.5 × (1 + 10 × 0.1) = 0.5 × 2.0 = 1.0 ore/second`

## Refined Resources (Smelting & Processing)

These are produced by smelting raw ores in Smelters, Arc Smelters, or Plane Smelters. The ratios are critical for balancing production.

| Input | Output | Quantity | Time (seconds) | Machine | Output per Second |
|-------|--------|----------|----------------|---------|-------------------|
| Iron Ore x1 | Iron Ingot x1 | 1 | 1 | Smelter | 1.0 |
| Copper Ore x1 | Copper Ingot x1 | 1 | 1 | Smelter | 1.0 |
| Stone x2 | Stone Brick x1 | 1 | 1 | Smelter | 1.0 |
| Coal x2 | Energetic Graphite x1 | 1 | 2 | Smelter | 0.5 |
| Titanium Ore x2 | Titanium Ingot x1 | 1 | 2 | Smelter | 0.5 |
| Silicon Ore x2 | Silicon Ingot x1 | 1 | 2 | Smelter | 0.5 |
| Crude Oil x2 | Refined Oil x1 + Hydrogen x1 | 2 | 4 | Oil Refinery | 0.5 oil, 0.5 hydrogen |
| Fire Ice x2 | Energetic Graphite x1 + Hydrogen x1 | 2 | 3 | Smelter | 0.33 graphite, 0.33 hydrogen |
| Kimberlite Ore x1 | Diamond x1 | 1 | 1 | Smelter | 1.0 |
| Spiniform Stalagmite x1 | Organic Crystal x1 | 1 | 2 | Smelter | 0.5 |
| Optical Grating Crystal x1 | Prism x1 | 1 | 2 | Smelter | 0.5 |
| Unipolar Magnet x1 | Magnet x1 | 1 | 1.5 | Smelter | 0.67 |

**Key Ratio Example:**  
To produce 1 Energetic Graphite per second, you need 2 Coal per second, which requires 4 Coal Miners (at base rate) or 2 Miners with Mining Speed Level 10.

## Intermediate Components (Assembler Production)

These are crafted in Assemblers, Matrix Labs, or specialized buildings. They form the building blocks of all advanced items.

| Component | Recipe | Craft Time (s) | Output per Second | Used In |
|-----------|--------|----------------|-------------------|---------|
| Magnet | Iron Ingot x1 | 1 | 1.0 | Motors, Electromagnets |
| Gear | Iron Ingot x1 | 1 | 1.0 | Conveyors, Sorters |
| Circuit Board | Copper Ingot x2 | 1 | 1.0 | Processors, Proliferators |
| Processor | Circuit Board x2 + Silicon Ingot x2 | 3 | 0.33 | Advanced processors, Drones |
| Motor | Iron Ingot x2 + Gear x1 + Magnet x1 | 2 | 0.5 | Conveyor Mk.II, Turbines |
| Electromagnet | Magnet x2 + Copper Ingot x1 | 1 | 1.0 | Wireless power, Drone stations |
| Super-Magnetic Ring | Electromagnet x2 + Magnet x2 | 3 | 0.33 | Particle colliders, Warpers |
| Particle Container | Unipolar Magnet x2 + Copper Ingot x2 | 4 | 0.25 | Graviton lenses, Strange matter |
| Graviton Lens | Prism x2 + Processor x2 | 6 | 0.17 | Ray receivers, Research |
| Strange Matter | Particle Container x2 + Iron Ingot x2 | 8 | 0.125 | Warpers, Artificial suns |

## Production Chains (Full Recipes)

Here are the complete production chains for key end-game items, from raw ore to finished product.

### Energetic Graphite (from Coal)
```
Coal Vein → Coal (Miner) → Smelter (x2 Coal → x1 Graphite, 2s)
```
**Throughput:** 1 Graphite/s requires 4 Coal miners (base) or 2 miners with Mining Speed 10.

### Titanium Alloy (for late-game structures)
```
Titanium Ore → Titanium Ingot (Smelter, 2s, 2:1)
Steel (from Iron Ore chain) → Steel Ingot (Smelter, 3s, 3 Iron Ore:1 Steel)
Titanium Ingot x4 + Steel x4 → Titanium Alloy x4 (Assembler, 6s)
```
**Throughput:** 4 Titanium Alloy every 6 seconds = 0.67/s, requiring 2.67 Titanium Ore/s and 2.67 Iron Ore/s.

### Quantum Chip (end-game research)
```
Silicon Ore → Silicon Ingot (Smelter, 2s, 2:1)
Copper Ore → Copper Ingot (Smelter, 1s, 1:1)
Circuit Board (Copper Ingot x2, 1s)
Processor (Circuit Board x2 + Silicon Ingot x2, 3s)
Quantum Chip = Processor x2 + Fractal Silicon x2 (Assembler, 6s)
```
**Throughput:** 1 Quantum Chip every 6 seconds = 0.17/s, requiring 4 Processors/s (which themselves require 8 Circuit Boards/s and 8 Silicon Ingots/s).

## Gas Giant & Rare Resources

Gas giants provide infinite resources via Orbital Collectors. These are critical for late-game hydrogen and deuterium production.

| Gas Giant Type | Resources Collected | Collection Rate (per second) |
|----------------|---------------------|------------------------------|
| Hydrogen Giant | Hydrogen | 0.5 - 1.5 |
| Deuterium Giant | Deuterium | 0.3 - 1.0 |
| Fire Ice Giant | Fire Ice | 0.2 - 0.8 |
| Mixed Giant | Hydrogen + Deuterium | Varies |

**Rare Resource Veins** (found only on specific planet types):
- **Fractal Silicon:** Only on Silicon planets with high wind.
- **Spiniform Stalagmite:** Organic crystal planets.
- **Optical Grating Crystal:** Barren desert planets.
- **Unipolar Magnet:** Neutron star or black hole systems.

## Proliferator Effects

Proliferators can boost production at the cost of extra materials. The three tiers are:

| Proliferator | Effect on Production | Extra Input Required |
|--------------|----------------------|----------------------|
| Mk.I (Blue) | +12.5% output | +20% input |
| Mk.II (Green) | +25% output | +40% input |
| Mk.III (Gold) | +37.5% output | +60% input |

**When to use:** Proliferators are most efficient on high-value recipes like Quantum Chips or Strange Matter, where the extra input cost is offset by the output boost.

## Quick Tips

1. **Always overbuild miners.** Vein Utilization research reduces vein depletion, but early game you need more miners than you think. A single Iron vein can support 2-3 smelters at base mining speed.

2. **Balance your oil refineries.** Crude Oil refining produces both Refined Oil and Hydrogen. If you only need oil, store or burn the excess hydrogen. If you need hydrogen, consider building a dedicated hydrogen farm from gas giants.

3. **Use gas giants for hydrogen.** Orbital Collectors on hydrogen giants provide infinite hydrogen without depleting veins. This is essential for late-game deuterium production.

4. **Rare resources are finite.** Unipolar Magnets and Fractal Silicon veins are limited. Plan your factory to minimize waste of these materials. Use Proliferator Mk.III on recipes involving them to maximize output.

5. **Smelting upgrades matter.** The Smelting Speed technology in the Upgrade tree doubles your smelter throughput at level 10. Prioritize this before building large smelting arrays.

6. **Always check planet types.** Each planet has a resource multiplier. A planet with "100% Iron" will produce twice as much Iron Ore per vein as a planet with "50% Iron". Use the star map to find high-yield planets.

7. **Automate early.** Hand-crafting is slow. Set up automated production of Belts, Sorters, and Assemblers as soon as possible. A single Assembler making Belts can supply your entire early-game factory.

8. **Storage is a buffer, not a solution.** Don't rely on storage boxes to fix imbalances. Use splitter arrays and overflow belts to manage excess resources. For example, if your hydrogen backs up, burn it in Thermal Power Plants.

9. **Matrix Labs for research.** Each cube type (Blue, Red, Yellow, Purple, Green) requires its own production chain. Plan your research labs in a dedicated area with separate input belts for each cube color.

10. **Use the calculator.** For complex production chains, use an online Dyson Sphere Program calculator or the in-game production statistics panel (P key) to check your throughput. This will save hours of debugging.
> 🛒 [**Buy Dyson Sphere Program on Steam**](https://store.steampowered.com/app/1366540/) — Build the ultimate factory across the galaxy!
> *This is an affiliate link. If you purchase through it, we may earn a small commission at no extra cost to you.*
