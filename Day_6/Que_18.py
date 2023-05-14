"""
    A website requires the users to input username and password to register. Write a program to check the validity of
    password input by users.

    Following are the criteria for checking the password:

    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12

    Your program should accept a sequence of comma separated passwords and will check them according to the above
    criteria. Passwords that match the criteria are to be printed, each separated by a comma.

    Example
    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E*,2We3345

    Then, the output of the program should be:
    ABd1234@1
"""

upper_char, lower_char, number, special_char = 0, 0, 0, 0

input_pwd = input().split(",")
print(input_pwd)
for valid_pwd in input_pwd:
    if 6 <= len(valid_pwd) <= 12:
        for character in valid_pwd:
            if character.islower():
                lower_char += 1
            if character.isupper():
                upper_char += 1
            if character.isdigit():
                number += 1
            if character in ["$", "#", "@"]:
                special_char += 1

        if lower_char > 1 and upper_char > 1 and number > 1 and special_char > 1:
            print(valid_pwd)
