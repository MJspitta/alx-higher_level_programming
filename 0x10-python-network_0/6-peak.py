#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """finds peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    nlen = len(list_of_integers)

    l, r = 0, nlen - 1
    while l < r:
        m = l + (r - l) // 2
        if list_of_integers[m] > list_of_integers[m + 1]:
            r = m
        else:
            l = m + 1

    return list_of_integers[l]
