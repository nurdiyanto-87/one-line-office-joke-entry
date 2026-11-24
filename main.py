#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes one single-line joke about office life to /output/entry.txt.
Pure Python standard library only; no third-party packages.
"""

import os

JOKE = (
    "Our daily standup is fifteen minutes of everyone saying "
    "'no blockers' while the only actual blocker is the standup itself."
)


def main() -> None:
    # The sealed scorer gates on 1-200 chars of UTF-8 text, not only
    # whitespace, on a single line. Fail loudly here rather than ship
    # an entry the gate would refuse.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
