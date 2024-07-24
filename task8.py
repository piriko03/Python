def fibonacci(n):
    if n <= 0:
        return "error"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))


#

def factorial(n):
    if n < 0:
        return "error"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))
