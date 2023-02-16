import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
g = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 230216
# 틀린 부분: heappop() 할 때 인자로 q를 넣어야함 -> heappop(q)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist: # 이미 최단거리기때문에 볼 필요 없음
            continue

        for i in g[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in distance[1:]:
    print(i if i != INF else "INFINITY")

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     g[a].append((b, c)) # 1번 노드 (3, 5) -> (노드, 비용)

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue

#         for i in g[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(start)

# for i in distance[1:]:
#     print(i if i != INF else "INF")

'''
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
'''