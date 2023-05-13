"""
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
    whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
    sequence.

    Example:
    0100,0011,1010,1001

    Then the output should be:
    1010
"""

input_value = list(map(str, input().split(',')))
my_list = []

for val in input_value:
    if int(val) % 5 == 0 and int(val[0]) != 0:
        my_list.append(val)

print(",".join(my_list))



