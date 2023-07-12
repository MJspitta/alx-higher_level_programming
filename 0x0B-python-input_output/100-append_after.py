#!/usr/bin/python3
""" Insert a line of text in file after specific string """


def append_after(filename="", search_string="", new_string=""):
    """ func that inserts line of text to a file after
    each line containing a specific string """
    lines = []
    with open(filename, 'r') as a_file:
        for line in a_file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as a_file:
        a_file.writelines(lines)
