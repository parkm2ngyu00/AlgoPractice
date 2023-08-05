import sys
from collections import deque
sys.setrecursionlimit(10000)

t = int(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while len(queue) > 0:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if matrix[nx][ny] == 1:
            matrix[nx][ny] = 0
            dfs(nx, ny)

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    count = 0
    for j in range(n):
        for k in range(m):
            if matrix[j][k] == 1:
                matrix[j][k] = 0
                bfs(j, k)
                # dfs(j, k)
                count += 1
    print(count)
