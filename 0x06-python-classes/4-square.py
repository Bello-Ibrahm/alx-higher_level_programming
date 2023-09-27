#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
        You are not allowed to import any module
"""


class Square:
    """a class Square

    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size=0):
        """The class constructor

        Args:
            size (int, optional): Size of the square
        """
        self.size = size

    def area(self):
        """Function that returns the area of a square"""
        return (self.size**2)

    @property
    def size(self):
        """Getter function"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function

        Raises:
            AttributeError: If value isn't an integer
            ValueError: If value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
