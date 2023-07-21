#!/usr/bin/python3
""" first class Base """


import json
import csv
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string representation of list """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string representation of
        list_objs to a file """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dict)
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ return list of json string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attributes
        already set """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        else:
            dum = None
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ return a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                obj_dict = cls.from_json_string(json_data)
                return [cls.create(**obj_dic) for obj_dic in obj_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
            elif cls.__name__ == "Square":
                writer.writerow(["id", "size", "x", "y"])

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id, obj.width, obj.height, obj.x, obj.y
                        ])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                instances = []
                for row in reader:
                    data = [int(x) for x in row]
                    obj_dict = {}
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                                'id': data[0],
                                'width': data[1],
                                'height': data[2],
                                'x': data[3],
                                'y': data[4]
                                }
                    elif cls.__name__ == "Square":
                        obj_dict = {
                                'id': data[0],
                                'size': data[1],
                                'x': data[2],
                                'y': data[3]
                                }
                    instances.append(cls.create(**obj_dict))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")
        screen.setup(800, 600)

        t = turtle.Turtle()
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                t.forward(square.size)
                t.left(90)
        t.hideturtle()
        screen.mainloop()
