#!/usr/bin/env python
"""
Replace all words with no, preserving punctuation. Based on meow.py.
"""

import argparse
import sys

import meow


def no(word):
    """Noify a word"""
    length = len(word)

    # Words longer than two will have:
    #  * first letter N
    #  * all others O

    return meow.capify("n" + ("o" * (length - 1)), word)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace all words with nos, preserving punctuation."
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
        line = line.decode("utf-8-sig").rstrip()  # No BOM
        if args.translation:
            print()
            print(line.encode("utf-8"))
        print(meow.meow_meow(line, no).encode("utf-8"))

# End of file
