#!/usr/bin/python3
""" crate object from JSON file """


import json


def load_from_json_file(filename):
    """ function that creates an object from a JSON file """
    with open(filename, 'r') as a_file:
        return json.loads(a_file.read())
