"""
    Write a program to generate and print another tuple whose values are even numbers in the given tuple
    (1,2,3,4,5,6,7,8,9,10).
"""

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

updated_tuple = tuple(val for val in my_tuple if val % 2 == 0)

print(updated_tuple)
