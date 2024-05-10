#!/usr/bin/python3
"""This module contains a function validUTF8"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Checks whether a data set represents a valid
    utf-8 encoding"""
    num_next = 0
    for byte in data:
        if num_next == 0:
            if byte >> 7 == 0b0:  # single byte character
                continue
            elif byte >> 5 == 0b110:  # two byte character
                num_next = 1
            elif byte >> 4 == 0b1110:  # three byte character
                num_next = 2
            elif byte >> 3 == 0b11110:  # four byte character
                num_next = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False  # not a continuation byte
            num_next -= 1
    return num_next == 0
