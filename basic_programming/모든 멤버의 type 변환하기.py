# def solution(mylist):
#     answer = []
#     for i in mylist:
#         answer.append(int(i))
#     return answer

def solution(mylist):
    return list(map(int, mylist))


print(solution(['1', '100', '33']))
