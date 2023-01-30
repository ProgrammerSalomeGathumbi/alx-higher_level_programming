#!/usr/bin/python3
"""
A module with a Rectangle class
"""


class Rectangle:
    """
    Class that represents a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with
        optional width and height values
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Delete a Rectangle instance and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol
        """
        if self.width == 0 or self.height == 0:
            return ""
        row = str(self.print_symbol) * self.width
        return "\n".join([row for i in range(self.height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the largest area
        between rect_1 and rect_2
        Raise TypeError if either rect_1 or rect_2
        are not instances of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @property
    def width(self):
        """
        Getter for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute
        Raise TypeError if value is not an integer
        Raise ValueError if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute
        Raise TypeError if value is not an integer
        Raise ValueError if value is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
