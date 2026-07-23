; Calibration check: draws a 50 mm horizontal line and a 50 mm vertical line
; Measure them with a ruler — both must be exactly 50 mm.
; If not: new $100 = current $100 * 50 / measured_X   (same idea for $101 with Y)
G21
G90
G0 Z3
G0 X0 Y0
G1 Z0 F200
G1 X50 Y0 F300   ; 50 mm along X
G0 Z3
G0 X0 Y0
G1 Z0 F200
G1 X0 Y50 F300   ; 50 mm along Y
G0 Z3
G0 X0 Y0
