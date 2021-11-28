#!/usr/bin/env python
"""
Unit tests for icebox.py
"""

import re
import unittest

import icebox


class TestIt(unittest.TestCase):
    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

        # Check pattern
        if len(word) > 4:
            found = re.match("p[l]+[u]+m", out, re.IGNORECASE)
            self.assertTrue(found)

        # Check caps
        for i in range(len(word)):
            self.assertEqual(word[i].isupper(), out[i].isupper())

    def test_1_letter_word(self):
        word = "I"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "P")

    def test_2_letter_word(self):
        word = "on"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "pl")

    def test_3_letter_word(self):
        word = "The"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Plm")

    def test_4_letter_word(self):
        word = "book"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "plum")

    def test_capify_1(self):
        word = "plum"
        reference = "Book"
        out = icebox.capify(word, reference)
        self.assertEqual(out, "Plum")

    def test_capify_2(self):
        word = "plum"
        reference = "BOOK"
        out = icebox.capify(word, reference)
        self.assertEqual(out, "PLUM")

    def test_capify_3(self):
        word = "plum"
        reference = "book"
        out = icebox.capify(word, reference)
        self.assertEqual(out, "plum")

    def test_capify_4(self):
        word = "plum"
        reference = "BoOk"
        out = icebox.capify(word, reference)
        self.assertEqual(out, "PlUm")

    def test_upper_4_letter_word(self):
        word = "BOOK"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "PLUM")

    def test_capped_4_letter_word(self):
        word = "Book"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Plum")

    def test_mixcapped_4_letter_word(self):
        word = "BooK"
        out = icebox.plum(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "PluM")

    def test_5_letter_word(self):
        word = "clock"
        out = icebox.plum(word)
        self.sanity_check(word, out)

    def test_6_letter_word(self):
        word = "whales"
        out = icebox.plum(word)
        self.sanity_check(word, out)

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = icebox.plum(word)
        self.sanity_check(word, out)

    def test_line(self):
        line = "On the bus"
        out = icebox.plum_plum(line, icebox.plum)
        self.assertEqual(out, "Pl plm plm")

    def test_is_word_1(self):
        thing = "word"
        out = icebox.is_word(thing)
        self.assertTrue(out)

    def test_is_word_2(self):
        thing = ";"
        out = icebox.is_word(thing)
        self.assertFalse(out)

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = icebox.plum_plum(line, icebox.plum)
        self.assertEqual(out, "Pl plm plm? Pl plm plm.")


if __name__ == "__main__":
    unittest.main()

# End of file
