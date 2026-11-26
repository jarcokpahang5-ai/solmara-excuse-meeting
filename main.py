"""The Funniest Excuse for Skipping a Meeting.

Writes a single original funny excuse line to /output/entry.txt
and prints exactly that line to stdout. Pure Python 3 standard
library, deterministic, no network access.
"""

import os

LINE = "My dog ate my meeting invite — and after one look at the agenda, I let him finish it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
