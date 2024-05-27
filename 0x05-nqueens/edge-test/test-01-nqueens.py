#!/usr/bin/python3
"""
Test Module for N queens solution finder
"""
import unittest
from subprocess import check_output


class TestNQueens(unittest.TestCase):
    """Unittest for N Queens Solver
    """
    def test_solve_nqueens(self):
        """Test case for N = 4
        """
        output_4 = check_output(["./0-nqueens.py", "4"]).decode("utf-8").strip()
        expected_4 = "[[0, 1], [1, 3], [2, 0], [3, 2]]\n[[0, 2], [1, 0], [2, 3], [3, 1]]"
        self.assertEqual(output_4, expected_4)


        """Test case for N = 6
        """
        output_6 = check_output(["./0-nqueens.py", "6"]).decode("utf-8").strip()
        expected_6 = (
            "[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]\n"
            "[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]\n"
            "[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]\n"
            "[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]"
        )
        self.assertEqual(output_6, expected_6)


if __name__ == "__main__":
    """Calls main function
    """
    unittest.main()
