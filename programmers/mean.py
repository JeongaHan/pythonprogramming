def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    return answer/len(arr)

arr = [1,2,3,4]
arr2 = [5,5]
print(solution(arr))
print(solution(arr2))