#!/usr/bin/python3
"""inherited class MyList"""


class MyList(list):
    """inherited class MyList"""
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        temp = list(self)
        temp.sort()
        print(temp)
