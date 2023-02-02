# p.262 전보

'''
n개의 도시, 도시끼리 통로가 있어야 메시지 전달 가능, 일정시간 소요
    - input: n, m, c | x, y, z == x에서 y로 이어지고 z시간 소요
    - c도시에서 가능한 모든 도시에 메시지를 보냈을 때 받는 도시의 개수와 모든 도시들이 메시지를 받는데까지 걸리는 시간 출력
'''
# 헷갈린 부분: 총 시간 != distance의 합. 그냥 가장 먼 노드까지 걸리는 시간
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c) # c에서 시작

cnt = 0
time = 0 # 가장 먼 곳의 시간 (가까운 노드의 시간은 이미 포함되므로)
for i in distance:
    if i != INF:
        cnt += 1
        time = max(time, i)

print(cnt - 1, time) # c 노드는 빼고 출력



