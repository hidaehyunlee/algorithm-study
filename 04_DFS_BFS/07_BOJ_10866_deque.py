# https://www.acmicpc.net/problem/10866
# 메모:
# 1. pop(index) 가능

import sys

deque = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        deque.append(command[1])

    elif command[0] == "push_back":
        deque.insert(0, command[1])

    elif command[0] == "pop_front":
        if len(deque) == 0: print(-1)
        else: print(deque.pop())
    
    elif command[0] == "pop_back":
        if len(deque) == 0: print(-1)
        else: print(deque.pop(0))

    elif command[0] == "size":
        print(len(deque))

    elif command[0] == "empty":
        if len(deque) == 0: print(1)
        else: print(0)

    elif command[0] == "front":
        if len(deque) == 0: print(-1)
        else: print(deque[len(deque) - 1])

    elif command[0] == "back":
        if len(deque) == 0: print(-1)
        else: print(deque[0])
