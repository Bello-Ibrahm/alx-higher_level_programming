#!/usr/bin/python3

class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is an integer greater than 0

        Args:
            name: name of the value
            value: value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initializes a Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """

    def __init__(self, size):
        """ Initializes a Square

        Args:
            size: size of one side of the square
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Returns the string representation of the square """
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    s = Square(5)
    print(s)
    print(s.area())
