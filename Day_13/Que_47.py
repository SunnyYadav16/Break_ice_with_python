"""
    Define a class named Circle which can be constructed by a radius. The Circle class has a method which can 
    compute the area.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


circle_obj = Circle(2)
print(circle_obj.calculate_area())
