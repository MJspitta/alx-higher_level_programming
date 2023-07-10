#!/usr/bin/python3
""" check if object is instance of a class """


def is_same_class(obj, a_class):
    """ function returns True if object is exactly an
    instance of the specified class else False """
    return type(obj) == a_class
