# 숨바꼭질4 https://www.acmicpc.net/problem/13913
# 최단이동 경로 출력 문제
from collections import deque

n, k = map(int, input().split())
length = 100001
g = [0] * length
path = [0] * length

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(g[x]) # sec

            ans = []
            while x != n: # 현재 x: 17, path를 활용해 경로 거슬러 올라감
                ans.append(x) # 현재 위치 추가
                x = path[x] # 이전 위치 저장
            ans.append(n) # 최초 시작위치 추가
            ans.reverse()
            print(' '.join(map(str, ans))) # for문 대신 문자열로 출력
            return
        
        for nx in [x+1, x-1, x*2]:
            if 0 <= nx < length and g[nx] == 0:
                g[nx] = g[x] + 1
                q.append(nx)
                path[nx] = x # nx 로 x(이전 위치) 알아낼 수 있음

bfs()