#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """finds peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    nlen = len(list_of_integers)

    low, high = 0, nlen - 1
    while low < high:
        mid = low + (high - low) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
