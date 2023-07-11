#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    dictionary = {}
    for attr in obj.__dict__:
        val = getattr(obj, attr)
        if isinstance(val, (list, dict, str, int, bool)):
            dictionary[attr] = val
    return dictionary
