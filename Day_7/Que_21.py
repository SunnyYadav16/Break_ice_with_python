"""
    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
    with a given steps. The trace of robot movement is shown as the following:

    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

    The numbers after the direction are steps. Please write a program to compute the distance from current position
    after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
    Example: If the following tuples are given as input to the program:

    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2

    Then, the output of the program should be:
    2
"""
from math import sqrt

starting_point = [0, 0]

while True:
    input_value = input().split()
    if len(input_value) == 0:
        break

    if input_value[0] == "UP":
        starting_point[1] += int(input_value[1])
    elif input_value[0] == "DOWN":
        starting_point[1] -= int(input_value[1])
    elif input_value[0] == "LEFT":
        starting_point[0] -= int(input_value[1])
    else:
        starting_point[0] += int(input_value[1])

print(round(sqrt(starting_point[1] ** 2 + starting_point[0] ** 2)))
