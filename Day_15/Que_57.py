"""
    Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""

string_input = input()
unicode_string = string_input.encode('utf-8')
print(unicode_string)