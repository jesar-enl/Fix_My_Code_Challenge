#!/usr/bin/python3
"""Module contains the Square class"""


class Square():
    """`Square` class showing the `area` and `perimeter` functions"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """Initialize the variables"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return (self.__width * self.__height)

    def perimeter_of_my_square(self):
        """ Perimeter of the square"""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """String representation of the Square"""
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
