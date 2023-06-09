#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Class of a square """

    def __init__(self, size=0):
        """ Initialize the class square
        Args:
            size - size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
