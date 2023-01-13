'''
다시 풀기
'''

from collections import deque

n, m = map(int, input().split())
g = [] # n*m

for i in range(n):
    g.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        # 현재위치에서 상하좌우 확인
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                continue
            if g[next_x][next_y] == 0:
                continue
            if g[next_x][next_y] == 1:
                g[next_x][next_y] = g[x][y] + 1
                q.append((next_x, next_y))
    return g[n - 1][m - 1]

print(bfs(0, 0))