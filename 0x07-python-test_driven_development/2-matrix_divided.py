#!/usr/bin/python3
"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    if not matrix or \
       not isinstance(matrix, list) or \
       not all(isinstance(i, list) for i in matrix) or \
       not all(len(j) == len(matrix[0]) for j in matrix) or \
       not all(isinstance(k, (int, float)) for i in matrix for k in i):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        msg = "div must be a number"
        raise TypeError(msg)

    if div != div:  # Check for NaN without using math.isnan()
        msg = "div must not be NaN"
        raise ValueError(msg)

    if div == 0:
        msg = "division by zero"
        raise ZeroDivisionError(msg)

    new_m = [[round(j / div, 2) for j in i] for i in matrix]
    return new_m
