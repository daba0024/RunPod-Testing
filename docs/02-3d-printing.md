# Step 1 — 3D Printing the Parts (start days before build day)

## Download the files — use the MakerWorld print profile

Primary source (the guide we follow):
**[MakerWorld — Build a Simple 3D CNC Plotter, print profile 2907504](https://makerworld.com/ru/models/2632836-build-a-simple-3d-cnc-plotter#profileId-2907504)**

If you have a Bambu Lab printer (or use Bambu/Orca Studio), click **"Open in Bambu Studio"** on
that profile — the plates arrive pre-arranged with the tested settings, and you can just press
print. Otherwise download the STLs from the same page (or from
[Thingiverse thing:4607077](https://www.thingiverse.com/thing:4607077)) and slice them yourself
with the settings below.

The set includes: the X and Y axis frames/rails, **gear racks** (the long toothed strips you can see
in the video), **pinion gears** that press onto the motor shafts, motor mounts, the pen holder /
Z-axis carriage, and cable clips.

## Print settings (if slicing yourself)

| Setting | Value |
|---------|-------|
| Layer height | 0.2 mm |
| Infill | 20–30 % (gears and pinions: 50–100 % for strength) |
| Supports | **Follow the MakerWorld profile** — some parts in this version print with supports; remove them carefully afterwards |
| Material | PLA |
| Bed adhesion | Brim on the long rack pieces (they like to warp/detach) |

Total print time is roughly **10–15 hours** depending on your printer — queue the parts up a few
days early. Print one small part first (a cable clip) to confirm your printer is dialed in.

## Quality checklist after printing

- [ ] All support material removed, especially from gear teeth and sliding channels
- [ ] Racks are straight (sight down their length — a bowed rack causes jams)
- [ ] Pinion gear presses snugly onto a motor shaft (the 28BYJ-48 shaft is a 5 mm D-shaft)
- [ ] Sliding parts actually slide — scrape off blobs/strings with a hobby knife
- [ ] Screw holes are clear (run an M3 screw through each once)

If a gear won't fit the motor shaft, warm it gently (hot water) or ream the hole slightly with a
knife. If it's loose, a tiny drop of super glue after final assembly fixes it.
