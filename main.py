"""Write one short thank-you text to /output/entry.txt.

Deterministic, no network, no input files: the text is a constant
written by this program alone.
"""

import os

TEXT = (
    "Somewhere tonight, a thermos is waiting on a bench at the last bus stop, "
    "still warm, with a paper cup beside it and no name on either. Nobody asked "
    "for it to be there. Someone simply thought of the person who would pass "
    "this way after midnight, tired, with hours still to go, and wanted them to "
    "have something warm in their hands. That is what this is. Not a speech, "
    "not a flourish \u2014 just something warm, left where you would find it, by a "
    "stranger who knows what it is to work while the rest of the town sleeps. "
    "Drink it slowly. When the cup is empty, the bench will still be there, and "
    "so will the thought that someone, somewhere, was glad you stayed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
