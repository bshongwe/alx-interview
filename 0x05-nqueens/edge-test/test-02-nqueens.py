#!/usr/bin/python3
"""
Test Module 2: N queens solution finder.
"""
import unittest
from subprocess import check_output, CalledProcessError


class TestNQueens(unittest.TestCase):
    """
    Unittests for N queens solution finder
    """
    def test_solve_nqueens(self):
        """Test case for N = 4
        """
        output_4 = self.run_program_with_input("4")
        expected_4 = [
            [[0, 1], [1, 3], [2, 0], [3, 2]],
            [[0, 2], [1, 0], [2, 3], [3, 1]]
        ]
        self.assertListEqual(output_4, expected_4)

        """Test case for N = 6
        """
        output_6 = self.run_program_with_input("6")
        expected_6 = [
            [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]],
            [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]],
            [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]],
            [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
        ]
        self.assertListEqual(output_6, expected_6)

        """Test case for N = 1
        """
        try:
            output_1 = self.run_program_with_input("1")
            expected_1 = [[[0, 0]]]
            self.assertListEqual(output_1, expected_1)
        except CalledProcessError as e:
            self.fail(f"An error occurred while running the program for N = 1: {e}")

    def run_program_with_input(self, input_val):
        try:
            output = check_output(["./0-nqueens.py", input_val]).decode("utf-8").strip()
            return self.parse_output(output)
        except CalledProcessError as e:
            raise e
        except Exception as e:
            self.fail(f"An error occurred while running the program: {e}")

    def parse_output(self, output):
        solutions = []
        for line in output.split('\n'):
            solution = eval(line.strip())
            solutions.append(solution)
        return solutions


if __name__ == '__main__':
    unittest.main()
