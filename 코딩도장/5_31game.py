import random

number = 0
print("컴퓨터 먼저 시작합니다.")
numbers = []
select = random.randint(1,3)
for i in range(0, select):
    number += 1
    numbers.append(number)
print(numbers)

numbers = input("0, 0, 0 형태로 입력해주세요 :").split(',')
number = int(numbers[-1])

while number < 31:
    if len(numbers) > 2:
        numbers = input("3개의 숫자만 입력해주세요").split(',')
        number = numbers[-1]
    else:
        pass