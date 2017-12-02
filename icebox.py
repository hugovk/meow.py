#!/usr/bin/env python
"""
Replace all words with plums, preserving punctuation.

For NaNoGenMo ~2014~ 2017.
~https://github.com/dariusk/NaNoGenMo-2014/~
https://github.com/NaNoGenMo/2017
"""
from __future__ import print_function, unicode_literals

import re
import sys
import random
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def plum_plum(line, converter_fun):
    """Plumify a line"""
    plummed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            plummed.append(converter_fun(thing))
        else:
            plummed.append(thing)
    return u"".join(plummed)


def plum(word):
    """Plumify a word"""
    plummed = ""
    length = len(word)

    if length == 1:
        return capify("p", word)
    elif length == 2:
        return capify("pl", word)
    elif length == 3:
        return capify("plm", word)
    elif length == 4:
        return capify("plum", word)

    # Words longer than four will have:
    #  * first letter P
    #  * last letter M
    #  * middle with a random number of Ls, then some Us

    # Number of LUs:
    elyous = length - len("p") - len("m")
    # Number of Ls:
    els = random.randrange(1, elyous)
    # Number of Os:
    yous = elyous - els

    plummed = "p" + ("l" * els) + ("u" * yous) + "m"
    return capify(plummed, word)


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
        description="Replace all words with plums, preserving punctuation.")
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
        print(plum_plum(line, plum).encode("utf-8"))

# End of file
