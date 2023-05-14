"""
    Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
    input by console.

    Example: If the following n is given as input to the program: 10

    Then, the output of the program should be: 0,2,4,6,8,10

    In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def calculate_even_numbers(number):
    for value in range(number+1):
        if value % 2 == 0:
            yield value


input_value = int(input())
returned_value = calculate_even_numbers(input_value)

for val in returned_value:
    print(val, sep=",")

