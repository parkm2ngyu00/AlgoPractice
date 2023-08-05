import sys
sys.setrecursionlimit(150000)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 1

def dfs(t):
    global cnt
    visited[t] = cnt
    for i in graph[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort()

dfs(r)
for i in range(1, n+1):
    print(visited[i])
