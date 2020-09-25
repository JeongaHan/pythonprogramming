def solution(answers):
    score = [0, 0, 0]
    answer = []
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        if student[0][i % len(student[0])] == answers[i]:
            score[0] += 1
        if student[1][i % len(student[1])] == answers[i]:
            score[1] += 1
        if student[2][i % len(student[2])] == answers[i]:
            score[2] += 1

    if score[0] == score[1] & score[1] == score[2]:
        return [1, 2, 3]
    tempmax = max(score)
    if score[0] == tempmax:
        answer.append(1)
    if score[1] == tempmax:
        answer.append(2)
    if score[2] == tempmax:
        answer.append(3)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
