n, k = map(int, input().split())

a = sorted(list(map(int, input().split()))) # 오름
b = sorted(list(map(int, input().split())), reverse=True) # 내림

for i in range(k):
    a[i] = b[i]

print(sum(a))