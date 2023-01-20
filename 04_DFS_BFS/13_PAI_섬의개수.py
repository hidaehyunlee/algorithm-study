# 32번 섬의 개수
# 풀이: x,y 1일때 상하좌우 다 탐색/ 0으로 바꿔서 다시 탐색 안하게 / dfs한번 끝나면 cnt++
# visited 행렬 만들어서 방문한 경로 저장할 필요가 있나 먼저 고민하기.
# 이 문제는 현재 행렬에 방문한 경로를 표시하기만 해도 됨

import sys
sys.setrecursionlimit(10000)

graph = [
        [1,1,0,1,0], 
        [1,1,0,1,0], 
        [1,1,0,0,0], 
        [0,0,0,1,1]
    ]

ans = 0
c = len(graph)
r = len(graph[0])

def dfs(x, y):
    if x < 0 or x >= c or y < 0 or y >= r or graph[x][y] == 0:
        return
    
    graph[x][y] = 0 # 육지를 바다로 -> 그래야 다시 계산 안함 (가지치기)
    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x - 1, y)

for i in range(c):
    for j in range(r):
        if graph[i][j] == 1:
            dfs(i, j)
            ans += 1

print(ans)