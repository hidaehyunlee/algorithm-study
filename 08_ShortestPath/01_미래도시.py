# p.259 미래도시

'''
1번부터 n번까지의 회사, 연결되어있는 각 회사끼리는 양방향 이동 안됨, 도시 이동시 시간 +1
1번회사 -> k번회사 -> x번회사 가는 최단 시간
'''

# 풀이: n의 범위가 100으로 작으므로 플로이드워셜로 풀기, 1->k + k->x 
# 틀린 부분:
    # 1. 간선 값 초기화 할 때 반대편 행렬도 같이 초기화 graph[a][b] = graph[b][a] = 1
    # 2. ans가 INF보다 큰 경우가 생길 수 있음! 두 값을 더하기 때문에.
 
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
x, k = map(int, input().split())

for v in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][v] + graph[v][b])

ans = graph[1][k] + graph[k][x]
if ans >= INF:
    print("-1")
else:
    print(ans)