# 입력
# aaabbbbcdddd
# 출력
# a3b4c1d4
! 다시풀기

s = input()
count = 0

for i in range(len(s)):
    if s[i] == s[i + 1]:
        print(i)
    #     count += 1
    # else:
    #     print(s, count, sep='', end='')
    #     count = 0
