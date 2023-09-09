#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in matrix:
        for ele in idx:
            print(ele, end=' ')
            if(ele is not idx[len(idx)-1]):
                print(" ", end="")
        print()
