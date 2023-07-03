#!/usr/bin/python3
""" Defines a rectangle """


class Rectangle:
    """ class of a rectangle
    Args:
        width: width of the rectangle
        height: height of the rectangle
    Raises:
        TypeError: if args are not integers
        ValueError: if args is less than 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return width of rectangle """
        return self.__width

    @width.setter
    def width(self, w):
        """ set width of rectangle """
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be >= 0")
        self.__width = w

    @property
    def height(self):
        """ return height of rectangle """
        return self.__height

    @height.setter
    def height(self, h):
        """ set height of rectangle """
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("height must be >= 0")
        self.__height = h
