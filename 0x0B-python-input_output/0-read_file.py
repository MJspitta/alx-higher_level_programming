#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """ function that reads a text file and prints it """
    with open(filename, encoding="UTF8") as a_file:
        output = a_file.read()
        print(output)
