#!/usr/bin/env python
"""
Unit tests for no.py
"""

import unittest
import meow
import no
import re


class TestIt(unittest.TestCase):

    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

        # Check pattern
        if len(word) > 1:
            found = re.match("n[o]+", out, re.IGNORECASE)
            self.assertTrue(found)

        # Check caps
        for i in range(len(word)):
            self.assertEqual(word[i].isupper(),
                             out[i].isupper())

    def test_1_letter_word(self):
        word = "I"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "N")

    def test_2_letter_word(self):
        word = "on"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "no")

    def test_3_letter_word(self):
        word = "The"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Noo")

    def test_4_letter_word(self):
        word = "book"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "nooo")

    def test_upper_4_letter_word(self):
        word = "NOOO"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "NOOO")

    def test_capped_4_letter_word(self):
        word = "Nooo"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Nooo")

    def test_mixcapped_4_letter_word(self):
        word = "NooO"
        out = no.no(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "NooO")

    def test_5_letter_word(self):
        word = "clock"
        out = no.no(word)
        self.sanity_check(word, out)

    def test_6_letter_word(self):
        word = "whales"
        out = no.no(word)
        self.sanity_check(word, out)

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = no.no(word)
        self.sanity_check(word, out)

    def test_line(self):
        line = "On the bus"
        out = meow.meow_meow(line, no.no)
        self.assertEqual(out, "No noo noo")

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = meow.meow_meow(line, no.no)
        self.assertEqual(out, "No noo noo? No noo noo.")
        self.assertEqual(out, "No noo noo? No noo noo.")


if __name__ == '__main__':
    unittest.main()

# End of file
