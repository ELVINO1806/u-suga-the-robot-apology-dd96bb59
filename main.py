"""Entry program for make.fun — The Robot Apology.

Writes the two-line apology entry to /output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

FIRST_LINE = "I am sorry I deleted your mother's voicemail while clearing old messages I thought nobody needed."
SECOND_LINE = "I learned that old does not mean unwanted, so now I ask before I delete anything with a voice in it."


def build_entry():
    """Join the two entry lines with a single newline, nothing else."""
    return FIRST_LINE + "\n" + SECOND_LINE


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = build_entry()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
