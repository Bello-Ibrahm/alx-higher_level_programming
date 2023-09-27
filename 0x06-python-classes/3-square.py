#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
"""


class Square:
    """a class Square"""

    def __init__(self, size=0):
        """The class constructor

        Args:
            size (int): Size of the square

        Raises:
            AttributeError: If size isn't an integer
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ function that compute area of square

        Returns:
            int: the square of the size
        """
        return (self.__size**2)
