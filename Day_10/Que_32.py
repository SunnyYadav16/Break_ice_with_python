"""
    Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
    values are square of keys. The function should just print the keys only.
"""


def square_dict():
    my_dict = {val: val**2 for val in range(1, 21)}
    print(my_dict.keys())


square_dict()
