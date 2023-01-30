#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function takes 2 integers/floats as input and adds them .

    Inputs:
    a: an integer or float.
    b: an integer or float, default value is 98.

    Output:
    An integer, the addition of the two integers.

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a+b
