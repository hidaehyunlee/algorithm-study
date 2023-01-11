'''
조건: 8*8 좌표평면 밖으로는 나갈 수 없음. 아래 두 경우로만 이동 가능
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
입력: 좌표평면 상 나이트의 위치 (a1)
출력: 나이트가 이동할 수 있는 경우의 수
'''

# a b c d e f g h
# 1 2 3 4 5 6 7 8

knight = input()
x = int(ord(knight[0]) - ord('a') + 1)
y = int(knight[1])
nexts = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
res = 0

for n in nexts:
    next_x = x + n[0]
    next_y = y + n[1]

    if next_x < 1 or next_x > 8 or next_y < 1 or next_y > 8:
        continue
    else:
        res += 1

print(res)