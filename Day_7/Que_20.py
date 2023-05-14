"""
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
    range 0 and n.

    Suppose the following input is supplied to the program:
    14

    Then, the output should be:
    0
    7
    14
"""


class Divisible:

    def divide_by_seven(self, number_value):
        for value in range(number_value + 1):
            if value % 7 == 0:
                yield value


input_number = int(input())
generator_result = Divisible().divide_by_seven(input_number)

for val in generator_result:
    print(val)
