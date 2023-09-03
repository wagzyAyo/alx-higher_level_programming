#!usr/bin/python3
"""This module divides element in a list
(matrix)"""


def matrix_divided(matrix, div):
    """This function divides elemnt in a
    list by a given number

    Args:
    matrix: list of elements int or floats
    div: number to be use for division

    raise:
    TypeError : if the matrix doesnt contain int or float
    TypeError : if rows contains different sizes
    TypeError : if div is not a n int or float
    ZeroDivisionError: if div is 0


    Return:
    a new matrix with the result of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(float, div):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row))for row in matrix])
