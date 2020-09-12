def solution(phone_number):
    answer = phone_number[-4:]
    answer = "*" * (len(phone_number)-4) + answer
    return answer

phone_number = "01033334444"
print(solution(phone_number))