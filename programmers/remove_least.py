def solution(arr):
    answer = []
    min = arr[0]
    if len(arr)==1:
        answer.append(-1)
        return answer
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
    for i in range(len(arr)):
        if arr[i] != min:
            answer.append(arr[i])
    return answer


arr = [2,3,6,1]
print(solution(arr))
