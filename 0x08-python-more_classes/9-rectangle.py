#!/usr/bin/python3
"""Write a class Rectangle that defines
a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """class Rectangle

    Attributes:
        number_of_instances (int): total number of instances
        print_symbol (str): the symbol the rectangle will be printed with

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor

        Args:
           width (int, optional): the width of the rectangle
           height (int, optional): the height of the rectangle

        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width

        Args:
           width (int, optional): the width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is not >= 0

        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter for height
        """
        return (self.__height)

    @height.setter
    def height(self, height):
        """setter for height

        Args:
           height (int, optional): the height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is not >= 0

        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    # @print_symbol.setter
    # def print_symbol(self, print_symbol):
    #     """setter for print_symbol

    #     Args:
    #        print_symbol (str): the print_symbol

    #     """
    #     self.print_symbol = print_symbol

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle

        """
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle

        If either width or height is 0, returns 0

        Returns:
            int: the perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """returns the rectangle with #'s

        Returns:
            str: the rectangle with #'s or empty string width or height = 0

        """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return (rec)
        for h in range(self.__height):
            for w in range(self.__width):
                rec += str(self.print_symbol)
            if h < self.__height - 1:
                rec += "\n"
        return (rec)

    def __repr__(self):
        """returns a string for recreating the rectangle

        Returns:
            str: a string for recreating the rectangle

        """
        return ("Rectangle("+str(self.__width)+", "+str(self.__height)+")")

    def __del__(self):
        """destructor for Rectangle

        Prints 'Bye rectangle…'
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
           rect_1 (Rectangle): rectangle 1
           rect_2 (Rectangle): rectangle 2

        Returns:
            (Rectangle): the biggest rectangle of the two

        Raises:
            TypeError: If either rect isn't a rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """creates a rectangle of with equal width and height

        Args:
           size (int, optional) (default 0): size of the square

        Returns:
            Rectangle: width and height = size

        """
        return Rectangle(size, size)
