# Troubleshooting

Work through these top-to-bottom — 90 % of first-build problems are on this page.

## Computer ↔ Arduino

| Symptom | Fix |
|---------|-----|
| No serial port appears | Install the **CH340 driver** (clone Nanos), try another USB cable — many cables are charge-only |
| Upload fails: `stk500_getsync` | Tools → Processor → **ATmega328P (Old Bootloader)** |
| Serial Monitor prints garbage | Set baud to **115200** |
| `error:` replies from GRBL | Line ending must be *Newline*; commands are case-sensitive-ish — use uppercase G-code |

## Motors

| Symptom | Fix |
|---------|-----|
| Buzzes/vibrates, doesn't spin | Coil pairs crossed: power off, swap the two wires of ONE coil (e.g. Blue↔Pink) |
| Doesn't move at all | RST–SLP jumper missing on that driver · EN not on D8 · Vref too low · cold solder on breadboard wire |
| Moves the wrong way | Invert with `$3` (X=1, Y=2, XY=3, Z=4, add to combine) — no rewiring needed |
| Stalls / skips during drawing | Lower speed (`$110=$111=300`), raise Vref slightly, check rack for print blobs, loosen an over-tight slide |
| Motor or driver gets hot | Vref too high — turn it down. Warm is OK, can't-touch is not |
| Moves only one direction | DIR wire loose on that axis |
| Random stops mid-job | Power supply too weak or breadboard wire loose; also disable computer sleep during long drawings |

## Drawing quality

| Symptom | Fix |
|---------|-----|
| Distances wrong (10 mm ≠ 10 mm) | Redo steps/mm calibration (Step 6B) |
| Circles are ovals | X and Y calibrated differently — recalibrate both |
| Wiggly/wobbly lines | Pen loose in holder · gear slipping on shaft (drop of super glue) · frame not screwed tight |
| Pen drags between shapes | Increase pen-up height in the G-code (Z3 → Z5) |
| Faint lines | Pen mounted too high; re-zero with the tip pressing very slightly into the paper |
| Drawing shifted / walks over time | Steps being skipped — see "stalls" above; also check the machine isn't hitting its physical travel limits (keep drawings inside ~90×90 mm) |

## Electrical safety reminders

- Never connect/disconnect a motor while the 12 V supply is on — it kills A4988 drivers instantly.
- Never connect the 12 V rail to the 5 V rail. GND rails, however, MUST be connected together.
- If something smells hot: power off first, investigate second.

## Still stuck?

- Re-watch the relevant section of [the build video](https://youtu.be/og1506q67mo) — pause and
  compare your wiring frame-by-frame.
- The comments on the video, the [MakerWorld page](https://makerworld.com/ru/models/2632836-build-a-simple-3d-cnc-plotter#profileId-2907504),
  and the [Thingiverse page](https://www.thingiverse.com/thing:4607077) are full of people who hit
  the same issue.
- GRBL's own wiki: [github.com/gnea/grbl/wiki](https://github.com/gnea/grbl/wiki)
