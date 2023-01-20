# 이모티콘 https://www.acmicpc.net/problem/14226
# 이모티콘 s개를 만들기 위한 최소시간
# 연산 3개 클립보드에 모두복사, 모두붙여넣기(클립보드 비어있으면 X), 하나삭제
# 화면에 이미 1개 입력되어있음

# 풀이: bfs 방문표시를 전체 인덱스만큼 만드는게 아니라,
# 2차원 리스트로 화면 이모지 개수, 클립보드 이모지 갯수 둘을 기록해야한다.

from collections import deque

s = int(input()) # 2 <= s <= 1000
visited = [[-1] * (s + 1) for _ in range(s + 1)]

def bfs():
    q = deque()
    q.append((1, 0)) # 화면 이모지 개수, 클립보드 이모지 개수
    visited[1][0] = 0

    while q:
        screen, clip = q.popleft()

        # 1. 화면 이모지 모두 클립보드에 복사
        if visited[screen][screen] == -1:
            visited[screen][screen] = visited[screen][clip] + 1
            q.append((screen, screen))
        # 2. 클립보드에 있는 모든 이모지 화면에 붙여넣기
        if visited[screen + clip][clip] == -1 and screen + clip <= s:
            visited[screen + clip][clip] = visited[screen][clip] + 1
            q.append((screen + clip, clip))
        # 3. 화면에서 하나 삭제
        if visited[screen - 1][clip] == -1 and screen - 1 >= 0:
            visited[screen - 1][clip] = visited[screen][clip] + 1
            q.append((screen - 1, clip))

bfs()
ans = -1
for i in range(s + 1):
    if visited[s][i] != -1:
        if ans == -1 or ans > visited[s][i]:
            ans = visited[s][i]

print(ans)
