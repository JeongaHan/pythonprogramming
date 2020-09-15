def solution(s):
    answer = ''
    temp = []
    for i in range(len(s)):
        temp.append(s[i])
    temp = sorted(temp,reverse=True)
    for i in range(len(temp)):
        answer += temp[i]
    return answer

print(solution('Zbcdefg'))