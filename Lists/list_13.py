""" Write a function that computes the list of the first 100 Fibonacci numbers. The first two Fibonacci numbers are 1
and 1. The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number. The first few
are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8. """
fibonacci_cache = {}


def fibonacci(n):
    value = 0
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value


for i in range(1, 101):
    print(i, ":", fibonacci(i))
