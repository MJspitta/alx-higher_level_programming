#!/usr/bin/python3
""" Save object to a file """


import json


def save_to_json_file(my_obj, filename):
    """ function writes an object to a text file using
    JSON representation """
    with open(filename, 'w') as a_file:
        json.dump(my_obj, a_file)
