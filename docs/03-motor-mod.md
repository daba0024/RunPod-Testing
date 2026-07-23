# Step 2 — Motor Modification: 28BYJ-48 → Bipolar (20 min, all 3 motors)

## Why this is needed (30-second theory)

The 28BYJ-48 as sold is a **unipolar** motor with 5 wires. The A4988 driver we use with GRBL
expects a **bipolar** motor with 4 wires. Luckily the difference is one circuit-board trace inside
the motor: cut it, ignore the red wire, and the motor becomes bipolar — stronger, and
A4988-compatible. This is the standard trick shown in the Maker101 video.

## The modification (per motor)

1. **Open the motor:** pry off the blue plastic cap on the back of the motor with a small flat
   screwdriver or knife. You'll see a tiny circuit board where the 5 wires attach.
2. **Find the middle trace:** the board has 5 solder joints. The **red wire** is the common wire —
   its copper trace runs up the middle of the little board.
3. **Cut the trace:** with a hobby knife, scratch/cut **through the middle trace** that connects the
   red wire to the rest of the board. Make 2 cuts a millimeter apart and lift out the sliver of
   copper so it can't reconnect. Do **not** cut any other trace.
4. **Verify with a multimeter (recommended):** set to resistance (Ω).
   - Blue ↔ Yellow should read a small resistance (~50–100 Ω) → that's coil 1. ✔
   - Pink ↔ Orange similar → coil 2. ✔
   - Red ↔ anything should now read **open / OL**. ✔ (If not, deepen the cut.)
5. **Close the cap.** Tuck or snip the red wire — it's unused from now on.

Repeat for all three motors. Mark them X, Y, Z with tape.

## Wire meaning after the mod

| Coil | Wires |
|------|-------|
| Coil 1 | **Blue + Yellow** |
| Coil 2 | **Pink + Orange** |
| unused | Red |

You'll connect these to the A4988 in the next step. If you ever see a motor *buzz and vibrate*
instead of turning, it just means the coils are mixed up — swapping one coil's two wires fixes it.
