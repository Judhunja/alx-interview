#!/usr/bin/python3
"""This module contains a function canUnlockAll."""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    You have n locked boxes. Each box is labelled from 0 to n-1.
    Each box may contain keys to other boxes.
    """
    keys = boxes[0]  # all the keys in the first box
    openedboxes = [boxes[0]]  # a list of lists with the boxes we have opened
    opened = [0]  # the number(index) of boxes we have opened

    for key in keys:
        if key < len(boxes) and key not in opened:
            opened.append(key)  # number of key = number of opened box
            openedboxes.append(boxes[key])  # add this box to the opened boxes
            keys.extend(boxes[key])  # add all the keys in the opened box

    return len(openedboxes) == len(boxes)
    # same number in the opened boxes as in the original number of boxes
    # indicates that all the boxes have been opened
