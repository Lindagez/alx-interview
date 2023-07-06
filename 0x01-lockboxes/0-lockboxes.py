#!/usr/bin/python3
"""Module gets true key
"""


def canUnlockAll(boxes):
    """Function to check boxes contain
    all valid keys"""
    opened_box = [0]
    for i in opened_box:
        for j in boxes[i]:
            if j >= 0 and j < len(boxes) and j not in opened_box:
                opened_box.append(j)
    return len(opened_box) == len(boxes)
