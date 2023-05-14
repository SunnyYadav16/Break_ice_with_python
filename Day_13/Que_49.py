"""
    Define a class named Shape and its subclass Square. The Square class has an init function which takes a
    length as argument. Both classes have an area function which can print the area of the shape where Shape's area
    is 0 by default.
"""


class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def calculate_area(self):
        return self.length * self.length


square_obj = Square(5)
print(square_obj.calculate_area())

print(Square().calculate_area())
