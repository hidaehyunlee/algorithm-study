ans = []
prev_v = []

def dfs(v):
    # 리프노드일때 결과추가
    if len(v) == 0:
        ans.append(prev_v[:])

    # 순열 생성 재귀 호출
    for i in v:
        next_v = v[:]
        next_v.remove(i)

        prev_v.append(i)
        dfs(next_v)
        prev_v.pop()

n = list(map(int, input()))
dfs(n)
print(ans)