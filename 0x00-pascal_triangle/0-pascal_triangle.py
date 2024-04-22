#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create function def pascal_triangle(n): that returns list of lists
    of integers representing Pascal’s triangle of n
    """
    # Checks if n is positive integer,
    # returns empty list if not
    if not isinstance(n, int) or n <= 0:
        return []

    # Initializes triangle with first row
    triangle = [[1]]

    # Generate subsequent rows starting from 2nd row to n-1
    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        # Iterate through elements except first and last
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
