#!/usr/bin/python3
""" checks if object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """ function returns True if obj is an instance
    or returns False """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
