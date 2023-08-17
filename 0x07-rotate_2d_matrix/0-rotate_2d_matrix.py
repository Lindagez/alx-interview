#!/usr/bin/python3
"""
rotate a matrix solution
"""


def rotate_2d_matrix(matrix):
    """rotate by transposing and reversing the cols and rows"""
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for r in range(len(matrix)):
        matrix[r].reverse()
