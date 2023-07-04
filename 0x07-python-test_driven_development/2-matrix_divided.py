#!/usr/bin/python3
""" divide a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    if not isinstance(matrix, list) or any(not isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rowlen = len(matrix[0])
    if any(len(rw) != rowlen for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for rw in matrix:
        row_value = [round(i / div, 2) for i in rw]
        new_matrix.append(row_value)
    return new_matrix
