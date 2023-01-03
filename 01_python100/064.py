n = int(input()) # 정량 N, 3과 7kg 엘레베이터로 움직일 수 있는 최소값 구하기
tmp = n
res = 0

if (n % 7 == 0 or n % 3 == 0):
    if n // 7:
        res = n // 7
        tmp = n // 7
    res += tmp // 3
    print(res)
else:
    print(-1)