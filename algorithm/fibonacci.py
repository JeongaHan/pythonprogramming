a = int(input())


def fibonacci(a):
    if a == 1:
        return 1
    elif a == 0:
        return 0
    else:
        return fibonacci(a - 2) + fibonacci(a - 1)


print(fibonacci(a))
