---
title: "Shapez 2 Color Mixing & Dye Reference"
description: "Complete reference for all 16 dye colors in Shapez 2 — mixing recipes, color IDs, and applications for painting shapes."
---

# 🎨 Shapez 2 Color Mixing & Dye Reference

Color mixing is a core mechanic in Shapez 2. While the basic shapes are extracted from crystals, **coloring** those shapes is what allows you to complete the more complex hub milestones. Every dye color can be crafted from the 4 primary dyes (white, red, green, blue) using mixers.

> **Data source:** Shapez 2 in-game manual v0.9.0 — Last verified: July 2026

---

## Primary Dyes (4 Base Colors)

These 4 dyes are produced directly from raw crystal deposits and serve as the foundation for all other colors.

| Color | Crystal Source | Production | Used In |
|:------|:---------------|:-----------|:--------|
| ⬜ **White** | White Crystal | Crystal Processor → White Dye | All pastel/mixed colors |
| 🔴 **Red** | Red Crystal | Crystal Processor → Red Dye | Orange, Purple, Pink |
| 🟢 **Green** | Green Crystal | Crystal Processor → Green Dye | Cyan, Yellow-Green |
| 🔵 **Blue** | Blue Crystal | Crystal Processor → Blue Dye | Cyan, Purple |

---

## Full Dye Color List (16 Colors)

All 16 colors available in Shapez 2, organized by how they're obtained. Mixing uses a **Mixer** building that combines two input dyes at a 1:1 ratio.

### Primary (4) — Direct from crystals

| Color | Name | RGB | How to Get |
|:------|:-----|:---|:-----------|
| ⬜ | **White** | `#FFFFFF` | White crystal → Processor |
| 🔴 | **Red** | `#FF0000` | Red crystal → Processor |
| 🟢 | **Green** | `#00FF00` | Green crystal → Processor |
| 🔵 | **Blue** | `#0000FF` | Blue crystal → Processor |

### Secondary (4) — Mix two primaries

| Color | Name | RGB | Mixing Recipe |
|:------|:-----|:---|:--------------|
| 🟡 | **Yellow** | `#FFFF00` | Red + Green |
| 🟣 | **Purple** | `#FF00FF` | Red + Blue |
| 🔷 | **Cyan** | `#00FFFF` | Green + Blue |
| 🟠 | **Orange** | `#FF8000` | Red + Yellow (or Red+Green+Red) |

### Tertiary (4) — Mix a primary + secondary

| Color | Name | RGB | Mixing Recipe |
|:------|:-----|:---|:--------------|
| 🌸 | **Pink** | `#FF8080` | Red + White |
| 🌿 | **Lime** | `#80FF00` | Green + Yellow |
| 🗻 | **Teal** | `#008080` | Green + Blue (Cyan) + more Blue |
| 🍫 | **Brown** | `#804000` | Red + Green + less Red |

### Special (4) — Three-color mixes or complex

| Color | Name | RGB | Mixing Recipe |
|:------|:-----|:---|:--------------|
| ⚪ | **Light Gray** | `#C0C0C0` | White + Black (if available) or White × 2 |
| 🌤️ | **Sky Blue** | `#8080FF` | Blue + White |
| 🌸 | **Rose** | `#FF4080` | Red + Pink |
| 🌑 | **Black** | `#000000` | Red + Green + Blue (all three) |

> **Note:** Black is the hardest color to produce, requiring all three primary dyes (Red + Green + Blue). Plan your production lines accordingly.

---

## Color Production Efficiency Tips

### Optimal Production Chains

For high-volume color production, structure your dye factories as follows:

```
Crystal Mines → Processors → Sorters → Mixers → Painters
```

**Most efficient approach:**

| Target Color | Chain | Buildings Required |
|:-------------|:------|:-------------------|
| **Yellow** (high demand) | Red Crystal + Green Crystal → Mixer | 2 Processors + 1 Mixer |
| **Cyan** (high demand) | Green Crystal + Blue Crystal → Mixer | 2 Processors + 1 Mixer |
| **Purple** | Red Crystal + Blue Crystal → Mixer | 2 Processors + 1 Mixer |
| **Orange** | Red Crystal + Yellow Dye → Mixer | 2 Processors + 1 Mixer + Yellow Mixer |
| **Pink** | Red Crystal + White Crystal → Mixer | 2 Processors + 1 Mixer |
| **Black** | Red + Green + Blue → Mixer × 2 | 3 Processors + 2 Mixers |

### Color Demand by Milestone

Certain colors appear more frequently in hub milestones:

| Frequency | Colors |
|:----------|:-------|
| 🟢 **Very Common** | Red, Green, Blue, Yellow, Cyan |
| 🟡 **Common** | White, Purple, Orange |
| 🟠 **Occasional** | Pink, Lime, Teal |
| 🔴 **Rare** | Black, Brown, Rose, Sky Blue, Light Gray |

> **Pro tip:** Build a permanent Yellow and Cyan production line early — they are required in nearly every milestone tier.

---

## Color Wheel Reference

For quick reference, here's the Shapez 2 color wheel relationships:

```
        Red
       /   \
    Purple  Orange
      |       |
    Blue --- Yellow
       \   /
       Cyan
```

**Mixing shortcuts:**
- Red + Yellow → **Orange**
- Red + White → **Pink**
- Blue + White → **Sky Blue**
- Blue + Yellow (Cyan+Yell) → **Green** variants
- Red + Blue → **Purple**
- Green + Blue → **Cyan**
- Red + Green → **Yellow**
- All three → **Black**

---

## Common Mistakes to Avoid

1. **❌ Processing the wrong crystal** — Check your miner's output before routing to the processor
2. **❌ Forgetting to balance mixer inputs** — If one input runs dry, the mixer stalls. Use belt balancers
3. **❌ Building too few mixers** — One mixer per color is rarely enough for T5+ milestones
4. **❌ Not stockpiling basics** — Always buffer Red, Green, Blue, and White dye before expanding
5. **❌ Underestimating Black production** — Black needs 3 input types, making it the production bottleneck of many advanced milestones

---

## Dye Layout Blueprint

Here's a compact dye factory layout (4×4 grid):

```
[Miner W] → [Proc W] → [Mixer W+R→Pink]
[Miner R] → [Proc R] → [Mixer R+G→Yell] → [Mixer R+Y→Ora]
[Miner G] → [Proc G] → [Mixer G+B→Cyan] → [Mixer R+B→Purp]
[Miner B] → [Proc B] →                    [Mixer R+G+B→Black]
```

This produces **8 unique colors** from just 4 crystal inputs.

---

> 🛒 [**Buy Shapez 2 on Steam**](https://store.steampowered.com/app/2162800/) — Support the developer!
>
> *Affiliate link — we earn a small commission at no extra cost to you.*
