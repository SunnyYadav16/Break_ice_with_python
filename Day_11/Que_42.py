"""
    Write a program which can map() and filter() to make a list whose elements are square of even number
    in [1,2,3,4,5,6,7,8,9,10].
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

updated_list = list(map(lambda y: y**2, filter(lambda x: x % 2 == 0, my_list)))
print(updated_list)
