# p.227
# 작은 금액부터 큰 금액 순으로 확인하며 만들 수 있는 최소한의 화폐개수 찾기

n, m = map(int, input().split()) #화폐 종류, 그 가치의 합
arr = [] # n개 화폐종류 담을 리스트
for i in range(n):
    arr.append(int(input()))
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - arr[i]] + 1)

# 출력
if d[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
    