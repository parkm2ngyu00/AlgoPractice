import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    discard = queue.popleft()
    queue.append(queue[0])
    shuffle = queue.popleft()

print(queue[0])