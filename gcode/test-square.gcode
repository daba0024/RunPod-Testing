; Test pattern: 40x40 mm square with an X through it
; Assumes: work zero set with pen tip touching paper (Z0), pen up = Z3
; Feed: 300 mm/min drawing, pen moves at 200
G21         ; millimeters
G90         ; absolute coordinates
G0 Z3       ; pen up
G0 X0 Y0    ; go to origin
; --- square ---
G1 Z0 F200  ; pen down
G1 X40 Y0 F300
G1 X40 Y40
G1 X0 Y40
G1 X0 Y0
G0 Z3       ; pen up
; --- diagonal 1 ---
G1 Z0 F200
G1 X40 Y40 F300
G0 Z3
; --- diagonal 2 ---
G0 X40 Y0
G1 Z0 F200
G1 X0 Y40 F300
G0 Z3
; --- done, return home ---
G0 X0 Y0
