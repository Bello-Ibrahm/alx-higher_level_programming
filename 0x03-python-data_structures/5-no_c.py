#!/usr/bin/python3
def no_c(my_string):
    no_c_and_C = [char for char in my_string if char not in ('c', 'C')]
    return (''.join(no_c_and_C))
