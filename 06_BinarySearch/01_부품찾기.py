# p.197
# 문제: 매장 n개의 부품(고유번호) 중, 손님이 요청한 m개의 부품이 존재하면 순서대로 각각 yes, 아니면 no 출력

n = int(input())
arr_n = list(map(int, input().split())) # set(map(int, input().split()))이 더 효과적
m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    if i in arr_n:
        print("yes", end=' ')
    else:
        print("no", end=' ')