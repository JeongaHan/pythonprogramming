n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))


def quick_sort(array):
    if len(array) <= 1: return array
    pivot = array[len(array) // 2]
    left, equal_arr, right = [], [], []
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(left) + equal_arr + quick_sort(right)


print(quick_sort(arr))
