# bfs: 1,1인곳에서 출발, 0으로 바꿔서 다시 탐색 안하게

# 2번째 풀이
from collections import deque

n = int(input())
g = [list(map(int, input())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    g[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):  
            nx = x + dx[i]    
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 1:
                if g[nx][ny] == 1:
                    q.append((nx, ny))
                    g[nx][ny] = 0
                    cnt += 1

    ans.append(cnt)


for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            bfs(i, j)

print(len(ans))
for i in sorted(ans):
    print(i)




# from collections import deque

# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# cnt = [] # 단지

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))

#     graph[x][y] = 0
#     house = 1

#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 q.append((nx, ny))
#                 house += 1

#     cnt.append(house)

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             bfs(i, j)

# # ans 출력
# print(len(cnt))
# for i in sorted(cnt):
#     print(i)