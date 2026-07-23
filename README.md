# Mini CNC Pen Plotter — First-Timer Build Guide

A complete, beginner-friendly guide to building the **Maker101 "Build a simple 3D mini CNC plotter"**
([the YouTube video](https://youtu.be/og1506q67mo)) — a small machine that grips a pen and draws
pictures on paper, controlled by an Arduino.

**How it works in one paragraph:** Two small stepper motors move a pen left/right (X axis) and the
paper platform forward/back (Y axis) using 3D-printed racks and gears. A third stepper lifts the pen
up and down (Z axis). An Arduino Nano runs a free firmware called **GRBL** that listens over USB for
"G-code" commands (`move to X10 Y20`, `pen down`, ...). You draw something in the free program
**Inkscape**, convert it to G-code, and stream it to the Arduino — the machine draws it.

## Primary reference

We follow the creator's own step-by-step guide on MakerWorld:
**[Build a Simple 3D CNC Plotter (model 2632836, print profile 2907504)](https://makerworld.com/ru/models/2632836-build-a-simple-3d-cnc-plotter#profileId-2907504)**.
Keep it open while building — it has the photos. The docs below follow the same step order and add
beginner explanations, checkpoints, exact wiring pins, and troubleshooting.

## Guide contents (read in order)

| Step | File | What you'll do |
|------|------|----------------|
| 0 | [docs/01-parts-list.md](docs/01-parts-list.md) | Buy/gather all parts (~$35–45) |
| 1 | [docs/02-3d-printing.md](docs/02-3d-printing.md) | Print the frame parts (**do this days before build day!**) |
| 2 | [docs/03-motor-mod.md](docs/03-motor-mod.md) | 5-minute modification to each motor |
| 3 | [docs/04-assembly.md](docs/04-assembly.md) | Assemble the machine (MakerWorld step order) |
| 4 | [docs/05-wiring.md](docs/05-wiring.md) | Wire everything on a breadboard |
| 5 | [docs/06-firmware.md](docs/06-firmware.md) | Install GRBL on the Arduino |
| 6 | [docs/07-software-and-first-draw.md](docs/07-software-and-first-draw.md) | Calibrate and draw your first picture |
| — | [docs/08-troubleshooting.md](docs/08-troubleshooting.md) | When something doesn't work |

Extras in this repo:

- `gcode/` — ready-made test drawings you can run immediately
- `tools/send_gcode.py` — a tiny Python program that sends a G-code file to the plotter
  (alternative to the Universal Gcode Sender app)

## The 4-hour build plan

> **Reality check before you start:** the 3D-printed parts take **10–15 hours of printer time**.
> That happens unattended, but it must happen **before** build day. The 4 hours below assume the
> printed parts are sitting on your desk. Same for shipping — order electronics a week ahead.

| Time | Stage | Guide | What happens |
|------|-------|-------|--------------|
| 0:00–0:20 | Setup | Step 0 | Lay out parts, install Arduino IDE + drivers on your computer |
| 0:20–0:40 | Motor mod | Step 2 | Convert the three 28BYJ-48 motors to "bipolar" (small cut inside each) |
| 0:40–1:40 | Assembly | Step 3 | MakerWorld order: Y slider → Y gear rail → X axis → gears on motors → Z pen holder → electronics box |
| 1:40–2:30 | Wiring | Step 4 | Breadboard: Arduino + 3 stepper drivers + motors + power |
| 2:30–3:00 | Firmware | Step 5 | Flash GRBL, smoke-test: make each motor move from the computer |
| 3:00–3:30 | Calibration | Step 6 | Set steps/mm so 10 mm commanded = 10 mm moved; set pen height |
| 3:30–4:00 | First drawing! | Step 6 | Run `gcode/test-square.gcode`, then draw a real picture |

## Official project sources

- **Video:** [Build a simple 3D mini CNC plotter — @maker101io](https://youtu.be/og1506q67mo)
- **STL files + step-by-step guide (primary):** [MakerWorld model 2632836](https://makerworld.com/ru/models/2632836-build-a-simple-3d-cnc-plotter#profileId-2907504)
  · also on [Thingiverse thing:4607077](https://www.thingiverse.com/thing:4607077)
- **Creator's write-up:** [Arduino Project Hub](https://projecthub.arduino.cc/maker101io/build-a-simple-3d-printed-cnc-plotter-machine-dc76c9)
  · [PCBWay project page](https://www.pcbway.com/project/shareproject/Build_a_simple_3D_Arduino_Mini_CNC_Plotter_e2c3f905.html)
- **Firmware:** [GRBL v1.1 on GitHub](https://github.com/gnea/grbl)

*Always cross-check wiring and part choices against the video and the creator's pages above — if this
guide and the video ever disagree, trust the video.*
