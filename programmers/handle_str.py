import re


def solution(s):
    p1 = re.compile('^[0-9]{4}$|^[0-9]{6}&')
    m = p1.match(s)
    if m:
        return True
    else:
        return False


print(solution("a1234"))
print(solution("1234"))
