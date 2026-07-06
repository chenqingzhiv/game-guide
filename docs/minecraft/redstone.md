---
title: "Minecraft Redstone Guide"
description: "Automation basics."
date: 2026-07-06
tags: [Minecraft, redstone]
---

## Basics

Redstone power: 15 blocks from source (extend with repeaters).
Tick: 0.1 seconds.

Key components: Repeater (delay 1-4 ticks), Comparator (measure/compare), Observer (detects changes), Piston (moves blocks).

## Essential Builds

Item Sorter: Hopper > Comparator > Repeater > Piston. Sorts 1 item type per chest.

Auto Melon Farm: Observer + Piston + Hopper minecart. ~2 stacks/hour.

XP Farm: Spawner + Water elevator + Killing chamber at Y=245.

## Logic Gates

NOT: Torch on block.
AND: Two repeaters into block.
OR: Two redstone lines merge.
T-Flip Flop: Piston pushing block into torch. Converts button to toggle.

RS Latch: Two torches cross-wired.