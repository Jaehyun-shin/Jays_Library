import random
print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다")
print("이 숫자를 맞춰주세요")
num = random.randint(1,100)

innum = input("1~100 숫자 입력 :")
innum = int(innum)
count = 0

while True:
    if innum > num:
        print("DOWN")
        innum = input("1~100 숫자 입력 :")
        innum = int(innum)
        count += 1
    elif innum < num:
        print("UP")
        innum = input("1~100 숫자 입력 :")
        innum = int(innum)
        count += 1
    else:
        print("정답입니다! {}회 만에 맞췄어요.".format(count))
        break