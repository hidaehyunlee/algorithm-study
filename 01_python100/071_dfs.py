'''
DFS에서 데이터를 찾을 때는 항상 "앞으로 찾아야 가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색을 합니다.
 
이 원칙을 반드시 기억해주셔야 해요. 
 
그래서 특정 노드가 
"앞으로 찾아야 가야할 노드"라면 계속 검색을 하는 것이고, 
"이미 방문한 노드"면 무시하거나 따로 저장하면 됩니다. 

https://data-marketing-bk.tistory.com/44 <- 꼭 읽기
'''

# 출력: ['E', 'A', 'B', 'C', 'D', 'F']

graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
    }

def dfs(graph, start):
    visited = [] # 방문 리스트
    stack = [start] # 아직 방문 안한 리스트에 시작노드 설정

    # 아직 방문 안한 노드가 존재한다면
    while stack:
        n = stack.pop() # 시작 노드 지정 E
        if n not in visited: # 방문 리스트에 없다면 
            visited.append(n) # 방문 리스트에 노드 추가
            stack += graph[n] - set(visited) # 방문 안한 리스트에, ? 인접 노드 추가 ?
    return visited

print(dfs(graph, 'E'))