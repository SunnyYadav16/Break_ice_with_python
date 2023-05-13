"""
    Write a program that accepts a sentence and calculate the number of letters and digits.

    Suppose the following input is supplied to the program:
    hello world! 123

    Then, the output should be:
    LETTERS 10
    DIGITS 3
"""

input_value = input()
letter_count, digit_count = 0, 0

for val in input_value:
    if val.isalpha():
        letter_count += 1
    elif val.isdigit():
        digit_count += 1

print("LETTERS", letter_count)
print("DIGITS", digit_count)

