#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2
("Office Artifacts: The One-Line Placard Contest").

Writes the one-line museum placard to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), UTF-8, with no trailing newline.
"""

import os

ENTRY_FILENAME = "entry.txt"

ENTRY_TEXT = (
    "Stapler, Ritual Binding Device, c. 1997. Pressed steel, donor unknown. "
    "Used to fasten offerings to the god of deadlines; jammed once, "
    "worshipped ever since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
