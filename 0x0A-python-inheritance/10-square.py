#!/usr/bin/python3
""" class inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits Rectangle """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size