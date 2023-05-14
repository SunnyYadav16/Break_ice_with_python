"""
    Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and 
    the values are square of keys.
"""


def square_dict():
    my_dict = {val: val**2 for val in range(1, 21)}
    print(my_dict)


square_dict()
