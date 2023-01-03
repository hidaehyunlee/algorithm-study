# 20190923출력하기
# 0 1 2 3 9

'''
문자 -> 아스키 : ord()
아스키 -> 문자: chr()
'''

s = "azzzzzzzzz"
one = s.count('a')
nine = s.count('z')

print(one+1, one-1, one, nine, one-1, nine, one+1, one+2, sep='')