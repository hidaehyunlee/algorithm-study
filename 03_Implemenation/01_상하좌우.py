# 5
# R R R U D D
# 3 4

n = int(input())
command = list(input().split())

x = 1
y = 1

for c in command:
    if c == 'L':
        if y != 1:
            y -= 1
    elif c == 'R':
        if y != n:
            y += 1
    elif c == 'U':
        if x != 1:
            x -= 1
    else:
        if x != n:
            x += 1

print(x, y)