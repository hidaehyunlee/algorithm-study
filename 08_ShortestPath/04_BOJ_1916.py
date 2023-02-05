'''
A(start)번째 도시에서 B(end)번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N
a,b,c = 노드(도시), 버스(간선), 비용 주어짐
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]: # i[0] -> 노드 | i[1] -> 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])