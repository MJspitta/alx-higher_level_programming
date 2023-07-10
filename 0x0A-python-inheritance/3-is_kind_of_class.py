#!/usr/bin/python3
""" checks if object is instance of or if the object is
an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if object is an instance
    or False if not """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
