---
title: "Shapez 2 Optimization Guide"
description: "Throughput and compactness."
date: 2026-07-06
tags: [Shapez 2, optimization]
---

## Compact Patterns

Stacker Sandwich: Stack belts before merging for double throughput.
Split-Merge: Split input, process parallel, merge back. 4x throughput in 2x space.

## Belt Balancers

4-to-4 balancer: All outputs equal regardless of inputs. Always balance before processing arrays.

Belt speed cap: 60 shapes/s. Balance upstream to hit this.

## Bus Architecture

Raw Processing > Shape Highway (8 belts) > Production Modules > Final Assembly > Hub.

Each module: split shape type, process, paint, merge back. 10x20 tiles compact.