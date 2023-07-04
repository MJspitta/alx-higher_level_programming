#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """ function that prints text with 2 new lines
    after each of these characters ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    for c in text:
        output += c
        if c in ".?:":
            output += "\n\n"

    print(output.rstrip())
