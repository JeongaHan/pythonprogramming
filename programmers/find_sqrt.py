def solution(n):
    for i in range(0, n + 1):
        if i ** 2 == n:
            return (i + 1) ** 2
    return -1


print(solution(121))
print(solution(3))
print(solution(1))
