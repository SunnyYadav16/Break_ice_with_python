"""
    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
    number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

result = []

for value in range(1000, 3001):
    if all(int(val) % 2 == 0 for val in str(value)):
        result.append(value)

print(*result, sep=",")
