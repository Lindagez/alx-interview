#!/usr/bin/python3
"""A module to find the minimun operations
to deplicate H n times"""


def minOperations(n):
    """A function returns a number of
    operations taken to get H n time"""
    "number of H's"
    nh = 1
    "previous copied number of H's"
    copied = 0
    "number of operations"
    nop = 0

    while (nh < n):
        "remainder as rem"
        rem = n - nh
        if (rem % nh == 0):
            "copy the current value"
            copied = nh
            "past the current value"
            nh += copied
            "copy and past are the two operations"
            nop += 2
        else:
            "pass the previous value"
            nh += copied
            "pass is the only operation 1"
            nop += 1
    return nop
