#!/usr/bin/python3
"""This module contains a function validUTF8"""

import codecs


def validUTF8(data):
    """Checks whether a data set represents a valid
    utf-8 encoding"""
    try:
        codecs.decode(bytes(data), 'utf-8')
        return True
    except Exception:
        return False
