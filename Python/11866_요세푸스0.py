import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
result_list = []

for i in range(1, n+1):
    queue.append(i)

i = k-1

while len(queue) > 0:
    queue.rotate(-i)
    num = queue.popleft()
    result_list.append(num)

result = str(result_list)[1:-1]
print('<', end='')
print(result, end='')
print('>')