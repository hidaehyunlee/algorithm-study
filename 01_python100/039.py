# 문장이 입력되면 모든 q를 e로, b를 n으로 바꾸는 프로그램을 작성해 주세요.

s = list(input())

for i in range(len(s)):
    if s[i] == 'q':
        s[i] = 'e'
    elif s[i] == 'b':
        s[i] = 'n'

print(s)

# print(s.replace('q', 'e').replace('b', 'n'))
'''
AttributeError: 'list' object has no attribute 'replace'
-> replace 는 str 객체에 사용
'''