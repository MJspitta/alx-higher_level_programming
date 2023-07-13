#!/usr/bin/python3
""" checks if object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """ function returns True if obj is an instance
    or returns False """
    if a_class in type(obj).__mro__[1:]:
        return True
    else:
        return False
