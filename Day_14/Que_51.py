"""
    Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


def division():
    return 5 / 0


try:
    print(division())
except ZeroDivisionError as e:
    print("Number is getting divided by zero, which is not possible.")
