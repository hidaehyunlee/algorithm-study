from collections import deque

gragh = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# 230216
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        for v in gragh[now]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)


# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = True

#     while q:
#         x = q.popleft()
#         print(x, end=' ')

#         for nx in gragh[x]:
#             if visited[nx] == False:
#                 q.append(nx)
#                 visited[nx] = True

bfs(1)