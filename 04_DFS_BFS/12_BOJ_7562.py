# 테케 / 체스판 한 변 길이 / 현재 위치 / 이동하려는 위치
# 최소 이동횟수 출력
# 풀이: 미로탈출 문제처럼, 모든 경로 확인후 가는 좌표마다 +1, 최종좌표 출력
# 나이트 이동 좌표 만들기
# [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

# 두번째 풀이
from collections import deque

tc = int(input())
dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]

for _ in range(tc):
    l = int(input())
    x, y = map(int, input().split())
    x_end, y_end = map(int, input().split()) 

    g = [[0] * l for _ in range(l)]

    # "최소 몇 번만에 이동" -> bfs로 +1 해주기
    q = deque()
    q.append((x, y))
    g[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and g[nx][ny] == 0:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1

    print(g[x][y] - 1)


# from collections import deque

# dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]

# def bfs(x, y, x_end, y_end):
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 1

#     while q:
#         x, y = q.popleft()

#         if x == x_end and y == y_end:
#             return graph[x][y] - 1

#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] == 0:
#                     q.append((nx, ny))
#                     graph[nx][ny] = graph[x][y] + 1

# test = int(input())
# for _ in range(test):
#     n = int(input())
#     graph = [[0] * n for _ in range(n)]
#     x, y = map(int, input().split())
#     x_end, y_end = map(int, input().split())

#     print(bfs(x, y, x_end, y_end))



