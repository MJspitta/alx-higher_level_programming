#!/usr/bin/python3
""" append to a file """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file
    and returns number of characters added """
    with open(filename, "a", encoding="UTF8") as a_file:
        app_end = a_file.write(text)
        return app_end
