m = int(input())
constructor = -1
for n in range(0, m):
    sum = n
    temp = n
    while temp > 0:
        sum = sum + temp % 10
        temp = temp // 10
    if sum == m:
        print(n)
        constructor = n
        break

if constructor == -1:
    print(0)

