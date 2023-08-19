import sys
from collections import deque

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 감
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 감

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
x, y, size = 0, 0, 2
count = 0
result = 0

#상어위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x = i
            y = j

def bfs(x, y, shark_size):
    distance = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    temp = []
    while len(queue) > 0:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] <= shark_size and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                distance[nx][ny] = distance[cx][cy] + 1
                if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                    temp.append((nx, ny, distance[nx][ny]))
    # 내림차순 정렬하는 이유는 아래서 pop을 사용하기 때문
    return sorted(temp, key=lambda x : (x[2], x[0], x[1]))

while True:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark[0]
    # 움직이는 칸수가 곧 시간이 됨
    result += dist
    graph[x][y], graph[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨줌
    x, y = nx, ny
    count += 1
    # 사이즈 커지는지 확인
    if count == size:
        size += 1
        count = 0

print(result)