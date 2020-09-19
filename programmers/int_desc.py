def solution(n):
    li = []
    answer = 0
    while n / 10 > 0:
        li.append(n % 10)
        n //= 10
    li = sorted(li, reverse=True)
    for i in range(len(li) - 1, -1, -1):
        answer += li[len(li)-1-i] * 10 ** i
    return answer


print(solution(118372))
