# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.

s = input()

for i in s:
    if i.isupper():
        print(i.lower(), end='')
    elif i.islower():
        print(i.upper(), end='')