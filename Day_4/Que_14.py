"""
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:
    Hello world!

    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
"""

input_value = input()
upper_count, lower_count = 0, 0


for val in input_value:
    if val.isalpha():
        if val.isupper():
            upper_count += 1
        else:
            lower_count += 1

print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)

