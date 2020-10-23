import re


# def intToKorean(number, official=False):
#     if number == 0:
#         return "영"
#     digits = str(number)
#     length = len(digits)
#     count = False
#     builder = []
#     for i in range(length):
#         base = length - i - 1
#         baseMod4 = base % 4
#         digit = int(digits[i])
#         if digit != 0:
#             count = True
#             if digit == 1:
#                 if official or baseMod4 == 0:
#                     builder.append('일')
#             else:
#                 builder.append('이삼사오육칠팔구'[digit - 2])
#             if baseMod4 > 0:
#                 builder.append('십백천'[baseMod4 - 1])
#         if baseMod4 == 0:
#             if count and base > 0:
#                 builder.append('만억조경해'[base // 4 - 1])
#             count = False
#     result = ''
#     for i in range(len(builder)):
#         result = result + builder[i]
#     return result


# print(intToKorean(111111, False))
# print(intToKorean(118, False))

def intToKorean(match):
    value = int(match.group())
    print(value)
    if value == 0:
        return "영"
    digits = str(value)
    length = len(digits)
    count = False
    builder = []
    for i in range(length):
        base = length - i - 1
        baseMod4 = base % 4
        digit = int(digits[i])
        if digit != 0:
            count = True
            if digit == 1:
                if baseMod4 == 0:
                    builder.append('일')
            else:
                builder.append('이삼사오육칠팔구'[digit - 2])
            if baseMod4 > 0:
                builder.append('십백천'[baseMod4 - 1])
        if baseMod4 == 0:
            if count and base > 0:
                builder.append('만억조경해'[base // 4 - 1])
            count = False
    result = ''
    for i in range(len(builder)):
        result = result + builder[i]
    return result


# p = re.compile('(?P<number>\d+)')
p = re.compile('(\d+)')
m = p.findall('2호선홍대입구역9번출구11')
print(p.sub(intToKorean, '2호선홍대입구역9번출구11'))
