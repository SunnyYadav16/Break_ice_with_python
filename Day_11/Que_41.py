"""
    Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

updated_list = list(map(lambda x: x**2, my_list))
print(updated_list)
