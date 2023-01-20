# 33번 문제

graph = [
        [], [], 
        ['a', 'b', 'c'], 
        ['d', 'e', 'f'], 
        ['g', 'h', 'i'], 
        ['j', 'k', "l"], 
        ['m', 'n', 'o'], 
        ['p', 'q', 'r', 's'], 
        ['t', 'u', 'v'], 
        ['w', 'x', 'y', 'z']
    ]

n = input() #"23"
ans = []

def dfs(idx, v):
    # 한 노드 끝까지 탐색하면 백트래킹
    if len(v) == len(n):
        ans.append(v)
        return
    
    # 입력값 자릿수 단위 반복
    for i in range(idx, len(n)):
        # idx 노드에 연결된 모든 노드(문자) 반복
        for j in graph[n[i]]:
            dfs(i + 1, v + j)

dfs(0, "23")
print(ans)



