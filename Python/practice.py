from collections import deque

queue = deque([3, 7, 2])
queue.append(5)
a = queue.popleft()
print(queue)
print(a)