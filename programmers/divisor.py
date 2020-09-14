def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    answer.sort()
    if (len(answer) == 0):
        answer.append(-1)
    return answer


arr = [3, 2, 6]
print(solution(arr, 10))
