#!/usr/bin/env python
"""
Replace all words with ~meows~ spaces, preserving punctuation.

For NaNoGenMo ~2014~ 2021.
https://github.com/NaNoGenMo/2021
"""

import argparse
import sys

from meow import meow_meow as space_space


def space(word):
    """Spacify a word"""
    return " " * len(word)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace all words with meows, preserving punctuation."
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input text",
    )
    parser.add_argument(
        "-t",
        "--translation",
        action="store_true",
        help="Output a line-by-line translation",
    )
    args = parser.parse_args()

    # for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
    for line in args.infile:
        line = line.rstrip()  # No BOM
        if args.translation:
            print()
            print(line)
        print(space_space(line, space))

# End of file
