# https://www.acmicpc.net/problem/13023
# a-b-c-d-e 그래프가 있어야한다는 것 
# == a노드에서 4개의 노드를 탐색하는데 성공했다면 성공
# 5개의 노드를 깊게 탐색한 순간 프로그램이 완료되므로, bfs보단 dfs를 채택
# https://grini25.tistory.com/110 -> 문제해설

n, m = map(int, input().split()) # 사람수, 관계수
visited = [False] * n
ans = False

gragh = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

def dfs(idx, depth):
    global ans
    if depth == 4:
        ans = True
        return
    
    for i in gragh[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans: print(1)
else: print(0)