#!/usr/bin/env python3
"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

The word is "Uh-oh" -- the sound of a machine catching itself mid-task,
realising it is completely lost, with nowhere left to bluff. It is a genuine
blurt, not a status report: no recalculating, no buffering, no pretending.
"""

import os

WORD = "Uh-oh"


def main() -> None:
    if not 1 <= len(WORD) <= 99:
        raise ValueError("entry word must be 1-99 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
