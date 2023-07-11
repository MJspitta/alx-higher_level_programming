#!/usr/bin/python3
""" defines a student """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            attrs = self.__dict__.keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]
        sdict = {attr: getattr(self, attr) for attr in attrs}
        return sdict

    def relooad_from_json(self, json):
        for attr, val in json.items():
            setattr(self, attr, val)
