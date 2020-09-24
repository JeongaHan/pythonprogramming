def solution(numbers):
    answer = set()
    temp = 0
    for i in range(len(numbers)):
        for j in range(1, len(numbers) - i):
            temp = numbers[i] + numbers[i + j]
            answer.add(temp)
    return sorted(list(answer))


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
numbers = [5, 0, 2, 7]
print(solution(numbers))