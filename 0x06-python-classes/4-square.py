#!/usr/bin/python3

""" Defines a square """


class Square:
    """ Defined a square """

    def __init__(self, size=0):
        """Instantiation of the sqaure class
        Args: size - size of the square
        Raises:
        TypeError: if size is not type int
        ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Defined property size
        Returns: size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Defined object area
        Returns: area of the class square
        """

        return (self.__size ** 2)
