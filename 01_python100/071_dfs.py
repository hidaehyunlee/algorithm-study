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

## 재귀함수
def dfs_recursive(graph, start, visited = []):
    # 데이터를 추가 + 재귀
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def dfs(graph, start_node):
    # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    need_visited.append(start_node) # 시작 노드를 시정하기
    
    # 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
        node = need_visited.pop() # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        
        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            visited.append(node) # 방문한 목록에 추가하기 
            need_visited.extend(graph[node]) # 그 노드에 연결된 노드를 
            
    return visited