a = int(input())


def factorial(a):
    if a > 1:
        return a * factorial(a - 1)
    else:
        return 1


print(factorial(a))
