#!/usr/bin/python3

# class Rectangle that defines a rectangle by:
# (based on 0-rectangle.py)
"""
    define a class 'Rectangle'
"""


class Rectangle:
    """
        rectangle with private instance attributes: 'width' & 'height'
    """

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """
            get the width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            Modifies the width of the rectangle

            Args:
                 value (int): the new width of the rectangle
        """

        if (type(value) != int):
            raise TypeError("width must be integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            get the height of the rectangle
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
            Modifies the height of the rectangle

            Args:
                 value (int): the new width of the rectangle
        """

        if (type(value) != int):
            raise TypeError("height must be integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
