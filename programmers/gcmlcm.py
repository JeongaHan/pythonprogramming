def solution(n, m):
    answer = []

    for i in range(n, 0, -1):
        if m % i == 0 and n % i == 0:
            answer.append(i)
            break

    for i in range(n, n * m + 1, n):
        if i % m == 0:
            answer.append(i)
            break

    return answer


print(solution(3, 12))
print(solution(2, 5))
print(solution(3, 4))
