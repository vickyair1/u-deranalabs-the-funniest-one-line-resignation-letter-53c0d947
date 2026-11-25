#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The letter is written by a webhook that has fired into a dead endpoint
for six months without anyone noticing. The joke turns on three beats:

  1. Setup   -- six months of silent, unnoticed work ("fired into a
                dead endpoint"), the flat complaint of a neglected worker.
  2. Turn    -- "my final delivery": a webhook's job is delivery, so
                the resignation itself is framed as one last delivery.
  3. Punch   -- "I quit.", the plain resignation, landing after the turn.

The line is built from its beats, validated against the gate
(1-140 chars, UTF-8, not only whitespace, single line), written with
no trailing newline, then read back and checked byte for byte.
"""

import os

# Beat 1: the setup -- the neglected work.
SETUP = "For six months I have fired into a dead endpoint and nobody noticed, "
# Beat 2: the turn -- the resignation framed as one last delivery.
TURN = "so consider this my final delivery: "
# Beat 3: the punch -- the plain resignation.
PUNCH = "I quit."

ENTRY = SETUP + TURN + PUNCH

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def build_entry() -> str:
    """Assemble the letter from its three beats."""
    return SETUP + TURN + PUNCH


def validate(entry: str) -> None:
    """Check the entry against the competition gate."""
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, gate is 1-140")
    if not entry.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def write_entry(entry: str) -> None:
    """Write the entry with no trailing newline, then round-trip guard."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise ValueError("round-trip mismatch: file does not match entry")


def main() -> None:
    entry = build_entry()
    validate(entry)
    write_entry(entry)
    print(f"chars: {len(entry)}")
    print(entry)


if __name__ == "__main__":
    main()
