INF = int(1e9)
# 노드 수가 상대적으로 적을 때 사용.

n = int(input())
m = int(input())
g = [[INF] * (n + 1) for _ in range(n + 1)] 

# 1. (x, x)는 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            g[a][b] = 0

# 2. 각 간선 정보 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

# 3. 플로이드 워셜 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])


# 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(g[a][b] if g[a][b] != INF else "INF", end=' ')
    print()
    