"""
    Write a program that computes the net amount of a bank account based a transaction log from console input. The
    transaction log format is shown as following:
    D 100
    W 200
    D means deposit while W means withdrawal.

    Suppose the following input is supplied to the program:
    D 300
    D 300
    W 200
    D 100

    Then, the output should be: 500

"""

total = 0

while True:
    input_value = input().split()
    if len(input_value) == 0:
        break

    if input_value[0] == 'D':
        total += int(input_value[1])
    elif input_value[0] == 'W' and int(total) != 0:
        total -= int(input_value[1])

print(total)
