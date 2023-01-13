#!/usr/bin/python3
"""
Doc
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        hold = triangle[-1]
        inside = [1]
        for i in range(len(hold) - 1):
            inside.append(hold[i] + hold[i + 1])
        inside.append(1)
        triangle.append(inside)
    return triangle
