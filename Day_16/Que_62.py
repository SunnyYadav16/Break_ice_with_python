"""
    The Fibonacci Sequence is computed based on the following formula:

    f(n)=0 if n=0
    f(n)=1 if n=1
    f(n)=f(n-1)+f(n-2) if n>1
    Please write a program to compute the value of f(n) with a given n input by console.

    Example: If the following n is given as input to the program: 7

    Then, the output of the program should be: 0,1,1,2,3,5,8,13

    In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def fibonacci_series(number):
    if number < 2:
        return number
    fibo_list = [0,1]
    a, b = 0, 1

    for val in range(2, number+1):
        c = a + b
        fibo_list.append(c)
        a = b
        b = c
    return fibo_list


number_input = int(input())
print(*fibonacci_series(number_input), sep=',')
