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
    if arrdict.get(item) is None:
        arrdict[item] = 1
    else:
        arrdict[item] += 1
if max(arrdict.values()) == 1 and len(arr)>1:
    print(arr[1])
else:
    print([k for k, v in arrdict.items() if v == max(arrdict.values())][0])

print(max(arr)-min(arr))