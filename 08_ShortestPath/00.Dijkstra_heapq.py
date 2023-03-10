import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수
start = int(input()) # 시작 노드 번호
graph = [[] for _ in range(n + 1)] # 각 노드에 연결되어 있는 (노드, 비용) 리스트
distance = [INF] * (n + 1) # 최단거리 테이블

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a노드에서 b노드로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # start 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 최단거리가 가장 짧은 노드 찾기 -> get_smallest_node() 와 같은 역할
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드 now가 이미 처리된 적 있다면 무시
            continue
        
        # 현재 노드와 연결된 다른 인접 노드들 확인 -> 현재 노드를 거치는 비용이 더 적다면 업데이트
        for i in graph[now]:
            # i == now 노드의 간선 정보 ex) (3, 5)
            cost = dist + i[1] # dist(1번 노드가는 비용) + 5(1번 노드에서 3번 노드 가는 비용)
            if cost < distance[i[0]]: # distance[i[0]] == 3번노드로 가는 최단거리 테이블의 현재값
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

# start에서 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

'''
- input
    6 11
    1
    1 2 2
    1 3 5
    1 4 1
    2 3 3
    2 4 2
    3 2 3
    3 6 5
    4 3 3
    4 5 1
    5 3 1
    5 6 2

- graph의 생김새
    [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

- 각 단계별 distace[]의 생김새
    [1000000000, 0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    [1000000000, 0, 2, 1000000000, 1000000000, 1000000000, 1000000000]
    [1000000000, 0, 2, 5, 1000000000, 1000000000, 1000000000]
    [1000000000, 0, 2, 5, 1, 1000000000, 1000000000]
    [1000000000, 0, 2, 4, 1, 1000000000, 1000000000]
    [1000000000, 0, 2, 4, 1, 2, 1000000000]
    [1000000000, 0, 2, 4, 1, 2, 1000000000]
    [1000000000, 0, 2, 4, 1, 2, 1000000000]
    [1000000000, 0, 2, 3, 1, 2, 1000000000]
    [1000000000, 0, 2, 3, 1, 2, 4]
    [1000000000, 0, 2, 3, 1, 2, 4]
'''