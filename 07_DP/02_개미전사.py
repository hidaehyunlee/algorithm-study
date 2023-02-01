# p.220 개미전사
# 풀이: 점화식: a_i = max(a_i-1, a_i-2 + k_i)

# 두번째 풀이
# 1 3 1 5
# 1, 3, 1, 5, 1 1, 1 5, 3 5, 0 -> 경우의 수 8개
#   -> i - 2 에서 식량을 털면 현재 i에서 털 수 있음
#   -> i - 1 에서 식량을 털면 현재 i에서 x
#   -> 둘 중 어느 값이 더 큰가 비교하면 됨
#       -> 점화식: d[i] = max(d[i - 1], d[i - 2] + k[i])

n = int(input()) # 식량창고 (3<= n <=100)
k = list(map(int, input().split())) # 각 식량창고에 저장된 식량 수 (0<= k <=1000)

d = [0] * 100
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n - 1]) # d[n]은 indexError

# n = int(input())
# arr = list(map(int, input().split()))
# d = [0] * 100

# d[0] = arr[0]
# d[1] = max(arr[0], arr[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + arr[i])

# print(d[n - 1])