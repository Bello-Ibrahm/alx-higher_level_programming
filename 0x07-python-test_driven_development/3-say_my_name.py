#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """prints Y

    Args:
       first_name (str): First name
       last_name (str) (default ""): Last name

    Raises:
        TypeError: if one or the other isn't a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
