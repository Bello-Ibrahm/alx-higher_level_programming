#!/usr/bin/python3
"""Class that inherits from list """


def inherits_from(obj, a_class):
    """function"""
    result = isinstance(obj, a_class) and type(obj) is not a_class
    return result
