#!/usr/bin/python3
"""
This module writes a class Square that defines a square
It has a Private instance attribute: size
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
