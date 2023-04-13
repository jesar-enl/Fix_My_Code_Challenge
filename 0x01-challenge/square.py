#!/usr/bin/python3
"""Module contains the Square class"""

class Square():
    """`Square` class showing the `area` and `perimeter` functions"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the variables"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width ** 2

    def PermiterOfMySquare(self):
        """ Perimeter of the square"""
        return (4 * self.width)

    def __str__(self):
        """String representation of the Square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
