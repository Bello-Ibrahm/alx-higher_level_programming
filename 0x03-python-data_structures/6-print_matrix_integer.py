#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in matrix:
        space = ""
        for ele in idx:
            print("{:s}{:d}".format(space, ele), end="")
            space = " "
        print()
