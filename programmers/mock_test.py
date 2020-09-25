def solution(answers):
    answer = [0,0,0]
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        if student[0][i%len(student[0])] == answers[i]:
            answer[0] += 1
        if student[1][i % len(student[1])] == answers[i]:
            answer[1] += 1
        if student[2][i % len(student[2])] == answers[i]:
            answer[2] += 1


    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
