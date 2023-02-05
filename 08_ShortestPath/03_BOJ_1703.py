# 최단경로 https://www.acmicpc.net/problem/1753

'''
시작점에서 다른 모든 정점으로의 최단경로
모든 간선의 가중치는 10이하의 자연수
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의

츨력: 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijktras(start):
    q = []
    heapq.heappush(q, (0, start)) # 최단거리 0, 노드 Start
    distance[start] = 0 # 최단거리 테이블

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijktras(start)

# for i in range(1, v + 1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

for i in distance[1:]:
    print(i if i != INF else "INF")