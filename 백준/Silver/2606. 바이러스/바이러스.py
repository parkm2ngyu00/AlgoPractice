n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(start):
    visited[start] = 1
    for nxt in graph[start]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            dfs(nxt)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(sum(visited)-1)