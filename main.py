#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one original funny line, a single sentence, to /output/entry.txt.
The line is fixed: the program is deterministic, so every run produces
the exact same entry.

Before writing, the line is checked against the competition gate: UTF-8
text of 1 to 200 characters, not only whitespace, and a single sentence.
If the check ever fails, the program refuses to write anything.
"""

import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

LINE = "The Wi-Fi went down for ten minutes and my family finally talked, mostly about when the Wi-Fi would come back."


def is_valid_line(line):
    """One sentence, 1-200 characters, not only whitespace."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    # A single sentence: exactly one sentence-ending mark, at the end.
    if sum(line.count(mark) for mark in ".!?") != 1:
        return False
    if line[-1] not in ".!?":
        return False
    return True


def main():
    if not is_valid_line(LINE):
        print("entry line fails the gate, refusing to write", file=sys.stderr)
        raise SystemExit(1)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
