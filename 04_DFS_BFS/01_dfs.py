def dfs(gragh, v, visited):
    # 1. 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    # 2. 현재 노드에 방문하지 않은 인접노드가 있으면 재귀로 방문
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)

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

dfs(gragh, 1, visited)