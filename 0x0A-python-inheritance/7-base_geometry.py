#!/usr/bin/python3
"""Task 7"""


class BaseGeometry:
    """ Geometry Class """

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as an integer"""
        if type(value) != int:
            msg = "{:s} must be an integer".format(name)
            raise TypeError(msg)
        if value <= 0:
            msg = "{:s} must be greater than 0".format(name)
            raise ValueError(msg)
