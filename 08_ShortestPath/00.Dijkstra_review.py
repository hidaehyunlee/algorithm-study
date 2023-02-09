import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
g = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c)) # 1번 노드 (3, 5) -> (노드, 비용)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in distance[1:]:
    print(i if i != INF else "INF")