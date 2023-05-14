"""
    Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
    Then the function needs to print the last 5 elements in the list.
"""


def squared_list():
    my_list = [value ** 2 for value in range(1, 21)]
    print(my_list[-5:])


squared_list()
