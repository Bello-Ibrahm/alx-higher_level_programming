#!/usr/bin/python3
"""Class that inherits from list """


class MyList(list):
    """inherited class MyList"""

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
