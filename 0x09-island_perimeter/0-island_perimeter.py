#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter (p) of an island with no lakes.
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter (p) of the island
    """
    p = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            p += sum(edges)
    return p
