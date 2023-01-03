# 문자열 정렬
# <, >, ^ 기호 앞에 나오는 건 빈 칸에 채울 문자
# <, >, ^ 기호 뒤에 나오는 숫자는 자릿수

# 왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} |'.format('left', 'a')
print(s9)
 
 
# 오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} |'.format('right', 'b')
print(s10)
 
 
# 가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} |'.format('center', 'c')
print(s11)

# 59번 답
user_input = input()
print("{0:=^50}".format(user_input))