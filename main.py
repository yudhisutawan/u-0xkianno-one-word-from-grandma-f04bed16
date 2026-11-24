#!/usr/bin/env python3
"""One Word From Grandma — entry program (stdlib only).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
The word is the tournament winner from TOURNAMENT.md.
Competition: u-0xkianno-one-word-from-grandma-f04bed16
("One Word From Grandma" — the single word grandma would text
about AI). Gate: entry.txt must be UTF-8 text of 1 to 30
characters, not only white space.
No writes to the repository directory; no network; no imports
beyond the standard library.
"""

import os

WORD = "Roomba"


def main() -> None:
    # Gate guard (validation only): entry must be 1-30 characters.
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
