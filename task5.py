def nums(dictionary):
    if not dictionary:
        print("empty")
        return

    min_value = min(dictionary.values())

    print(min_value)

my_dict = {'a': 100, 'b': 38, 'c': 48, 'd': 11}

nums(my_dict)


#
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(10)
print(result)