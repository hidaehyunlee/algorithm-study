INF = int(1e9)

n = int(input()) # 노드 수
m = int(input()) # 간선 수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 최단경로 테이블, 초기값 무한

# 1. 자기 자신에서 자기로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 2. 각 간선에 대한 정보 입력 받아 초기화
for _ in range(m):
    # a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 3. 점화식에 따라 플로이드 워셜 알고리즘 수행 -> Dab와 Dak + Dka 비교해서 더 작은 값으로
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=' ')
    print() # 2차원 리스트 형식으로 출력


'''
- input
    4
    7
    1 2 4
    1 4 6
    2 1 3
    2 3 7
    3 1 5
    3 4 4
    4 3 2

- output
    0 4 8 6 
    3 0 7 9 
    5 9 0 4 
    7 11 2 0
'''