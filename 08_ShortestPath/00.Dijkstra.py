import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드의 번호

# 1. 리스트 생성 및 초기화
graph = [[] for _ in range(n + 1)] # 각 노드에 연결되어 있는 노드 번호를 담는 리스트
visited = [False] * (n + 1) # 방문 체크용 리스트
distance = [INF] * (n + 1) # 최단거리 테이블 생성 및 무한으로 초기화

# graph 초기화: 모든 간선 정보 입력받기
for _ in range(m):
    # a노드에서 b노드까지 가는 비용(간선 값)이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 2. 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환 (리스트 순차탐색)
def get_smallest_node():
    min_val = INF
    idx = 0 # 최단거리가 가장 짧은 노드

    for i in range(1, n + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i # 노드
    return idx

# 3. 다익스트라 구현
def dijkstra(start):
    # 시작 노드에 대해 최단거리 테이블 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 기준 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거치는 경우가 더 짧은 경우, 업데이트
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 4. 다익스트라 수행
dijkstra(start)

# 5. 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우에는 INF 출력
    if distance[i] == INF:
        print("INFINITY")
    else: # 최단거리 출력
        print(distance[i])
