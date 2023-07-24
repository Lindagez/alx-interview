#!/usr/bin/python3
"""Module makes a pasical triagle
"""


def pascal_triangle(n):
    """Function return n rows of pasical tri
    """
    if n <= 0:
        return []
    tri_list = [[1]]
    for j in range(n - 1):
        tri_list.append([1] + [tri_list[j][i] + tri_list[j][i + 1]
                        for i in range(len(tri_list[j]) - 1)] + [1])
    return tri_list
