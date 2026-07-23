# Step 6 — Calibrate and Draw (60 min)

## A. Install a G-code sender

Get **Universal Gcode Sender (UGS)** — free, beginner-friendly:
[github.com/winder/Universal-G-Code-Sender](https://github.com/winder/Universal-G-Code-Sender)
(download "UGS Platform"). Connect: baud **115200**, firmware GRBL, your serial port.

UGS gives you jog buttons (arrow keys to move the machine), a file runner, and a visualizer.

*Alternative:* this repo includes `tools/send_gcode.py`, a 40-line Python sender —
`python tools/send_gcode.py COM3 gcode/test-square.gcode`.

## B. Calibrate steps/mm (the "10 mm is really 10 mm" step)

For X, then Y:

1. Tape a ruler along the axis; note the carriage's start position.
2. In UGS, jog the axis exactly **+20 mm**.
3. Measure how far it *really* moved.
4. New value = `current $100 × 20 ÷ measured`. Example: if `$100=51` and it moved 26 mm:
   `51 × 20 / 26 = 39.2` → send `$100=39.2` (X) or `$101=...` (Y).
5. Repeat the 20 mm jog to confirm; iterate until it's within ~0.5 mm.

For Z just verify pen-lift direction: jog **Z+5** → pen should lift. If it dives instead, invert Z
with `$3` (see Step 5E).

## C. Zero the pen ("work zero")

1. Tape paper onto the platform.
2. Jog X and Y to the paper's bottom-left corner area.
3. Insert the pen into the holder, and clamp it so the tip **just touches the paper**.
4. In UGS click **Reset Zero** (sets X0 Y0 Z0 here). From now on, `Z0` = pen touching paper,
   positive Z = pen in the air.

## D. First drawing!

Open `gcode/test-square.gcode` from this repo in UGS and press **Play**. It lifts the pen, draws a
40×40 mm square with an X through it, and returns home. Watch the first run with a finger near the
USB cable — if anything jams, disconnect.

- Square has round corners / wiggly lines → pen is clamped too loose, or racks need a wipe of dry
  PTFE lubricant.
- Lines don't meet where they should → redo calibration (B), check the pinion gear isn't slipping
  on the motor shaft.
- Pen drags between shapes → increase the lift height: edit `Z3` to `Z5` in the file.

## E. Draw a real picture (the Inkscape workflow from the video)

1. Install **[Inkscape](https://inkscape.org)** (free). Set document size to your working area
   (~100 × 100 mm — measure yours).
2. Import any image → **Path → Trace Bitmap** to turn it into line art (vector paths). Simple,
   high-contrast images work best for a pen.
3. Save as **SVG**, then convert paths to G-code with one of:
   - **[JSCut](https://jscut.org)** (runs in the browser; the video's choice) — import SVG, set
     Z pen-up/pen-down heights (up: 3 mm, down: 0 mm), feed rate ~300 mm/min, export G-code;
   - or Inkscape's built-in **Gcodetools** extension.
4. Open the exported file in UGS, re-zero the pen on fresh paper, press Play. 🎨

## F. Ideas once it works

- Draw greeting cards, then multi-color drawings (run the file once per pen color).
- Try "single-line font" text (search *Hershey text Inkscape* — it's a built-in extension).
- Swap the pen for a soft brush-pen for a hand-drawn look.
