dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 동일한 Key가 존재하면 어떤 Key에 해당하는 Value를 불러야 할지 알 수 없다
a = {1: 'a'}
print(a)
# Key에 리스트는 쓸 수 없다
# a = {[1,2] : 'hi'}

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
for k in a.keys():
    print(k)
print(list(a.keys()))
print(a.values())
print(a.items())
a.clear()
print(a)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('nokey'))  # None 반환
# print(a['nokey']) key 오류

print(a.get('foo', 'bar'))

print('name' in a)
print('email' in a)