#!/usr/bin/python3
""" This module contains a function rotate_2d_matrix """


def rotate_2d_matrix(matrix):
    """ Rotate matrix in place by 90 degrees
    clockwise """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(left, right):
            top, bottom = left, right
            topleft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topleft
            right -= 1
            left += 1
