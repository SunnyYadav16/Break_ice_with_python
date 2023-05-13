"""
    Define a class which has at least two methods:

    getString: to get a string from console input
    printString: to print the string in upper case.
    Also, please include simple test function to test the class methods.

    Hints:
    Use init method to construct some parameters
"""


class InputOutput:
    def __init__(self):
        self.abc = None

    def get_string(self):
        self.abc = input()

    def print_string(self):
        print(self.abc.upper())


my_obj = InputOutput()
my_obj.get_string()
my_obj.print_string()
