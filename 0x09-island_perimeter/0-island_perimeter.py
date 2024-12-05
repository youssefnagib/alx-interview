#!/usr/bin/python3
from typing import List
"""
This module contains a function that calculates
the perimeter of an island in a grid.
"""


def island_perimeter(grid: List[List]):
    """
    Calculates the perimeter of an island in a grid.

    Args:
    grid (List[List[int]]): A 2D grid representing the island.
    """
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == row - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == col - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
