#!/usr/bin/python3
""" class that inherits from list """


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ prints a sorted list """
        sort_list = sorted(self)
        print(sort_list)
