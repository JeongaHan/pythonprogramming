import copy


def solution(mylist):
    answer = copy.deepcopy(mylist)
    for i in range(len(answer)):
        for j in range(len(answer)):
            answer[i][j] = mylist[j][i]

    return answer


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(solution(mylist))
# new_list = list(map(list, zip(*mylist)))
# print(new_list)
print(*mylist[0])