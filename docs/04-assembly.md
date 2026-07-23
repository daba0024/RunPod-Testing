# Step 3 — Mechanical Assembly (60 min)

This chapter follows the **step order of the MakerWorld guide** you're using:
[Build a Simple 3D CNC Plotter — makerworld.com/models/2632836](https://makerworld.com/ru/models/2632836-build-a-simple-3d-cnc-plotter#profileId-2907504).
Keep that page open next to this one — its photos show exactly how each part mates. This page adds
the beginner context and checkpoints.

> Do the [motor modification (Step 2)](03-motor-mod.md) **before** assembly — it's much easier to
> modify the motors before they're screwed into the frame.

## 3.1 Prepare the printed parts

- Remove all support material **carefully** — especially from the gear teeth and the sliding
  channels. Leftover support = jammed axis later.
- Test-slide every slider on its rail before assembly. It should glide with light finger pressure.
  Too tight → scrape/sand lightly. Way too loose → reprint that part (check belt/flow calibration).

## 3.2 Y-axis slider

The Y slider is printed in **split parts** (so it fits small print beds).

1. Connect the split parts of the Y-axis slider together. They should snap/screw into each other
   **tightly** — no wobble. Use M3 screws where holes are provided.
2. ✔ Checkpoint: the joined slider is flat (set it on a table — no rocking).

## 3.3 Y-axis gear rail

1. Join the Y-axis gear rail sections the same way — align the teeth carefully at the joints so
   the rack is one continuous straight toothed strip.
2. ✔ Checkpoint: sight down the rack — straight, with no step where the sections meet.

## 3.4 X-axis

1. Insert the X-axis gear rail and the X slider parts together, per the photos on the MakerWorld
   page.
2. Fasten with M3 screws.
3. ✔ Checkpoint: the slider travels the full rail smoothly end-to-end.

## 3.5 Gears onto the motors

1. Press a printed pinion gear onto each motor's D-shaft (flat side aligned). Snug fit is the
   goal; warm the gear in hot water if it's too tight, and save any glue for after the first
   successful test drawing.
2. Mount the X and Y motors into their printed mounts with M3 screws so each pinion **meshes with
   its gear rail** — teeth engaged fully but not binding.
3. ✔ Checkpoint: turn each motor shaft gently by hand (they resist — that's the gearbox, it's
   normal); the axis should move without clicking or skipping.

## 3.6 Z-axis: pen lift

1. Install the Z-axis motor into its mount on the X carriage.
2. Attach the **pen holder onto the Z motor's shaft** — on this design the pen holder mounts
   directly to the motor, and the motor rotation raises/lowers the pen.
3. Insert a pen and clamp it lightly for now — final pen height is set during calibration
   (Step 6), not now.

## 3.7 Electronics box

The design includes a printed electronics enclosure that rides along with the machine:

1. Fit the box base onto the **X motor and the Y gear rail** as shown on the MakerWorld page —
   it's designed to be **easily removable**, so don't glue it.
2. The Arduino Nano + the three A4988 drivers (breadboard or a mini PCB) live in this box.
   Leave the lid off until wiring (next step) is tested.

## 3.8 Mount and route

1. Mount the machine on your rigid base board (or a clean table edge) so the frame can't shift
   while drawing; the video simply tapes/screws it to a dark board.
2. Route the motor wires with the printed cable clips so no wire can snag a moving axis through
   the machine's **full travel** — push each axis end-to-end by hand to verify.

**Done when:** every axis slides freely by hand through full travel, gears mesh without slipping,
and nothing wobbles. Next: [Step 4 — Wiring](05-wiring.md).
