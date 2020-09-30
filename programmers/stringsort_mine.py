def solution(strings, n):
    strings = sorted(strings)
    strings = sorted(strings, key = lambda x : x[n])
    return strings


# strings = ['sun', 'bed', 'car']

strings = ['abce','abcd','cdx']
n = 2
print(solution(strings, n))
