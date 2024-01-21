#!/usr/bin/python3
""" This module contains a function minOperations. """


def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.

    Your text editor can execute only two operations in this file:
    Copy All and Paste.
    This method calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    min_ops = 0
    length = 1
    copy_all = 0

    while length < n:
        # it is necessary to perform Copy all
        # if n is divisible by length
        if (n % length) == 0:
            # length is the number of 'h' characters in the file
            copy_all = length
            min_ops += 1
        length += copy_all
        min_ops += 1

    return min_ops
