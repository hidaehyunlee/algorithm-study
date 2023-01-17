# https://www.acmicpc.net/problem/10845
# 메모:
# 1. 클래스 말고 그냥 구현
# 2. append 말고 insert(인덱스, 값) 로 구현하면 훨씬 간단
# 3. input 시간초과 -> sys.strin.readline()

import sys

q = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "pop":
        if len(q) == 0: print(-1)
        else: print(q.pop())

    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if len(q) == 0: print(1)
        else: print(0)

    elif command[0] == "front":
        if len(q) == 0: print(-1)
        else: print(q[len(q) - 1])

    elif command[0] == "back":
        if len(q) == 0: print(-1)
        else: print(q[0])

    else:
        q.insert(0, command[1])