n, k = map(int, input().split())

a = sorted(list(map(int, input().split()))) # 오름
b = sorted(list(map(int, input().split())), reverse=True) # 내림

# 오답: b가 더 작을 수도 있으니 비교해야함
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))