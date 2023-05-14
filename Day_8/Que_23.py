"""
    Write a method which can calculate square value of number
"""


def calculate_sqrt(number):
    return number**2


input_value = int(input())
squared_value = calculate_sqrt(input_value)
print(squared_value)