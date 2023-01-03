# 복세편살! 어떤 입력이 주어지면 앞 글자만 줄여 출력

l = input().split()

for i in range(len(l)):
    print(l[i][0], end='')

# 더 파이썬스러운 코드
# user_input = input().split()
# result = ''

# for s in user_input:
#     result += s[0]

# print(result)