def solution(s):
    count = len(s)
    if count%2==1:
        count = count//2
        answer = s[count]
    else:
        count = count//2-1
        answer = s[count:count+2]
    return answer

print(solution("abcde"))
print(solution("abcd"))