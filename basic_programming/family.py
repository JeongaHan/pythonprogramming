class Family:
    lastname = '박'


print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))

# 클래스변수 : 모두 같은 메모리를 가리킨다.
