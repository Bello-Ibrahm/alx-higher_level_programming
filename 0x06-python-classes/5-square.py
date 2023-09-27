#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""
class Square:
    """a class Square"""

    def __init__(self, size=0):
        """Class constructor"""
        self.size = size

    def area(self):
        """Function that return area of a square"""
        return (self.size**2)

    @property
    def size(self):
        """Getter function
        Returns:
            int: self.__size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function

        Args:
            value (int, optional): Size of the square

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

    def my_print(self):
        """Prints the square to stdout using #'s
        """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if not self.size:
            print()
