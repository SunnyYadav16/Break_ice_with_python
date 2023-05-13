"""

    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]

    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.

    For example Let us assume the following comma separated input sequence is given to the program:
    100,150,180

    The output of the program should be:
    5,4,4

    If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the
    output received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it
    should be assumed to be a console input.

"""
from math import sqrt

val_c, val_h = 50, 30


def calculation(d_value):
    return str(round(sqrt((2 * val_c * val_h) / d_value)))


if __name__ == "__main__":
    my_list = []
    val_D = input().split(",")

    for val in val_D:
        calculated_value = calculation(int(val))
        my_list.append(calculated_value)

    print(",".join(my_list))
