"""
    Define a function that can accept two strings as input and print the string with maximum length in console. If two 
    strings have the same length, then the function should print all strings line by line.
"""


def compare_length(str_1, str_2):
    if len(str_1) == len(str_2):
        print(str_1)
        print(str_2)
    elif len(str_1) > len(str_2):
        print(str_1)
    else:
        print(str_2)


input_value = input().split()
compare_length(input_value[0], input_value[1])
