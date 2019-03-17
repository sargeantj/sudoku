"""Unit tests of the Game."""


import unittest
import game as gm


class TestGameMethods(unittest.TestCase):
    """TestGameMethods extends methods in the game file."""

    def test_check_list(self):
        """Test of check_list."""
        self.assertTrue(gm.check_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertTrue(gm.check_list([1, 0, 3, 0, 0, 6, 0, 8, 9]))
        self.assertFalse(gm.check_list([1, 1, 0, 0, 0, 0, 0, 0, 3]))

    def test_zero_check(self):
        """Test of zero_check."""
        self.assertEqual(gm.zero_check([
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]), 0)
        self.assertEqual(gm.zero_check([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]), 81)

        self.assertEqual(gm.zero_check([
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]), 63)


class TestGameOfSudoku(unittest.TestCase):
    """Test a game of Sudoku."""

    def test_full_process(self):
        """Test the full process works."""
        self.assertEqual(
            gm.GameOfSudoku([[8, 0, 0, 4, 0, 0, 6, 0, 1],
                             [2, 0, 0, 6, 0, 5, 8, 4, 0],
                             [0, 0, 0, 0, 0, 0, 0, 5, 0],
                             [0, 0, 6, 5, 4, 0, 0, 0, 8],
                             [5, 0, 0, 0, 0, 0, 0, 1, 0],
                             [0, 0, 1, 8, 2, 0, 0, 0, 3],
                             [0, 0, 0, 0, 0, 0, 0, 9, 0],
                             [6, 0, 0, 1, 0, 8, 4, 7, 0],
                             [3, 0, 0, 9, 0, 0, 1, 0, 5]]).complete,
            [[8, 7, 5, 4, 9, 2, 6, 3, 1],
             [2, 9, 3, 6, 1, 5, 8, 4, 7],
             [1, 6, 4, 7, 8, 3, 2, 5, 9],
             [9, 3, 6, 5, 4, 1, 7, 2, 8],
             [5, 8, 2, 3, 7, 6, 9, 1, 4],
             [7, 4, 1, 8, 2, 9, 5, 6, 3],
             [4, 1, 8, 2, 5, 7, 3, 9, 6],
             [6, 5, 9, 1, 3, 8, 4, 7, 2],
             [3, 2, 7, 9, 6, 4, 1, 8, 5]])


if __name__ == '__main__':
    unittest.main()
