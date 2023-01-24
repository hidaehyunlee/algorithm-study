# 1. 시작점, 끝점은 0과 n
# 2. 시작점과 끝점을 통해 중간 지점을 구하고
# 3. 중간 지점의 제곱 값과 n을 비교
# 4. 비교했을 때, n 미만이면 시작점 = 중간점 + 1
# 5. n 이상이면 끝점 = 중간점 - 1

n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)