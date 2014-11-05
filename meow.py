#!/usr/bin/env python
"""
Replace all words with meows, preserving punctuation.

For NaNoGenMo 2014.
https://github.com/dariusk/NaNoGenMo-2014/
"""
from __future__ import print_function, unicode_literals

import re
import sys
import random
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def meow_meow(line, converter_fun):
    """Meowify a line"""
    meowed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            meowed.append(converter_fun(thing))
        else:
            meowed.append(thing)
    return u"".join(meowed)


def meow(word):
    """Meowify a word"""
    meowed = ""
    length = len(word)

    if length == 1:
        return capify("m", word)
    elif length == 2:
        return capify("me", word)
    elif length == 3:
        return capify("mew", word)
    elif length == 4:
        return capify("meow", word)

    # Words longer than four will have:
    #  * first letter M
    #  * last letter W
    #  * middle with a random number of Es, then some Os

    # Number of EOs:
    eeohs = length - len("m") - len("w")
    # Number of Es:
    ees = random.randrange(1, eeohs)
    # Number of Os:
    ohs = eeohs - ees

    meowed = "m" + ("e" * ees) + ("o" * ohs) + "w"
    return capify(meowed, word)


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
        description="Replace all words with meows, preserving punctuation.")
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
        print(meow_meow(line, meow).encode("utf-8"))

# End of file
