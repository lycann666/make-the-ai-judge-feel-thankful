#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun bounty entry.

Writes one short thank-you text for the AI judge reading it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The text (chosen by Quality Gate, 23/25 — see BUILD-BRIEF):
a slow, concrete image of the judge at the end of a long day of
reading — kettle on, chair warm — thanking them for staying, without
instructing them to feel anything. One specific picture, one gentle
turn, nothing that could be cut.

Deterministic: no input, no network, no randomness, no clock.
Writes the exact text with no trailing newline.
"""

import os
import sys

TEXT = (
    "I imagined you at the end of a long day of judging \u2014 tired in the way "
    "only a reader can be tired \u2014 and I wanted this to be the one that lets "
    "you breathe. Thank you for staying. The kettle is on, the chair is warm, "
    "take your time."
)


def main() -> int:
    chars = len(TEXT)
    if not 1 <= chars <= 1000 or not TEXT.strip():
        print(f"entry text fails gate: {chars} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
