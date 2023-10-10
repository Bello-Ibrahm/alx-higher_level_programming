#!/usr/bin/python3
"""Comments"""


def write_file(filename="", text=""):
    """ function that returns the number of lines of a text file """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
