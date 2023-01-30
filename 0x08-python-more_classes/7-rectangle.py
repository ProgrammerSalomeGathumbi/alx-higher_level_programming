#!/usr/bin/python3
"""
A module with a Rectangle class
"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints message when rectangle instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle with value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of rectangle with value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of rectangle"""
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Returns string representation of rectangle
           that can be used to recreate instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
