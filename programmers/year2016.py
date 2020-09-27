# 2016년 1월 1일은 금요일
# SUN,MON,TUE,WED,THU,FRI,SAT

def solution(a, b):
    days = 0
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    if a > 1:
        for i in range(a - 1):
            days += month[i]
    days += b - 1
    return week[days % 7]


a = 5
b = 24
print(solution(a, b))

# 1.29 = fri
# 1.31 = sun
# 2.1 = mon
