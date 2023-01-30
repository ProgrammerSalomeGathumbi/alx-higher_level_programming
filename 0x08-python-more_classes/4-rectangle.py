#!/usr/bin/python3
"""
This is a  rectangle module
"""


class Rectangle:
    """
    Rectangle Class: defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height
        :param width: width of the rectangle (default 0)
        :param height: height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter for the width
        :return: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the width
        :param value: new width value
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the height
        :return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height
        :param value: new height value
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        :return: rectangle area (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the rectangle perimeter
        :return: rectangle perimeter (2 * (width + height))
        or 0 if width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        returns a string representation of the rectangle using #
        :return: string representation of the rectangle
        or an empty string if width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return ""
        row = "#" * self.width + "\n"
        return row * self.height

    def __repr__(self):
        """
        returns a string representation of the rectangle
        that can be used to recreate the object
        :return: string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)
