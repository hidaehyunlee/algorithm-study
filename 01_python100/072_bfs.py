'''
BFS를 구현하기 위해서는 항상 "방문하고자 하는 노드"와 "방문했던 노드"를 나누어서 알고리즘을 구성하는 것이 핵심 원리입니다. 
 
1. 시작 노드를 방문했던 노드에 삽입한다. 
2. 방문할 노드에 시작노드의 Child Node를 삽입한다. 
3. Child노드를 중심으로 다시 1~2단계를 거쳐 탐색한다.
'''

graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        # BFS와 DFS의 가장 큰 차이점은 While문 다음에 어떤 자료를 우선적으로 추출하느냐 입니다. 
        # DFS 같은 경우 리스트의 가장 끝에 있는 데이터를 기준으로 추출하지만, 
        # BFS는 리스트의 가장 처음에 있는 인자를 받습니다. 
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(bfs(graph, 'E'))