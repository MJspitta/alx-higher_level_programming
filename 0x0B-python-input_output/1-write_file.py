#!/usr/bin/python3
""" write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    and returns number of characters written """
    with open(filename, "w", encoding="UTF8") as a_file:
        in_put = a_file.write(text)
        return in_put
