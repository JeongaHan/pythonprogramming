n = int(input())
arr = list()
arrsum = 0
for i in range(n):
    arr.append(int(input()))
    arrsum += arr[i]

arr.sort()
print(arrsum / n)
print(arr[n // 2])

arrdict = dict()
for item in arr:
    arrdict[item] = 0
for item in arr:
    if arrdict[item] > 1:
        arrdict[item] += 1
    else:
        arrdict[item] = 1
if max(arrdict.values()) == 1:
    print(arr[1])
arrdict2 = {v: k for k, v in arrdict.items()}
print(arrdict)
print(arrdict2)
