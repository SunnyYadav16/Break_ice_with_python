"""
    Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20
     (both included).
"""


def squared_list():
    my_list = [value ** 2 for value in range(1, 21)]
    print(tuple(my_list))


squared_list()
