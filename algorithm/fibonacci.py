a = int(input())
# 피보나치 수열 0번째 0, 1번째 1

def fibonacci(a):
    if a == 1:
        return 1
    elif a == 0:
        return 0
    else:
        return fibonacci(a - 2) + fibonacci(a - 1)


print(fibonacci(a))
