#!/usr/bin/python3
""" Insert a line of text in file after specific string """


def append_after(filename="", search_string="", new_string=""):
    """ func that inserts line of text to a file after
    each line containing a specific string """
    with open(filename, 'r') as a_file:
        lines = a_file.readlines()

    with open(filename, 'w') as a_file:
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string + "\n")
