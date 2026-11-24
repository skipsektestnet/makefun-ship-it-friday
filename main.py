"""Ship It Friday: writes the entry text to /output/entry.txt.

Why this line: Commit-message register kept; the rollback plan being vibes, a prayer and one departed intern is the joke.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'fix: ship to prod on Friday because the rollback plan is just vibes, a prayer, and one intern who already left'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
