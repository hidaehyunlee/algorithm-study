'''
Connected Component?
나누어진 각각의 그래프를 연결 요소라고 한다. 

이때 연결 요소가 될 조건은 다음과 같다.
1. 연결 요소에 속한 모든 정점을 연결하는 경로가 있어야 한다.
2. 또 다른 연결 요소에 속한 정점과 연결하는 경로가 있으면 안된다.
'''
# 풀이:
# 한 정점의 모든 경로를 다 돌았는데, visited가 남아있으면?
# cnt ++ 해주고 dfs 한번 더

# 그래프 표현방법: 정점만 저장하는게 좋을까? yes

# + 노드 하나인 예외경우 따로 처리 할 필요 X
# 재귀 허용치 넘어가면 런타임에러 아래로 해결
# -> sys.setrecursionlimit(10000)

# 2번째 풀이
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
# 그래프 정점만 저장 -> append 
g = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

#print(g) # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
visited = [False] * (n + 1)
cnt = 0
def dfs(v):
    visited[v] = True

    for i in g[v]:
        if not visited[i]:
            dfs(i)

for i in range(n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt - 1)


# import sys
# sys.setrecursionlimit(10000)

# def dfs(v):
#     visited[v] = True
#     for i in g[v]:
#         if not visited[i]:
#             dfs(i)

# n, m = map(int, sys.stdin.readline().split())
# cnt = 0
# visited = [False] * (n + 1)
# g = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     g[a].append(b)
#     g[b].append(a)

# for i in range(1, n + 1):
#     if not visited[i]:
#         # if not g[i]: # 노드 하나인 예외경우
#         #     cnt += 1
#         #     visited[i] = True
#         # else: # 해당 정점과 연결된 그래프 존재
#             dfs(i)
#             cnt += 1

# print(cnt)