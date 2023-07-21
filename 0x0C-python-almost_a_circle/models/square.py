#!/usr/bin/python3
""" contains a square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return custom string representation """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, val):
        """ set size """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        attrib = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attrib):
                    setattr(self, attrib[i], arg)
        else:
            for key, val in kwargs.items():
                if key in attrib:
                    setattr(self, key, val)
