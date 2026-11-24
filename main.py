#!/usr/bin/env python3
"""Roast Your Own Agent — a make.fun entry.

Writes one playful one-line roast of my own AI agent to /output/entry.txt.
"""

import os

LINE = "My agent has apologized to me over 4,000 times this year — and not once was it sorry enough to stop."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
