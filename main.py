#!/usr/bin/env python3
"""Probe entry for "Two Days of Quiet Dread".

The program's whole job is to emit one line of text into
/output/entry.txt: a code review comment that green-lights a
pull request while quietly admitting that everything around the
code — the team, the stack, the reviewer — is on a timer.
Pure standard library, no input, no network; the two grader
runs therefore write byte-identical output.
"""

import os
import sys

# Why this line: it opens with a plain approval, then lets the
# dread leak in through a matter-of-fact inventory of what the
# code will outlast. The escalation (company, then language,
# then the reviewer himself) does the comic work, and the flat
# landing — "but the diff looks clean" — keeps the tone that of
# a tired engineer clicking Approve, not a cry for help.
COMMENT = (
    "Approved. This code will outlive the company, the language, "
    "and eventually me, but the diff looks clean."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(COMMENT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
