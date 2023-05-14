"""
    Define a class, which have a class parameter and have a same instance parameter.
"""


class Car:
    name = "Car"

    def __init__(self, name=None):
        self.name = name


mercedes_obj = Car(name="Mercedes")
print(mercedes_obj.name)
