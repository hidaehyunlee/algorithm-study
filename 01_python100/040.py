max_weight = int(input())
n = int(input())

l = list()
sum_weight = 0
count = 0

for i in range(n):
    l.append(int(input()))

for i in range(n):
    if sum_weight <= max_weight:
        sum_weight += l[i] 
        count += 1
    else:
        break;

print(count - 1)

'''
# 더 좋은 코드
total = 0
count = 0
limit = int(input('제한무게는 얼마인가요? : '))
n = int(input('몇명이 탈 수 있나요? : '))
 
for i in range(n):
    total += int(input('몸무게를 입력해주세요 : '))
    if total <= limit:
        count += 1
'''