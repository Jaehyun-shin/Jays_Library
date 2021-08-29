name_list = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
names = name_list.split(',')

lee_count = 0
kim_count = 0
leejy = 0
one_name = []

for i in names:
    if i[0] == "이":
        lee_count += 1
    elif i[0] == "김":
        kim_count += 1

for i in names:
    if i not in one_name:
        one_name.append(i)
    else:
        pass


print("이씨는 {}명, 김씨는 {}명 입니다.".format(lee_count, kim_count))
print("이재영씨는 {}번 반복됩니다.".format(names.count("이재영")))
print(one_name)
print(sorted(one_name))