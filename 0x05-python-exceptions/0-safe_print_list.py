#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ele_count = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            ele_count += 1
        except BaseException:
            break
    print()
    return (ele_count)
