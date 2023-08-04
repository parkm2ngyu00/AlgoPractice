from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0 
    return

T = int(input())
res_list = []

for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                bfs(i, j)
                count += 1
    res_list.append(count)

for i in res_list:
    print(i)