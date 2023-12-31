#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py):
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """

    def __init__(self, size):
        """initializes Square

        Attributes:
            self.__size: size of one side of the square

        Args:
            size: size of one side of the square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
