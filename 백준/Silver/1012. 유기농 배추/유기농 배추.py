import sys
sys.setrecursionlimit(10000) # 백준에서 재귀로 문제를 풀 때 반드시 해줘야 함 (재귀 횟수에 제한이 있기 때문)

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                dfs(nx, ny)
                
for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for x in range(n):
        for y in range(m):
            if field[x][y] == 1:
                dfs(x, y)
                count += 1
    print(count)