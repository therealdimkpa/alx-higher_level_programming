#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = matrix[:]
   
    for item in range(0, len(n_matrix)):
        for subitem in range(0, len(n_matrix[item])):
            n_matrix[item][subitem] = n_matrix[item][subitem] ** 2

    return (n_matrix)
