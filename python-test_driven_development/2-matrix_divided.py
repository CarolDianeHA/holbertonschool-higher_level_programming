#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    rowLenght = len(matrix[0])
    for row in matrix:
        if len(row) != rowLenght:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for value in row:
            if type(value) not in [int, float]:
                raise TypeError(message)
    return [[round((element/div), 2) for element in row] for row in matrix]
