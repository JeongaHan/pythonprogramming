odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['life', 'is']]

a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])

a = [1, 2, ['a', 'b', ['life', 'is']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))
a[2] = 4
print(a)
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))
# print(a.index(0)) ValueError

a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

# remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수이다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

a = [1, 2, 3]
print(a.pop())
print(a)

# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.
a = [1, 2, 3]
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
