#!/usr/bin/python3
""" This module contains a function island_perimeter """


def island_perimeter(grid):
    """ Calculates the perimeter of the connected islands """
    if grid is None:
        return None
    visited = set()

    def search(i, j):
        """ Recursively goes through each cell of land until
        it reaches out of bounds where it returns 1 """
        if (
            i >= len(grid) or j >= len(grid[0])
            or (i < 0) or (j < 0) or (grid[i][j] == 0)
        ):
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        perimeter = search(i, j + 1)
        perimeter += search(i + 1, j)
        perimeter += search(i, j - 1)
        perimeter += search(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return search(i, j)
    return 0
