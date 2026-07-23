# Step 0 — Parts & Tools List

Order the electronics ~1 week ahead (AliExpress is cheapest but slow; Amazon is faster).
Everything here is a common hobby part — search the exact names below.

## Electronics (~$30–40)

| Qty | Part | Notes | ~Price |
|-----|------|-------|--------|
| 1 | **Arduino Nano** (or clone, "Nano V3 CH340") | The brain. Clones work fine; you may need the CH340 USB driver | $5 |
| 3 | **28BYJ-48 stepper motor, 5 V** | The small silver-blue geared motors. Often sold in 5-packs with ULN2003 boards — the green ULN2003 boards are **not used** in this build | $8 (5-pack) |
| 3 | **A4988 stepper driver module** (red/green Pololu-style) | Drives the motors. Usually sold in 5-packs. DRV8825 also works | $7 |
| 1 | **Breadboard** (830-point full size) | Everything plugs into this | $4 |
| 1 | **Jumper wire kit** (male–male + male–female Dupont wires) | | $5 |
| 1 | **12 V 2 A DC power adapter** + female DC barrel jack adapter (screw terminals) | Powers the motors. The Arduino itself is powered by USB | $8 |
| 3 | **100 µF electrolytic capacitor** (16 V or higher) | One across each driver's motor-power pins — protects the A4988s | $1 |
| 1 | **Mini-USB cable** (data-capable, not charge-only) | Nano uses mini-USB, not micro | $3 |

## Hardware & consumables

| Qty | Part | Notes |
|-----|------|-------|
| 1 kit | **M3 screws + nuts assortment** (6–20 mm lengths) | Holds the printed parts together; check the Thingiverse page/video for exact counts |
| ~300 g | **PLA filament** | For the printed parts (any color — the video uses purple) |
| 1 | **Fine-tip pen** (gel pen or fineliner) | The "tool head" |
| — | **Paper + masking tape** | Tape the paper to the bed |
| 1 | **Rigid base board** (~30×30 cm plywood/MDF, optional) | The video mounts everything on a dark board |

## Tools

- Small Phillips screwdriver
- Hobby knife (for the motor modification and cleaning 3D prints)
- Small flat screwdriver or ceramic screwdriver (to adjust the tiny potentiometer on the A4988)
- Multimeter — **strongly recommended** for setting the driver current safely (~$12 if you don't own one)
- Computer (Windows/Mac/Linux) with a USB port

## Do you have a 3D printer?

If **yes**: you're set — go to [Step 1: 3D printing](02-3d-printing.md).

If **no**, you can still build this:
- Public libraries and makerspaces often have printers you can use cheaply.
- Online print services (Craftcloud, PCBWay, JLC3DP) will print and mail the parts — upload the STL
  files from [Thingiverse](https://www.thingiverse.com/thing:4607077).
- A friend with a printer needs ~1 spool evening and ~300 g of filament.
