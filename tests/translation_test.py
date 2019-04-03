"""Tests of translation methods."""

import unittest
from sudoku.core import translation


class TestTranslationMethods(unittest.TestCase):
    """Test the translation methods."""

    def test_numbers_to_game(self):
        """Test numbers_to_game."""
        self.assertEqual(
            translation.numbers_to_game([0, 5, 0, 0, 0, 4, 0, 0, 0,
                                         3, 0, 0, 0, 0, 0, 1, 0, 0,
                                         0, 8, 1, 3, 0, 0, 4, 5, 0,
                                         5, 0, 0, 9, 6, 0, 0, 0, 4,
                                         0, 3, 6, 0, 0, 8, 0, 0, 0,
                                         0, 4, 0, 0, 0, 3, 2, 0, 0,
                                         0, 0, 0, 0, 8, 0, 6, 0, 0,
                                         0, 6, 0, 2, 5, 0, 3, 0, 9,
                                         0, 0, 0, 0, 0, 1, 0, 2, 0]),
            [[0, 5, 0, 0, 0, 4, 0, 0, 0],
             [3, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 8, 1, 3, 0, 0, 4, 5, 0],
             [5, 0, 0, 9, 6, 0, 0, 0, 4],
             [0, 3, 6, 0, 0, 8, 0, 0, 0],
             [0, 4, 0, 0, 0, 3, 2, 0, 0],
             [0, 0, 0, 0, 8, 0, 6, 0, 0],
             [0, 6, 0, 2, 5, 0, 3, 0, 9],
             [0, 0, 0, 0, 0, 1, 0, 2, 0]])
