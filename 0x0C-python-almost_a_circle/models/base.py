#!/usr/bin/python3
""" first class Base """


import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string representation of list """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string representation of
        list_objs to a file """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(json_str)
