from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    print(command)