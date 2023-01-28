# 동전0 https://www.acmicpc.net/problem/11047
# 동전 n 종류, 합 k를 위한 필요한 동전 개수 최소값 구하기

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
ans = 0

coins.sort(reverse=True)
for i in coins:
    if k >= i:
        ans += (k // i)
        k %= i

print(ans)