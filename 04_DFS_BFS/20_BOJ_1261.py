# 알고스팟 https://www.acmicpc.net/problem/1261
# output: 벽을 최소 몇 개 부수어야 하는지 출력
# 숨바꼭질3처럼 가중치 문제
# 벽 부수는 횟수가 0인걸 먼저 처리 -> 0에서 0으로 이동 먼저 처리

from collections import deque

m, n = map(int, input().split()) # 가로, 세로 1 <= nm <= 100
g = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if g[nx][ny] == 0: # 빈 방 우선 탐색
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

print(bfs())