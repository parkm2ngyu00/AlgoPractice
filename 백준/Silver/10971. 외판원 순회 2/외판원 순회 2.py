import sys

N = int(sys.stdin.readline())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

min_value = float('inf')

def dfs_backtracking(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if matrix[next][start] != 0:
            min_value = min(min_value, value + matrix[next][start])
            return
    for i in range(N):
        if matrix[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value+matrix[next][i], visited)
            visited.pop()
    return

for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)