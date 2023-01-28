# 숨바꼭질3 https://www.acmicpc.net/problem/13549
#  1초 후에 X-1 또는 X+1로 이동
#  0초 후에 2*X의 위치로 이동하게
# 가장 빠른 시간이 몇 초 후
# 아이디어: 시간을 최소화하는 0초로 이동하는 연산이 가장 우선 체크되어야 한다.
#           -> q.popleft로 체크하므로, q.appendleft 연산으로 우선순위 줄 수 있음

# 세번째 제출
# 놓친 부분: q = deque(); q.append(n 혹은 [n]) 과 q = deque([n]) 은 다르다
# - nx 가 -1인 곳만 방문하도록 하기  
from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001

q = deque([n])
visited[n] = 0

while q:
    x = q.popleft()

    if x == k:
        print(visited[x])
        break

    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx <= 100000 and visited[nx] == -1:
            if nx == x * 2:
                q.appendleft(nx)
                visited[nx] = visited[x]
            else:
                q.append(nx)
                visited[nx] = visited[x] + 1


# 두번째 제출
# from collections import deque
# import sys

# n, k = map(int, sys.stdin.readline().split())

# def bfs():
#     graph = [-1] * 100001
#     graph[n] = 0
#     queue = deque([n])

#     while queue:
#         x = queue.popleft()

#         # 동생의 위치에 도달했다면 리턴
#         if x == k:
#             print(graph[x])
#             return

#         # 반복문을 통해 3가지 이동의 경우를 확인
#         for nx in (x + 1, x - 1, x * 2):
#             # next x가 범위 내에 있고 and 이동하지 않았다면 이동
#             if 0 <= nx <= 100000 and graph[nx] == -1:
#                 # 순간이동이라면
#                 if nx == x * 2:
#                     graph[nx] = graph[x] # 0초 갱신
#                     queue.appendleft(nx) # 순간이동이기에 먼저 탐색
#                 else:
#                     graph[nx] = graph[x] + 1
#                     queue.append(nx)

# bfs()

# 첫번째 제출:  if graph[2 * x] == 0 and (2 * x) <= max_len: IndexError: list index out of range
# n, k = map(int, input().split())
# max_len = 100001
# graph = [0] * max_len
# sec = 0

# q = deque()
# q.append(n)

# while q:
#     x = q.popleft()

#     if x == k:
#         print(graph[x])
#     # 2x 이동
#     if graph[2 * x] == 0 and (2 * x) <= max_len:
#         graph[2 * x] = graph[x]
#         q.appendleft(2 * x)
#     # x - 1 이동
#     if graph[x - 1] == 0 and 0 <= x - 1:
#         graph[x - 1] = graph[x] + 1
#         q.append(x - 1)
#     # x + 1 이동
#     if graph[x + 1] == 0 and x + 1 <= max_len:
#         graph[x + 1] = graph[x] + 1
#         q.append(x + 1)
    