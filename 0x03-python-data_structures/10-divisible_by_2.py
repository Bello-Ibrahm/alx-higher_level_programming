#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_List = []
    for x in my_list:
        if (x % 2 == 0):
            new_List.append(True)
        else:
            new_List.append(False)
    return (new_List)
