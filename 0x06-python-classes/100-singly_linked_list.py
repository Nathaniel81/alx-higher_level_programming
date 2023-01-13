#!/usr/bin/python3

"""
Doc
"""


class Node():
    """
    Defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrives the value of attribute data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the value of the attribute data.
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Retrives the value of attribute next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of the attribute next_node.
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """
    Defines a singly linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to the singly linked list.
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            traverse = self.__head
            while (traverse.next_node is not None and
                    traverse.next_node.data < value):
                traverse = traverse.next_node

            new_node.next_node = traverse.next_node
            traverse.next_node = new_node

    def __repr__(self):
        """
        Prints representation of the singly linked list with magic
        method __repr__.
        """
        traverse = self.__head
        numbers = []

        while traverse is not None:
            numbers.append(str(traverse.data))
            traverse = traverse.next_node

        return ('\n'.join(numbers))
