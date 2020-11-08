num = int(input().strip())
# print(num)
# print(ord("a")) #97
# print(ord("A")) #65

for i in range(65,91):
    if num == 0:
        i += 32
    print(chr(i),end="")