#!/usr/bin/python3
"""Defines a class rectanglr and calculates area and perimeter"""


class Rectangle:
    """
    A class used to represent a rectangle

    Attributes
    ----------
    width : int
        integer representing the width of the rectangle
    height : int
        the height of the rectangle

    Methods
    -------
    area()
        returns the area of the rectangle
    perimiter()
        returns the perimeter
    """

    def __init__(self, width=0, height=0):
        """
        If the arguments are not passed, default are used

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectange (default is 0)
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectanglr"""
        # if either measurement is 0, return 0
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using '#' characters

        If either the width or height is 0, an empty string is returned.
        The string representation consists of rows of '#' characters, forming
        the visual appearance of a rectangle, with rows separated by newline
        characters.
        """

        rec_str = ""

        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rec_str += "#" * self.__width + "\n"

        return rec_str
