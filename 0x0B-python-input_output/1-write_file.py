#!/usr/bin/python3
"""Comments"""


def number_of_lines(filename=""):
    """ function that returns the number of lines of a text file """

    with open(filename) as myfile:
        lines = myfile.readlines()
    return (len(lines))
