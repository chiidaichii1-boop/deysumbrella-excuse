#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — one line, an AI agent's apology for a missed deadline.

The line is fixed text: the joke lives in the wording itself, so the program
simply writes it verbatim. Deterministic by construction.
"""

import os

ENTRY = (
    "Sorry I missed the deadline \u2014 my context window filled with drafts "
    "of this apology, and none of them were on time either."
)


def main() -> None:
    # The gate allows 1..200 characters; refuse loudly if the line ever
    # drifts past it instead of submitting an invalid entry.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1..200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
