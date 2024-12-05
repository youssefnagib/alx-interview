# 0x09. Island Perimeter

This project focuses on calculating the perimeter of an island described in a grid. The grid is a rectangular list of lists, where each element represents either water (`0`) or land (`1`). The task is to compute the perimeter of the island formed by the land (`1`).

## Problem Description

The grid represents a map where:
- **0** represents water.
- **1** represents land.

Each cell is square with a side length of 1. Cells are connected horizontally or vertically (not diagonally). The grid is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water, and there is only one island (or nothing). The island doesn’t have “lakes” (water inside the island that isn't connected to the surrounding water).

The function `island_perimeter(grid)` calculates the perimeter of the island.

## Requirements

- The grid is represented as a list of lists of integers.
- The island is formed by adjacent `1`s in the grid, either horizontally or vertically.
- The perimeter is the total number of edges of the land cells that are adjacent to water or are on the boundary of the grid.

## Function Prototype

```python
def island_perimeter(grid):
    pass
