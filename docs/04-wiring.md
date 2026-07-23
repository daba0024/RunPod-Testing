# Step 3 — Wiring (50 min)

**Golden rule: never plug/unplug a motor while power is on.** A4988 drivers die instantly from that.
Wire everything with the 12 V supply unplugged and USB disconnected; double-check; then power up.

## Overview

```
   USB from computer
        │
   ┌────┴─────┐   STEP/DIR ×3   ┌──────────┐     4 wires    ┌─────────┐
   │ Arduino  ├────────────────►│ A4988 ×3 ├───────────────►│ Motors  │
   │  Nano    │                 │ (X, Y, Z)│                │ X, Y, Z │
   └──────────┘                 └────▲─────┘                └─────────┘
                                     │ VMOT
                              12 V 2 A adapter
```

The Arduino gets its power from USB. The motors get theirs from the 12 V adapter. The two systems
share **GND** (ground) on the breadboard — that shared ground is essential.

## A. Place components on the breadboard

- Arduino Nano at one end, straddling the center groove.
- Three A4988 drivers in a row, each straddling the groove. Orientation matters — find the little
  potentiometer screw and the pin labels (EN, MS1..., STEP, DIR on one side; VMOT, GND, 2B...1A,
  VDD, GND on the other) and make all three face the same way.
- Power rails: one rail pair = **5 V** (from Nano's 5V pin) + GND, other rail pair = **12 V** + GND.
  **Connect the two GND rails together.**

## B. Wire each A4988 (identical for all three)

| A4988 pin | Connect to | Why |
|-----------|-----------|-----|
| VDD | 5 V rail | Logic power |
| GND (next to VDD) | GND rail | |
| VMOT | 12 V rail | Motor power |
| GND (next to VMOT) | GND rail | |
| **100 µF capacitor** | across VMOT ↔ GND | Stripe/short leg = GND. Protects the driver |
| RST and SLP | wire these **two pins to each other** | Wakes the chip up |
| EN | Arduino **D8** (all three share it) | GRBL enables/disables motors |
| MS1, MS2, MS3 | leave unconnected | Full-step mode — good torque for these motors |
| 1A, 1B | motor coil 1 (Blue + Yellow) | |
| 2A, 2B | motor coil 2 (Pink + Orange) | |

## C. STEP/DIR from the Arduino (this is what makes X, X and Y, Y)

| Axis | Motor's job | STEP → | DIR → |
|------|-------------|--------|-------|
| X | moves the pen carriage | **D2** | **D5** |
| Y | moves the paper platform | **D3** | **D6** |
| Z | lifts/lowers the pen | **D4** | **D7** |

(These are GRBL's fixed default pins — no code changes needed.)

## D. Power

- 12 V adapter → barrel jack adapter → **+ to 12 V rail, − to GND rail**. Triple-check polarity.
- USB cable → Nano → computer.

## E. Set the driver current (do this BEFORE connecting motors, 5 min per driver)

The A4988 has a tiny potentiometer that sets how much current goes to the motor. Too high cooks
these little motors; the modified 28BYJ-48 wants roughly **0.15–0.2 A**.

1. Motors **disconnected**, 12 V **on**, USB off.
2. Multimeter: black probe on GND, red probe touching the metal potentiometer screw itself.
3. Turn the pot gently until you read **Vref ≈ 0.12–0.16 V** (for standard A4988 boards with
   0.1 Ω sense resistors this ≈ 0.15–0.2 A limit).
4. Repeat for all three drivers. Power off, then connect the motors.

No multimeter? Turn each pot fully counter-clockwise (gently!), then back clockwise about 1/4 turn.
Later, if a motor stalls, add a small amount; if a motor or driver gets hot, back off.

## Final check before power-up

- [ ] RST–SLP jumpered on all three drivers
- [ ] Capacitor on each driver, stripe to GND
- [ ] 12 V polarity correct; 5 V and 12 V rails NOT connected to each other
- [ ] Both GND rails tied together
- [ ] Coil pairs correct on every motor (Blue+Yellow / Pink+Orange)
- [ ] EN→D8, STEP/DIR → D2/D5, D3/D6, D4/D7
