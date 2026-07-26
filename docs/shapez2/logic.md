---
title: "Shapez 2 Logic Guide — Pins & Wiring"
description: "Master Shapez 2 logic. Learn pin placement, wire connections, conditional processing, and advanced automation."
---

# ⚡ Shapez 2 Logic Guide — Pins & Wiring

---

## 📍 What Are Pins?

Pins are small connectors attached to the sides of belts, machines, and other shapez 2 buildings. Each pin broadcasts a **binary signal** (0 or 1) based on some property of the item passing through or the state of the building. They are the foundation of all automation logic in the game.

You can place pins on any belt segment by clicking the small square node on the belt's side. Once placed, a pin reader can be configured to detect one of several conditions:

- **Belt moving** — outputs 1 when the belt is actively moving items, 0 when it's stopped or empty
- **Shape present** — outputs 1 when a shape passes the pin location
- **Color detection** — outputs 1 when the shape matches a selected color
- **Quadrant detection** — outputs 1 when a specific quadrant of the shape is present
- **Item type** — outputs 1 when the item matches a chosen shape ID

Pins give you eyes on your factory. Without them, belts run blind. With them, you can build decision-making into every junction.

---

## 🔌 Basic Wiring Components

Wiring connects pins to logic gates and filters. Here's a reference table of the core components:

| Component | Function |
|:----------|:---------|
| **Pin Reader** | Reads a property from a belt or machine and outputs a 0 or 1 signal |
| **Wire** | Connects a pin output to a logic gate input or filter |
| **AND Gate** | Outputs 1 only when **both** inputs are 1 |
| **OR Gate** | Outputs 1 when **any** input is 1 |
| **NOT Gate** | Inverts the signal (0→1, 1→0) |
| **Comparator** | Compares two values — outputs 1 when the comparison is true |
| **Delay** | Delays a signal by a configurable number of in-game ticks |
| **Filter** | Lets shapes pass through only when the input condition is met |

Wires can be placed by dragging from an output pin to an input pin. A green wire indicates a live connection; a red or missing wire means the signal isn't reaching its destination. Wires can cross each other without interference — they only connect at explicit pin junctions.

---

## 🔄 All 6 Comparator Comparison Modes

The **comparator** is the most powerful logic component in Shapez 2. It has two inputs (A and B) and outputs a binary 1 or 0 based on the comparison mode you select. Here are all six modes:

### 1. Equal (A = B)
Outputs 1 when the value of input A exactly equals input B. Use this to match specific color values, shape IDs, or signal strengths. Essential for exact-match sorting.

### 2. Not Equal (A ≠ B)
Outputs 1 when A and B are different. This is the inverse of Equal. Useful for detecting mismatches — for example, flagging shapes that don't belong on a particular belt.

### 3. Greater Than (A > B)
Outputs 1 when the number on input A is strictly larger than input B. Critical for **overflow detection** — if a belt's item count exceeds a threshold, trigger a diversion.

### 4. Less Than (A < B)
Outputs 1 when A is strictly smaller than B. The inverse of Greater Than. Combine with a timer to detect when a machine has been idle for too long.

### 5. Greater Than or Equal (A ≥ B)
Outputs 1 when A is larger than or equal to B. This is the most commonly used threshold check — "is the item count at least X?" is a natural question for inventory management.

### 6. Less Than or Equal (A ≤ B)
Outputs 1 when A is smaller than or equal to B. Useful for "is this belt nearly empty?" scenarios — trigger a refill request when items drop below a threshold.

Each comparator has a built-in display showing the current values of A and B. You can set the B value manually as a constant, or wire it from another pin. When using constants, the comparator acts like a programmable threshold detector.

---

## 🌐 Wire Network Topologies

Wires in Shapez 2 form a **bus topology** — all wires sharing the same color are electrically connected. This means every pin on the same wire color reads the same signal. Understanding topology helps you design clean, scalable factories.

### Point-to-Point
The simplest topology: one output pin directly wired to one input. Use for single-condition filters and simple on/off controls. No branching, no confusion.

### Shared Bus
Multiple pins share a single wire color. All readers on that wire see the same signal. This is efficient when several machines need the same control signal — for example, a single "halt production" pin wired to every machine in a bank.

### Star Network
A central comparator or gate feeds signals to multiple downstream machines. The central node acts as a decision point. Use this when one condition determines the state of many filters.

### Cascaded Chain
Comparators feed into each other sequentially. Each stage refines the signal. A common pattern: detect color → detect quadrant → route to specific assembler. Cascades allow complex multi-condition logic without needing wide fan-in.

### Daisy Chain
Pins pass a shape's properties from belt to belt, with each segment checking a different condition. The shape moves down the chain, and at each step a filter either passes it through or diverts it. Ideal for multi-stage sorting.

**Important rule**: Wires of different colors are electrically isolated. Use color to create separate signal domains — control signals on one color, data signals on another. This prevents feedback loops and keeps your logic readable.

---

## 🧠 Practical Logic Circuits

### Color Sorter

A color sorter detects the color of an incoming shape and routes it to the correct output belt.

**Setup**:
1. Place a pin reader on the main input belt and configure it to detect a specific color (e.g., red).
2. Place a filter directly after the pin reader on the same belt.
3. Wire the pin reader's output to the filter's control input.
4. When a red shape passes the pin, the signal goes high (1), and the filter opens.
5. Red shapes pass through; all other shapes are rejected to a secondary belt.

For multi-color sorting, chain several of these in sequence. The first filter catches red, the second catches blue on the reject line, the third catches green, and so on. Each stage removes one color from the stream.

### Quad-Filter

The quad-filter checks **which quadrant** of a shape is present. Shapes in Shapez 2 have four quadrants, each of which can have its own color and shape piece. A quad-filter lets you route based on quadrant composition.

**Setup**:
1. On a belt carrying mixed quadrant shapes, place four pin readers in sequence.
2. Configure each reader to detect a different quadrant (Q1, Q2, Q3, Q4).
3. Each reader feeds a separate filter on a parallel belt.
4. When a shape passes, each reader checks its assigned quadrant. Only the filter matching a present quadrant opens.

This is the basis for **puzzle-piece routing** — breaking a complex shape into its component quadrants and sending each to the right assembler.

For a **fine-grained quad-filter**, use comparators instead of direct pin readers. Set each comparator to A = B, where A is the pin reader value and B is the specific quadrant value you want to match. This gives you exact quadrant matching with no false positives.

### Memory Cells (1-Bit SR Latch)

A memory cell stores a single bit of information indefinitely — even after the input signal stops. In Shapez 2, you build one using a feedback loop with two AND gates and one OR gate.

**Setup**:
1. Connect an OR gate output to one input of an AND gate.
2. Route the AND gate's output back to the OR gate's second input (feedback loop).
3. The other AND gate input is your "set" signal.
4. Add a second AND gate with a "reset" signal and wire it to break the feedback.

When the **set** signal pulses high, the output goes high and stays high forever — even after the set signal drops. When the **reset** signal pulses high, the output drops and stays low.

**Practical use**: Store the state of a machine. If a machine jams, set the bit. The memory cell keeps the jam flag high until you manually reset it (or build an auto-reset timer). Memory cells are also used in counters, sequencers, and state machines.

### Item Counter

Combine a pin reader (counting items passing by) with a comparator set to A ≥ B. Connect a constant value B (say, 100) to the comparator. When 100 items have passed, the comparator fires. Wire this to a memory cell to latch the "batch complete" signal, then use it to trigger a machine or sorter.

---

## 📡 Sensors

Sensors are specialized pin configurations that detect factory-wide conditions beyond individual items.

### Belt Jam Sensor
Place a pin on a belt and set it to "belt moving." When a jam occurs upstream, the belt stops, and the pin outputs 0. Wire this to a NOT gate so you get a 1 signal when the belt is stopped — that's your jam alarm.

### Machine Idle Sensor
Place a pin reader on the output belt of a machine. If the machine is producing, items flow and the belt stays moving. If the machine stops (no input, or full output), the belt stops. Wire this to a comparator (A = 0) to detect idle state, then feed that into a timer delay. If the machine is idle for more than X ticks, trigger a warning or redirect materials.

### Overflow / Full-Belt Sensor
Place a pin on the input belt of a machine. If the belt is moving but items are backing up (the belt is full and stuttering), the belt moves intermittently. Wire the pin to a comparator with A < B (where B is a low threshold) to detect stutter. When the belt is fully saturated and stalled, the pin outputs a steady 0 — trigger a diversion belt to send excess items to storage or a sink.

### Shape Property Sensor
Use a pin reader in "shape property" mode to detect specific combinations of color and quadrant. This is more powerful than simple color or quadrant detection because it checks both simultaneously. Wire multiple readers together through AND gates for compound conditions: "red + quadrant 2 + no quadrant 3" = route to assembler C.

---

## 🔧 Troubleshooting Common Logic Problems

### Signal Not Reaching Destination
Check wire color. Wires of different colors are isolated — if your source pin is blue and your filter input is green, the signal won't cross. Delete and re-place the wire to ensure correct color continuity.

### Filter Not Opening
Filters open only when the control signal is **steady 1**. If your pin reader is pulsing (flickering as items pass), the filter may not stay open long enough for the shape to pass through. Use a delay gate or latch to hold the signal.

### Logic Gate Locks Up
If a gate stays stuck at 1 or 0, check for feedback loops. A wire accidentally connecting output back to input can create an oscillation or latch. Use different wire colors for feedback paths to keep them visually distinct.

### Comparator Shows Wrong Values
Verify that the A and B inputs are wired to the correct sides of the comparator. Swap them if needed. Also check that your constant B value is entered correctly — it's easy to accidentally set 10 instead of 100.

### Belt Backs Up Behind Filter
When a filter rejects items, the rejected lane can back up and jam the entire system. Always route rejected items to a valid destination — overflow storage, a sink, or a secondary production line. Never leave a filter's reject output unconnected.

### Performance Issues with Many Pins
Hundreds of pins and wires can cause frame drops in the mid-to-late game. Use wire colors strategically to minimize connections, and group logic gates into compact clusters. Consider using a single comparator with multiple constant thresholds instead of several individual comparators.

---

## 🏭 Advanced Tips

- **Color-code your wires**: Use red wires for power/control signals, blue for data/item-property signals, green for clock/timing signals. This makes debugging infinitely easier.
- **Label your comparators**: Use the in-game label tool to write what each comparator's threshold is. You'll thank yourself when you revisit the factory 20 hours later.
- **Use delay belts for timing**: A belt with a defined length acts as a delay line. Combine with logic gates to create synchronization circuits — hold a shape at a filter until the matching component arrives.
- **Build small and test**: Don't wire up a whole factory at once. Build one sorter, test it, then clone it. Wiring bugs compound exponentially with scale.
- **Blueprint power**: Once you have a working quad-filter or memory cell, save it as a blueprint. You can drop pre-built logic modules anywhere in your factory.

---

> 🛒 [**Wishlist Shapez 2 on Steam**](https://store.steampowered.com/app/2162800/)
