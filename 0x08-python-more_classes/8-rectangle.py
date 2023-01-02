#!/usr/bin/python3

class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        if(type(height) != int):
            raise TypeError("height must be integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if (type(width) != int):
            raise TypeError("width must be integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if(type(value) != int):
            raise TypeError("height must be integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width <= 0 or self.__height <= 0):
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        string = ""
        if (self.__height == 0 or self.__width == 0):
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string

    def __repr__(self):
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif(not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_2.area() > rect_1.area()):
                return (rect_2)
            else:
                return (rect_1)
