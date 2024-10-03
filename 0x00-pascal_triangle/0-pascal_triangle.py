#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing the first n rows of Pascal's triangle.
    """
    triangle = []
    for i in range(1, n+1):
        row = []
        C = 1
        for j in range(1, i+1):
            row.append(C)
            C = C * (i - j) // j
        triangle.append(row)
    return triangle