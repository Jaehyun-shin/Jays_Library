number_list = input("숫자 리스트를 입력해주세요.")

number = number_list.split(" ")
numbers = []

# 정수형으로 변환

for i in number:
    numbers.append(int(i))

# 정렬 후 짝수와 홀수로 나누기

numbers.sort()

ones = []
twos = []


for i in range(0, len(numbers)):
    if i % 2 == 0:
        ones.append(numbers[i])
    else:
        twos.append(numbers[i])
result = []

twos.reverse()

print(numbers)
print(ones, twos)

for i in range(0, len(ones)):
    result.append(ones[i])
    result.append(twos[i])

print(result)