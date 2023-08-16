#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda line: list(map((lambda x: x * x), line))), matrix))
