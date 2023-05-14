"""
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in
    comma separated form while n is input by console.

    Example: If the following n is given as input to the program: 100

    Then, the output of the program should be: 0,35,70

    In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def divisible(number):
    for val in range(number+1):
        if val % 35 == 0:
            yield val


input_value = int(input())
returned_value = divisible(input_value)

for val in returned_value:
    print(val, sep=",")




