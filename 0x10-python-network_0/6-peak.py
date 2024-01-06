#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If mid ele > next one, peak might be on the left side
            high = mid
        else:
            # If mid ele <= next one, a peak might be on the right side
            low = mid + 1

    # 'low' now points to a potential peak
    return list_of_integers[low]
