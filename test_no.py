#!/usr/bin/env python
"""
Unit tests for meow.py
"""
from __future__ import print_function, unicode_literals

import unittest
import meow
import re


class TestIt(unittest.TestCase):

    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

        # Check pattern
        if len(word) > 4:
            found = re.match("m[e]+[o]+w", out, re.IGNORECASE)
            self.assertTrue(found)

        # Check caps
        for i in range(len(word)):
            self.assertEqual(word[i].isupper(),
                             out[i].isupper())

    def test_1_letter_word(self):
        word = "I"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "M")

    def test_2_letter_word(self):
        word = "on"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "me")

    def test_3_letter_word(self):
        word = "The"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Mew")

    def test_4_letter_word(self):
        word = "book"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "meow")

    def test_capify_1(self):
        word = "meow"
        reference = "Book"
        out = meow.capify(word, reference)
        self.assertEqual(out, "Meow")

    def test_capify_2(self):
        word = "meow"
        reference = "BOOK"
        out = meow.capify(word, reference)
        self.assertEqual(out, "MEOW")

    def test_capify_3(self):
        word = "meow"
        reference = "book"
        out = meow.capify(word, reference)
        self.assertEqual(out, "meow")

    def test_capify_4(self):
        word = "meow"
        reference = "BoOk"
        out = meow.capify(word, reference)
        self.assertEqual(out, "MeOw")

    def test_upper_4_letter_word(self):
        word = "BOOK"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "MEOW")

    def test_capped_4_letter_word(self):
        word = "Book"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Meow")

    def test_mixcapped_4_letter_word(self):
        word = "BooK"
        out = meow.meow(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "MeoW")

    def test_5_letter_word(self):
        word = "clock"
        out = meow.meow(word)
        self.sanity_check(word, out)

    def test_6_letter_word(self):
        word = "whales"
        out = meow.meow(word)
        self.sanity_check(word, out)

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = meow.meow(word)
        self.sanity_check(word, out)

    def test_line(self):
        line = "On the bus"
        out = meow.meow_meow(line)
        self.assertEqual(out, "Me mew mew")

    def test_is_word_1(self):
        thing = "word"
        out = meow.is_word(thing)
        self.assertTrue(out)

    def test_is_word_2(self):
        thing = ";"
        out = meow.is_word(thing)
        self.assertFalse(out)

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = meow.meow_meow(line)
        self.assertEqual(out, "Me mew mew? Me mew mew.")


if __name__ == '__main__':
    unittest.main()

# End of file
