import re

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)
for r in result:
    print(r)

m = p.match("python")
print(m.group(), m.start(), m.end(), m.span())

m = p.search("3 python")
print(m.group(), m.start(), m.end(), m.span())

m = re.match('[a-z]+','python')
print(m.group())