"""
    Define a custom exception class which takes a string message as attribute.
"""


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")

except CustomException as ce:
    print(f"The error raised: {ce.message}")
