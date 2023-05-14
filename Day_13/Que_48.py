"""
    Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method 
    which can compute the area.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.width * self.length


rectangle = Rectangle(3, 4)
print(rectangle.calculate_area())
