#!/usr/bin/env python
"""
Replace all words with no, preserving punctuation. Based on meow.py.
"""
from __future__ import print_function, unicode_literals

import re
import sys
import random
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def no_no(line):
    """Noify a line"""
    noed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            noed.append(no(thing))
        else:
            noed.append(thing)
    return u"".join(noed)


def no(word):
    """Noify a word"""
    noed = ""
    length = len(word)

    # Words longer than two will have:
    #  * first letter N
    #  * all others O

    return capify("n" + ("o" * (length-1)), word)


def capify(word, reference):
    """Make sure word has the same capitalisation as reference"""
    new_word = ""

    # First check whole word before char-by-char
    if reference.islower():
        return word.lower()
    elif reference.isupper():
        return word.upper()

    # Char-by-char checks
    for i, c in enumerate(reference):
        if c.isupper():
            new_word += word[i].upper()
        else:
            new_word += word[i]
    return new_word


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Replace all words with nos, preserving punctuation.")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, help="Input text")
    parser.add_argument('-t', '--translation', action="store_true",
                        help="Output a line-by-line translation")
    args = parser.parse_args()

#     for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
    for line in args.infile:
        line = line.decode("utf-8-sig").rstrip()  # No BOM
        if args.translation:
            print()
            print(line.encode("utf-8"))
        print(no_no(line).encode("utf-8"))

# End of file
