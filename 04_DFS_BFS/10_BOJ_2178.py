# 풀이: bfs
# 좌표가 경로를 벗어나지 않는 범위 내에서 1. 방문여부 확인, 2. 길이 맞는지 확인
# 조건에 맞다면 방문여부 수정 후, 큐에 넣어서 다음 차례에 추가

from collections import deque

n, m = map(int, input().split())
gragh = [list(map(int, input())) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 상하좌우

# bfs
q = deque()
q.append((0, 0))
gragh[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if gragh[nx][ny] == 0:
            continue
        if gragh[nx][ny] == 1:
            q.append((nx, ny))
            gragh[nx][ny] = gragh[x][y] + 1

#print(gragh)
print(gragh[n - 1][m - 1])