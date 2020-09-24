def solution(x, n):
    answer = []
    temp = 0
    for i in range(n):
        temp += x
        answer.append(temp)
    return answer


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
