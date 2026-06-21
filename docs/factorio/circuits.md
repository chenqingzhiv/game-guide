---
title: Circuit Networks & Automation Guide
description: Master Factorio's circuit network — combinators, SR latches, clocks, belt balancing, train control, cracking control, and power switches with working examples.
---

# 🔌 Circuit Networks & Automation Guide

> *"The factory must grow — intelligently."*

Factorio's **Circuit Network** is the nervous system of your factory. It lets you wire up combinators, belts, inserters, train signals, and power switches to build everything from a simple belt balancer to a fully automated megabase.

This guide covers the fundamentals and advanced builds with **working examples** you can blueprint right away.

---

## 📦 Combinator Types

There are three combinator types — every circuit build starts with these.

### Constant Combinator

The **Constant Combinator** provides a fixed signal on the circuit network. Use it as a reference value or setpoint.

-   Outputs the signals you configure in its GUI
-   Available from red/green circuit research (red science)
-   Connect its output to any circuit wire

**Example — Setpoint for cracking control:**

Set a Constant Combinator to output `Petroleum Gas = 100` — this becomes the threshold your cracking plant compares against.

### Arithmetic Combinator

The **Arithmetic Combinator** performs math on one or two input signals and outputs a result.

| Operation | Input 1 | Input 2 | Output |
|-----------|---------|---------|--------|
| `A + B` | Signal | Number/Signal | Result |
| `A - B` | Signal | Number/Signal | Result |
| `A * B` | Signal | Number/Signal | Result |
| `A / B` | Signal | Number/Signal | Result (floor) |
| `A % B` | Signal | Number/Signal | Result (modulo) |
| `A ^ B` | Signal | Number/Signal | Result (exponent) |
| `A << B` | Signal | Number/Signal | Bitshift left |
| `A >> B` | Signal | Number/Signal | Bitshift right |
| `AND`/`OR`/`XOR` | Signal | Signal | Bitwise logic |
| `NOT` | Signal | — | Bitwise NOT |
| Each → `+ 0` | Any signal | 0 | Signal pass-through (useful for wire merging!) |

> 💡 **Pro tip:** `Each + 0` is the most common Arithmetic Combinator trick — it copies every input signal to the output on a different color wire, acting as a wire bridge.

### Decider Combinator

The **Decider Combinator** compares signals and outputs a specified signal (or the input signal) when the condition is met.

| Condition | Example | Behavior |
|-----------|---------|----------|
| `A > B` | Iron Plate `> 100` | Outputs when Iron Plate exceeds 100 |
| `A = B` | Petroleum `= 0` | Outputs when Petroleum is exactly 0 |
| `A < B` | Iron Ore `< 50` | Outputs when Iron Ore is below 50 |
| `A ≠ B` | Signal `≠ 0` | Outputs when signal is non-zero |
| `A ≥ B` / `A ≤ B` | — | Greater/less than or equal |
| `A > 0` / `A = 0` | — | Common zero-check patterns |

**Output modes:**

-   **Output: `1`** — outputs a single green signal (value 1) when condition is true
-   **Output: `Input count`** — passes the input signal through when condition is true

> 💡 **Pro tip:** Use `Everything` / `Anything` / `Each` as the input signal for multi-signal logic:
> - `Everything > 0` = all signals must be positive
> - `Anything < 0` = at least one signal is negative
> - `Each * 2` = double every signal individually

---

## 🔧 Basic Circuit Builds

### SR Latch (Set-Reset Latch)

The SR Latch is the fundamental memory cell of the circuit network. It maintains its output state until a *reset* condition overrides it.

**Use case:** Keep a power switch closed until steam storage drops, then open it until steam refills (hysteresis).

```
         ┌──────────────┐
 Set ───▶│              │
         │  Decider A   │─── Output ──▶
 Reset ─▶│  (Memory)    │
         └──────────────┘
              ▲
              │ (feedback loop)
              └── output connected to input
```

**Blueprint recipe:**

1.  **Decider Combinator (Memory):**
    -   Input: Red wire from tank/power switch
    -   Condition: `Signal > 0`
    -   Output: `Input count` (red wire from output back to input)
2.  **Second Decider (Set/Reset):**
    -   Outputs a signal (e.g., `S = 1`) when the "set" condition is met
    -   Outputs a signal (e.g., `R = 1`) when the "reset" condition is met
3.  Wire the set/reset signals into the memory combinator's input.

**Real-world example — Steam battery SR Latch:**

| Condition | Signal | Action |
|-----------|--------|--------|
| Steam tank < 500 | Set = 1 | Enable accumulators |
| Steam tank > 2000 | Reset = 1 | Disable accumulators |

The gap between 500 and 2000 provides **hysteresis** — the system won't rapidly toggle.

### Clock (Timer)

A clock circuit produces a periodic pulse. Essential for timed insertions, belt pacing, and measurement intervals.

**Pulse generator (rapid clock):**

```
  Arithmetic: Signal + 1 → Signal  (output feedback to input)
  Decider:    Signal < 100 → Signal (output to circuit network)
```

- The Arithmetic combinator increments `Signal` every tick
- The Decider passes `Signal` through while it's below 100
- When `Signal` reaches 100, the Decider stops — the Arithmetic resets back to 0
- Cycle repeats → you get a 100-tick period square wave

**Adjustable clock with Constant Combinator:**

```
  Constant:           T = 60  (period)
  Arithmetic:         T * 1 → T  (pass-through, outputs T)
  Decider (Counter):  C = C + (1 every tick)
  Decider (Output):   C < T → C  (pass C through while below T)
```

When `C >= T`, the Counter resets to 0 and the clock fires.

### Counter

Count items as they pass on a belt or enter a chest. Combine with a clock for **throughput measurement**.

**Basic item counter:**

1.  Place a **pulse-mode inserter** — wire it to read hand contents, pulse mode
2.  Connect green wire from inserter to an **Arithmetic Combinator**: `Each + 0 → Each`
3.  Feed the output back to the input (red wire) — this accumulates
4.  Wire a **Constant Combinator**: `R = 1` to a **Decider** that outputs `Everything * 0` when `R > 0` to reset

**Belt throughput (items/minute):**

1.  Counter circuit as above
2.  Connect a clock set to 3600 ticks (60 seconds at 60 UPS)
3.  Decider checks: if clock fires, output the counter value → that's items/minute

---

## 🎛️ Belt Balancing & Priority Splitters

Circuit-controlled belt balancing lets you build **smart splitters** and **priority mergers** without relying on lane-balancer blueprints.

### Priority Input Splitter

Ensure one belt gets filled before overflow goes to a secondary belt.

```
        ┌────────┐
 Input ─▶ Splitter├─── Priority output
        │        ├─── Overflow (circuit-controlled)
        └────────┘
              ▲
              │
         Read belt (red wire)
```

1.  Place a **Splitter** with output priority set to the desired belt
2.  Connect a **red wire** from the priority-output belt (read belt contents) to the splitter's input
3.  Set the splitter to **"Enable/disable"** — condition: `Iron Plate < 8` (or your threshold)
4.  When the priority belt backs up, the splitter enables overflow on the second output

### Balanced Load Balancer

Use circuits to balance multiple belts without building a huge belt balancer.

1.  Place **4 splitters** in a tree (2 → 1, 2 → 1, then combine)
2.  Wire each belt to an **Arithmetic Combinator**: `Each + 0 → Each`
3.  Sum all 4 signals, divide by 4 → that's the average
4.  Compare each individual belt to the average → enable/disable inserters or splitters to match

---

## 🚂 Train Station Control

Circuit-controlled train stations prevent multiple trains from queuing at the same station and let you call trains only when resources are available.

### Single-Train Enable/Disable

Wire the station to a chest or storage tank. The station enables only when there's enough to load (or enough room to unload).

**Loading station example:**

1.  Connect all provider chests to the **train stop** via red wire
2.  Set train stop condition: `Iron Plate > 2000` (enough to fill one train)
3.  Trains with `Wait until: circuit condition > 0` will only path to this stop when it's active

### Multi-Station Priority (Stacker Bypass)

Prevent trains from going to a station that's nearly empty when another station is full.

1.  Each station reads the total items in its chests
2.  Each station outputs `L = 1` (limit) when it has enough items
3.  Wire all stations together on the same circuit network
4.  Each station checks its own chest level against a threshold — `Iron Plate > 2000 → L = 1`
5.  Train limit = 1 on each station — trains only go to stations broadcasting `L = 1`

> 💡 **Pro tip:** Use **Train Limit** (introduced in Factorio 1.1) instead of enable/disable for smoother train pathing. Set train limit to 1 on stations that have enough resources, 0 on empty stations.

### Station Timer (Pulse Generator)

Prevent trains from stacking when a station is just above threshold but quickly draining.

1.  Wire a **Decider Combinator**: `Iron Plate > 2000 → L = 1`
2.  Wire output back through an **Arithmetic Combinator**: `L - 1 → L`
3.  This creates a timer — the station stays open for ~60 ticks after chests drop below threshold

---

## 🛢️ Oil Cracking Control

Oil cracking — converting Heavy → Light → Petroleum — is the most common circuit-controlled process in Factorio. You want to crack only when there's excess of the heavier oil.

### Basic Heavy → Light Cracking

```
                    ┌──────────────┐
 Light Oil ─────────▶              │
 (red wire)         │  Decider     │── Green wire ──▶ Heavy Cracking Pump
 Petroleum ────────▶│  Combinator  │
 (red wire)         │              │
                    └──────────────┘
 Condition: Light Oil > Petroleum
 Output:     Light Oil (Input Count)
```

1.  Wire a **red circuit** from the Light Oil storage tank(s) to the Decider Combinator input
2.  Wire a **red circuit** from the Petroleum Gas tank(s) to the same Decider Combinator input
3.  Set Decider: `Light Oil > Petroleum Gas → Output: Light Oil (Input Count)`
4.  Wire the Decider output (**green wire**) to the pump feeding the Heavy → Light cracking chemical plants
5.  The pump only turns on when there's more Light Oil than Petroleum — i.e., you're backed up on Light

### Full Cracking Priority System

Control all three cracking stages with priority: Light cracking runs first, Heavy cracking only when Light is also surplus.

**Setup:**

| Cracking Stage | Condition | Pump Signal |
|----------------|-----------|-------------|
| Light → Petro | `Light Oil > Petroleum` | Enable pump |
| Heavy → Light | `Heavy Oil > Light Oil` AND `Light Oil > Petroleum` | Enable pump |
| Heavy → Petro (if available) | `Heavy Oil > 0` AND `Petroleum < Light Oil` | Enable pump |

**Why this works:**

-   If Petroleum is low, Light cracking runs first (Light → Petro)
-   If Light is also building up, Heavy cracking opens (Heavy → Light)
-   If Petroleum is satisfied AND Light is still backed up, Heavy → Petro kicks in

**Blueprint wiring:**

1.  Wire **all tanks** to a shared red circuit network
2.  Decider #1: `Light > Petro → L = 1` → controls Light → Petro pump
3.  Decider #2: `Heavy > Light → H = 1` AND `L = 1` → controls Heavy → Light pump
4.  Decider #3: `Heavy > 0` AND `Petro < Light → P = 1` → controls any Heavy → Petro pump

---

## ⚡ Power Switch Control

Use circuit-controlled power switches to manage steam batteries, solar-accumulator priority, and emergency backup power.

### Steam Battery (Accumulator Priority)

Prevent steam engines from running when accumulators have charge.

```
                    ┌──────────────┐
 Accumulator ───────▶              │
 Charge (A)         │  Arithmetic  │── A * 100 ──▶  Decider ──▶ Power Switch
                    │              │
                    └──────────────┘
                    ┌──────────────┐
 Accumulator ───────▶              │
 Max (J)            │  Combinator  │
                    └──────────────┘
```

1.  Connect an **accumulator** to an **Arithmetic Combinator**: `A * 100 ÷ J → %`
2.  Feed to a **Decider Combinator**: `% < 20 → Enable Power Switch`
3.  Wire the Decider output to a **Power Switch** (connect to switch via green wire)
4.  Set the Power Switch to: `Enable: Signal > 0`

Now steam only kicks in when accumulators drop below 20%.

### Solar-Only Power Switch

Cut off the main grid from accumulator-fed substations during the day.

1.  Read an **Accumulator** charge (signal `A`)
2.  Wire to **Decider**: `A > 95 → S = 1` (daytime, accumulators nearly full)
3.  Wire to **Power Switch**: enable when `S = 1`
4.  Second Power Switch (night): `A < 5 → S = 1` (switch to accumulators)

### Emergency Backup

Trigger backup steam when the main grid power falls below a threshold.

1.  Place a **power pole** on the main grid
2.  Wire it to an **Arithmetic Combinator**: `Each * 1 → P` (reads satisfaction/availability)
3.  **Decider**: `P < 500000 → E = 1` (below 5 MW → activate)
4.  Wire to a **Power Switch** controlling backup steam engines

---

## 🧩 Advanced Patterns

### Memory Cell

Store a value indefinitely:

```
 Decider Combinator:  Everything > 0 → Everything (Input Count)
 Wire output (red) back to input (red)
```

- Set signal `R = 1` to clear the memory
- New values merge with the stored value

### Pulse Extender

Convert a 1-tick pulse into a sustained signal:

```
 Decider:  Signal > 0 → Signal (Input Count)
 Wire output back through Arithmetic: Signal - 1 → Signal
```

The signal persists for `N` ticks where `N` is the initial value, then decays.

### S-R Latch with Hysteresis (Compact)

For when you need threshold-based control with deadband:

1.  Decider #1: `A > 100 → S = 1`
2.  Decider #2: `A < 50 → R = 1`
3.  Memory Decider #3: `S > 0 → S = 1` with feedback, override by `R > 0`

---

## 🏗️ Blueprint Strings

You can share and import any of the builds above as blueprint strings. Visit **[factorioprints.com](https://factorioprints.com)** or paste strings directly into your game.

> ⚠️ Blueprint strings are long — use the in-game import (`Ctrl+V` / `Cmd+V` in the blueprint library) or a pastebin.

---

## 🎯 Quick Reference

| Component | Function | Key Setting |
|-----------|----------|-------------|
| **Constant Combinator** | Reference value | Set desired signal/number in GUI |
| **Arithmetic Combinator** | Math / conversion | `Each + 0` for wire bridging |
| **Decider Combinator** | Compare & output | `Everything` / `Anything` for multi-signal |
| **Power Switch** | Grid segment control | Enable condition via circuit |
| **Train Stop** | Station enable/disable | Circuit condition or train limit |
| **Pump** | Fluid flow control | Enable condition via circuit |
| **Inserter** | Item flow control | Circuit condition + read/pulse mode |

---

## 📚 Further Reading

-   [Official Factorio Wiki — Circuit Network](https://wiki.factorio.com/Circuit_network)
-   [Official Factorio Wiki — Combinator Tutorial](https://wiki.factorio.com/Tutorial:Combinator_tutorial)
-   [Reddit r/factorio — Circuit Network Showcase](https://www.reddit.com/r/factorio/)
-   [Factorio Prints — Community Blueprints](https://factorioprints.com)

---

> 🛒 **Support the developers — [Buy Factorio on Steam](https://store.steampowered.com/app/427520/?utm_source=game-guide.club&utm_medium=referral&utm_campaign=circuits-guide)**
