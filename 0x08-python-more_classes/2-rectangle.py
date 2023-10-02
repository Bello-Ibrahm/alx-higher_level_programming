#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by:
    (based on 1-rectangle.py)"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if not isinstance(value, int):
            msg = "width must be an integer"
            raise TypeError(msg)
        if (value < 0):
            msg = "width must be >= 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            msg = "height must be an integer"
            raise TypeError(msg)
        if (value < 0):
            msg = "height must be >= 0"
            raise ValueError(msg)
        self.__height = value

    def area(self):
        """ return the area of a rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ return the perimeter of a rectangle on success, 0 otherwise"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))
