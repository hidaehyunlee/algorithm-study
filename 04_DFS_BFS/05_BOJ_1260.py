# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())

# 1. 그래프를 2차원리스트 True False로 저장
g = [[False] * (n + 1) for _ in range(n + 1)] # 노드 개수만큼 2차원리스트 초기화
for _ in range(m):
    a, b = map(int, input().split()) 
    g[a][b] = g[b][a] = True

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def dfs(v):
    # 현재 v 방문처리, print
    visited1[v] = True
    print(v, end=' ')
    
    for i in range(1, n + 1):
        # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
        if not visited1[i] and g[v][i]: 
            dfs(i)

def bfs(v):
    # 현재 v 방문처리, print
    q = deque([v])
    visited2[v] = True
    
    while q:
        v = q.popleft() # 큐에 있는 첫번째 값 pop
        print(v, end=' ')

        for i in range(1, n + 1):
            # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            if not visited2[i] and g[v][i]: 
                q.append(i) # i 값 push
                visited2[i] = True  # i 값을 방문처리

dfs(v)
print()
bfs(v)