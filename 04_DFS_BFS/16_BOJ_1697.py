# 숨바꼭질 https://www.acmicpc.net/problem/1697
# 풀이: 100,000 그래프 0으로 / bfs 1로 변경, / nx가 동생 위치일 때 리턴
# 알게된점: dx 리스트에 *2를 담는게 될까 했는데, for문에서 바로 현재위치와 계산한 값을 사용하면 된다.

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
graph = [0] * 100001

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        n = q.popleft()
        if n == k:
            print(graph[n])
            return
        
        for next_n in [n - 1, n + 1, n * 2]:
            if 0 <= next_n <= 100000 and graph[next_n] == 0:
                graph[next_n] = graph[n] + 1
                q.append(next_n)

bfs(n, k)