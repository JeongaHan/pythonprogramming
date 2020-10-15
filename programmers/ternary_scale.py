import math


def solution(n):
    answer = 0
    three = []
    while n > 0:
        three.append(n % 3)
        n = n // 3
    three.reverse()
    for i in range(len(three)):
        answer += three[i] * math.pow(3, i)
    return int(answer)


print(solution(45))