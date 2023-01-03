# 사용자에게 숫자를 입력받고 이를 2진수를 바꾸고 그 값을 출력해주세요.
# (bin 함수를 사용하지 않고 풀어주세요.)

n = int(input())
b = list()

while n:
    if n % 2 == 0:
        b.append(0)
    else:
        b.append(1)
    n //= 2

b = sorted(b, reverse=True)
for i in range(len(b)):
    print(b[i], end='')

# 더 나은 코드
# print(''.join(b))
'''
join(list) : 리스트의 문자열들을 합치는 역할
" ".join(list) -> 띄어쓰기(혹은 다른 문자열) 포함해서 join
'''
