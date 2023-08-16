#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, each_line))for each_line in matrix]
