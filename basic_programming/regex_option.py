import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

# DOTALL, S
p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE, I
p = re.compile('[a-z]',re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


# MULTILINE, M
p = re.compile("^python\s\w+",re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))