#!/usr/bin/env python
"""
Unit tests for no_meows.py
"""

import unittest

import no_meows


class TestIt(unittest.TestCase):
    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

    def test_1_letter_word(self):
        word = "I"
        out = no_meows.space(word)
        self.assertEqual(out, " ")

    def test_2_letter_word(self):
        word = "on"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "  ")

    def test_3_letter_word(self):
        word = "The"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "   ")

    def test_4_letter_word(self):
        word = "book"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "    ")

    def test_upper_4_letter_word(self):
        word = "BOOK"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "    ")

    def test_capped_4_letter_word(self):
        word = "Book"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "    ")

    def test_mixcapped_4_letter_word(self):
        word = "BooK"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "    ")

    def test_5_letter_word(self):
        word = "clock"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "     ")

    def test_6_letter_word(self):
        word = "whales"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "      ")

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = no_meows.space(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "             ")

    def test_line(self):
        line = "On the bus"
        out = no_meows.space_space(line, no_meows.space)
        self.assertEqual(out, "          ")

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = no_meows.space_space(line, no_meows.space)
        self.assertEqual(out, "          ?           .")


if __name__ == "__main__":
    unittest.main()

# End of file
