#!/usr/bin/python3
""" add new attribute to an object """


def add_attribute(obj, attr, val):
    """ func that adds a new attribute to the object
    if it is possible """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
