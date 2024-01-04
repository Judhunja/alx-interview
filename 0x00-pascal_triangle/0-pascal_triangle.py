#!/usr/bin/python3
"""This module contains a function pascal_triangle."""


def pascal_triangle(n):
    """Return pascal's triangle of n as a list of integers."""
    if (n <= 0):
        return []

    ans = [[1]]

    for i in range(n - 1):
        new = [0] + ans[-1] + [0]
        row = []
        for j in range(len(ans) + 1):
            row.append(new[j] + new[j + 1])
        ans.append(row)

    return ans
