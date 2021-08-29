import math

items = input("총 건수를 입력해주세요 :")
pages = input("페이지에 보여줄 수를 입력해주세요 :")

if int(items) == 0:
    print(1)
else:
    result = math.ceil(int(items) / int(pages))
    print(result)