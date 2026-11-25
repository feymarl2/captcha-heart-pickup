#!/usr/bin/env python3
"""Robot romance pickup-line entry for make.fun.

Writes the single pickup line to /output/entry.txt. Standard library
only, no network, no clock, no randomness: byte-identical output.
"""

import os

TEXT = "Are you a captcha? Because my heart keeps failing to prove it's human around you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
