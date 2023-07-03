#!/usr/bin/python3

"""Class defining Rectangle"""


class Rectangle:
    """class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __del__(self):
        """Delete instance"""
        print("Bye Rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Get attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Set print behaviour"""
        if self.__width == 0 or self.__height == 0:
            return ""
        pri = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pri

    def __repr__(self):
        """String Rep to recreate new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
