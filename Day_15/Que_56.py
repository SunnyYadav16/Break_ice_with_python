"""
    Print a unicode string "hello world".
"""

string_value = "hello world"

print(string_value.encode("unicode_escape").decode())
