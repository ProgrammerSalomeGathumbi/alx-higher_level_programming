#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""


class Rectangle:
    """
    Defines a rectangle with private attributes `width` and `height`
    and methods for setting and retrieving the values of the attributes.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional `width` and `height` values.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Get the current value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of height.
        Raises a TypeError if `value` is not an integer,
        and raises a ValueError if `value` is less than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Get the current value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of width.
        Raises a TypeError if `value` is not an integer,
        and raises a ValueError if `value` is less than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
