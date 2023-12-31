#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """ Class Square that defines methods and attributes for a square object
    - Write a class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """ Class Constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
