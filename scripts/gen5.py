#!/usr/bin/env python3
"""Last 2 pages to reach 160"""

import os
DOCS = "/home/hermes/game-guide/docs"

def w(path, content):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)

w("games/survival-tiers.md", """---
title: "Best Survival Games Ranked - 2026 Tier List"
description: "Complete survival game tier list ranking the best survival, crafting, and factory games of 2026."
date: 2026-07-06
tags: [survival, tier list, games, ranking]
---

## Survival Game Tier List 2026

A comprehensive ranking of the best survival and crafting games based on player count, community activity, content depth, and replayability.

## S-Tier (Must Play)

**Minecraft** — The best-selling game of all time. Infinite possibilities, modding, redstone automation.
**Valheim** — Viking survival with incredible building physics and atmospheric exploration.

## A-Tier (Excellent)

**Satisfactory** — First-person factory automation perfection. Beautiful world, deep logistics.
**Factorio** — The gold standard of factory games. Infinite scalability.
**Don't Starve Together** — Unique art style, deep seasonal mechanics, co-op play.
**Stardew Valley** — The ultimate farming life sim. Unmatched charm and depth.

## B-Tier (Great)

**Rust** — The definitive PvP survival experience. High skill ceiling.
**Subnautica** — Best underwater exploration game ever made.
**7 Days to Die** — Best zombie survival crafting with blood moon hordes.
**Enshrouded** — Beautiful voxel building with action combat.
**V Rising** — Vampire survival with stylish combat and castle building.
**Grounded** — Unique backyard scale survival with story focus.

## C-Tier (Good)

**Palworld** — Pokemon with guns and factory automation. Novelty factor.
**Core Keeper** — Engaging mining loop but limited endgame.
**Raft** — Ocean survival is unique but content is limited.
**Sons of the Forest** — Great horror survival but shorter than expected.
**Timberborn** — Beavers! Unique water mechanics but small scope.
**Dyson Sphere Program** — Satisfying factory building but lacks combat depth.
**Shapez 2** — Minimalist factory puzzler. Pure optimization.
""")

w("guides/gaming-setup.md", """---
title: "Best Gaming Setup for Survival Games - Budget to Premium"
description: "Complete gaming setup guide for survival and factory games. From budget builds to premium rigs for Valheim, Satisfactory, Rust and more."
date: 2026-07-06
tags: [gaming, gear, setup, hardware]
---

## Gaming Setup Guide for Survival Games

Survival and factory games have different hardware needs than competitive shooters. Here's what matters most.

## Budget Build ($600-800)

**CPU:** AMD Ryzen 5 5600
**GPU:** RTX 3060 12GB or RX 6700 XT
**RAM:** 16GB DDR4-3200
**Storage:** 1TB NVMe SSD

**Good for:** Stardew Valley, Timberborn, Shapez 2, DST, Core Keeper

## Mid-Range Build ($1200-1500)

**CPU:** AMD Ryzen 7 7800X3D
**GPU:** RTX 4070 Super or RX 7800 XT
**RAM:** 32GB DDR5-6000
**Storage:** 2TB NVMe SSD

**Good for:** Valheim, Satisfactory, Factorio, Enshrouded, V Rising, Grounded

## Premium Build ($2500+)

**CPU:** AMD Ryzen 7 9800X3D
**GPU:** RTX 5090 or RX 9070 XT
**RAM:** 64GB DDR5-6000
**Storage:** 4TB NVMe SSD

**Good for:** Rust (high pop), 7 Days to Die (max settings), Modded Minecraft, Subnautica

## Factory Game Optimization

Factory games (Satisfactory, Factorio, DSP) are CPU-bound. Prioritize:
- High single-core performance (X3D CPUs are best)
- LOTS of RAM (32GB+ for mega-factories)
- Fast storage (NVMe for 10k+ object saves)

## Survival Game Optimization

Survival games (Rust, 7 Days, Valheim) need:
- Strong GPU for draw distances
- 32GB RAM for 100+ player servers
- Fast storage for texture streaming
""")

import subprocess
result = subprocess.run(["find", DOCS, "-type", "f", "-name", "*.md"], capture_output=True, text=True)
count = len([f for f in result.stdout.strip().split("\n") if f])
print(f"Total .md files: {count}")
