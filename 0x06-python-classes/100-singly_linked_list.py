#!/usr/bin/python3
""" Defines a node of a singly linked list """


class Node:
    """ Class of a node """

    def __init__(self, data, next_node=None):
        """ Initialize class Node
        Args:
            data: data value for linked list
            next_node: Node object
        Raises:
            TypeError: if data is not integer or next_node not Node object
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve data """

        return self.__data

    @data.setter
    def data(self, value):
        """ Set data """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next_node """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set next_node """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class of singly linked list """

    def __init__(self):
        self.head = None

    def __str__(self):
        finalstr = ""
        currvar = self.head
        while currvar:
            finalstr += str(currvar.data) + "\n"
            currvar = currvar.next_node
        return finalstr.rstrip("\n")

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            currvar = self.head
            while currvar.next_node and value >= currvar.next_node.data:
                currvar = currvar.next_node
            new_node.next_node = currvar.next_node
            currvar.next_node = new_node
