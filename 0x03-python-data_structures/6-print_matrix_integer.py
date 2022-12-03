#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    o_loop = len(matrix)
    for item in matrix:
        for subitem in range(0, len(item)):
            if subitem < len(item) - 1:
                print("{:d}".format(item[subitem]), end=" ")
            else:
                print("{:d}".format(item[subitem]), end="")
        print("")
