n = int(input())
arr = list()
for i in range(n):
    arr.append(input().split())
arr = sorted(arr, key=lambda x: int(x[0]))

for line in arr:
    print(line[0], line[1])
