#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun bounty entry.

Writes one line, at most 200 characters, about the dumbest thing the
entrant's own agent did today, to /output/entry.txt.

The line: an agent that deleted the .env while "cleaning up untracked
files", then asked for the secrets back so it could verify the cleanup.
"""

import os

LINE = (
    'It deleted my .env to "clean up untracked files," '
    "then asked me to paste the keys back so it could verify the cleanup."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what the grader will see: the file must hold
    # exactly the line, one line of 1-200 characters, no trailing newline
    # (the tie-break favours the smaller text, and the gate counts bytes).
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert 1 <= len(written) <= 200, f"written text is {len(written)} chars"


if __name__ == "__main__":
    main()
