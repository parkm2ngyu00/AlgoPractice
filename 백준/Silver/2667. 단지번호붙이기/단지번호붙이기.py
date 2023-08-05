from collections import deque

n = int(input())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = []

def bfs(x, y):
    loc_count = 0
    queue = deque()
    queue.append((x, y))
    while len(queue) > 0:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                queue.append((nx, ny))
        loc_count += 1
    res.append(loc_count)

count = 0

for i in range(n):
    temp = list(input())
    graph.append(temp)

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            graph[i][j] = '0'
            bfs(i, j)
            count += 1

print(count)
for i in sorted(res):
    print(i)