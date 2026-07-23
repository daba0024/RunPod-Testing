#!/usr/bin/env python3
"""Minimal G-code sender for GRBL.

Usage:
    python send_gcode.py <serial-port> <file.gcode>

Examples:
    python send_gcode.py COM3 gcode/test-square.gcode          (Windows)
    python send_gcode.py /dev/ttyUSB0 gcode/test-square.gcode  (Linux/Mac)

Requires: pip install pyserial
"""
import sys
import time

try:
    import serial
except ImportError:
    sys.exit("pyserial is not installed. Run:  pip install pyserial")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    port, path = sys.argv[1], sys.argv[2]

    with open(path) as f:
        lines = [ln.split(";")[0].strip() for ln in f]
        lines = [ln for ln in lines if ln]

    with serial.Serial(port, 115200, timeout=5) as s:
        # Wake GRBL and let it finish booting
        s.write(b"\r\n\r\n")
        time.sleep(2)
        s.reset_input_buffer()

        total = len(lines)
        for i, line in enumerate(lines, 1):
            s.write((line + "\n").encode())
            # Wait for GRBL to acknowledge before sending the next line
            while True:
                reply = s.readline().decode(errors="replace").strip()
                if reply == "ok":
                    break
                if reply.startswith("error") or reply.startswith("ALARM"):
                    sys.exit(f"GRBL rejected line {i} ({line!r}): {reply}")
            print(f"[{i}/{total}] {line}")

    print("Done!")


if __name__ == "__main__":
    main()
