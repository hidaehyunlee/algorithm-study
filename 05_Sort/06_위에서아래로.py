n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in sorted(arr, reverse=True):
    print(i, end=' ')