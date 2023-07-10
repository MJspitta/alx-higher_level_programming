#!/usr/bin/python3
""" empty class BaseGeometry """


class BaseGeometry():
    """ BaseGeometry class """

    def area(self):
        """ public instance method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method integer_validator """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
