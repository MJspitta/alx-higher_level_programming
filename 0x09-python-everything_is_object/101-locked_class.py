#!/usr/bin/python3
""" prevents user from creating new instance attributes """


class LockedClass:
    """ a class that prevents user from dynamically creating
    new instance attributes """

    __slots__ = "first_name"
