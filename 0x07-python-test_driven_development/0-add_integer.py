#!/usr/bin/python3
"""Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a
TypeError exception with the message a must be an
integer or b must be an integer

a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    Args are a and b, and they can be int or float
    If Args are invalid type, a TypeError is raised"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
