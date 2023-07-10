#!/usr/bin/python3
""" class that inherits from int """


class MyInt(int):
    """ Inverts the == and != operators """
    def __eq__(self, flip):
        return super().__ne__(flip)

    def __ne__(self, flip):
        return super().__eq__(flip)
