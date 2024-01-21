#!/usr/bin/python3
""" This module contains a function minOperations. """
import math


def minOperations(n: int) -> int:
    """
    In a text file, there is a single character H.

    Your text editor can execute only two operations in this file:
    Copy All and Paste.
    This method calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n % 2 == 0 and n % 3 != 0:
        return math.floor(math.sqrt(n)) + 2
    elif n % 2 == 0:
        return math.floor(math.sqrt(n)) + 4
    else:
        return math.floor(math.sqrt(n)) + 3
