#!/usr/bin/python3
""" Defines square """


class Square:
    """ Class of a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the class square
        Args:
            size: size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieve size of the square """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieve position of the square """

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Area of square
        Returns:
            The current square area
        """

        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size + self.__position[0]):
                for j in range(self.__size + self.__position[1]):
                    if i >= self.__position[0] and j >= self.__position[1]:
                        print("#", end="")
                print()
