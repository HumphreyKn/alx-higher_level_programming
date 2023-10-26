#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """
    defines a square class with private attribute size
    Checks the datatype and value
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
