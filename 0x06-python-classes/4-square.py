#!/usr/bin/python3
"""
This module writes a class Square that defines a square

"""


class Square:
    """
        This class defines a square by its size.
    """
    def __init__(self, size=0):
        """
            Initialize the square with an optional size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size

    def area(self):
        """
            Return the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute
        Args:
            value (int): The new size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
