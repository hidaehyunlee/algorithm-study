from collections import deque

queue = deque()

# push
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# pop (첫 번째 요소)
queue.popleft() 
print(queue)

# push bottom
queue.appendleft(0)
print(queue)