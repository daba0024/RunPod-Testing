# Step 4 — Firmware: Put GRBL on the Arduino (30 min)

GRBL is free, battle-tested CNC firmware. You don't write any code — you install it once and then
talk to it over USB.

## A. Install the Arduino IDE

1. Download the **Arduino IDE** from [arduino.cc/en/software](https://www.arduino.cc/en/software) and install it.
2. Plug in the Nano. If no serial port shows up (very common with clone Nanos), install the
   **CH340 driver** (search "CH340 driver" + your OS; it's a 1-minute install), then replug.

## B. Install GRBL

1. Download GRBL v1.1: go to [github.com/gnea/grbl](https://github.com/gnea/grbl) → green **Code**
   button → **Download ZIP**. Unzip it.
2. Inside the unzipped folder there is a folder literally named `grbl`. In the Arduino IDE:
   **Sketch → Include Library → Add .ZIP Library...** — but select that inner `grbl` **folder**
   (the IDE accepts folders too). This installs GRBL as a library.
3. **File → Examples → grbl → grblUpload** — opens a tiny sketch. No edits needed.
4. **Tools → Board → Arduino Nano**. **Tools → Processor → ATmega328P** (if upload fails later,
   try **ATmega328P (Old Bootloader)** — most clones need this). **Tools → Port →** your port.
5. Click **Upload** (arrow button). Success looks like "Done uploading."

## C. First contact 🎉

1. **Tools → Serial Monitor**, set **115200 baud** (bottom-right dropdown), line ending = *Newline*.
2. You should see: `Grbl 1.1h ['$' for help]` — your plotter is alive.
3. Type `$$` and press Enter — GRBL prints its settings list.

## D. Smoke test — make the motors move

With 12 V on, type each line and press Enter. Watch/hold each motor:

```
$1=255        (keep motors engaged and holding)
G91           (relative-move mode)
G0 X10        → X motor should turn
G0 Y10        → Y motor should turn
G0 Z5         → Z motor should turn
```

- **Motor turns:** ✔ move on.
- **Buzzes/vibrates but doesn't turn:** the two coils are cross-wired — power off, swap the two
  wires of ONE coil on that driver (e.g. swap Blue and Pink), retry.
- **Nothing at all:** check that driver's RST–SLP jumper, EN wire, and Vref.

## E. Load the recommended settings

Copy-paste this whole block into the Serial Monitor (these match this machine; `$100/$101/$102`
get fine-tuned in the next step):

```
$0=10
$1=255
$3=0
$4=0
$5=0
$20=0
$21=0
$22=0
$30=1000
$31=0
$32=0
$100=51
$101=51
$102=51
$110=500
$111=500
$120=50
$121=50
$122=50
$130=100
$131=100
$132=20
```

What the important ones mean:
- `$100/$101/$102` — steps per millimeter for X/Y/Z. **51 is a starting guess**; we calibrate it
  precisely in Step 5. (Math: the modified 28BYJ-48 does ~2038 full steps per revolution; divided
  by the printed pinion's circumference ≈ 40 mm → ~51 steps/mm. Your printed gear may differ.)
- `$110/$111` — max speed 500 mm/min. These geared motors are slow; faster = skipped steps.
- `$120–122` — gentle acceleration so the light frame doesn't shake.
- If an axis later moves the **wrong direction**, don't rewire — set `$3`:
  `$3=1` inverts X, `2` inverts Y, `3` inverts X+Y, `4` inverts Z (add values to combine).
