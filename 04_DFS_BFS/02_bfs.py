from collections import deque

def bfs(gragh, start, visitied):
    q = deque([start])

    # 1. 현재 노드를 방문처리
    visited[start] = True

    # 2. 큐가 빌때까지 인접노드 탐색
    while q:
        # 노드를 꺼내 출력
        v = q.popleft()
        print(v, end=' ')

        # v의 인접노드 중 방문 안한 노드들 모두 큐에 삽입하고 방문처리
        for i in gragh[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

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

bfs(gragh, 1, visited)