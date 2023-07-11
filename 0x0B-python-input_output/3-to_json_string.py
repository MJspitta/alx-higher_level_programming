#!/usr/bin/python3
""" JSON representation of object """


import json


def to_json_string(my_obj):
    """ function that returns JSON representation
    of an object string """
    return json.dumps(my_obj)
