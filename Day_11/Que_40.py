"""
    Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
    otherwise print "No".
"""

input_value = input()

if input_value in ["yes", "YES", "Yes"]:
    print("Yes")
else:
    print("No")


