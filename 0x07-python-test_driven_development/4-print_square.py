#!/usr/bin/python3
"""Write a function that prints a square with the character #
"""


def print_square(size):
    """prints a square with #

    Args:
       size (int): size of the square

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: size must be >=0
        TypeError: size must be an int

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
