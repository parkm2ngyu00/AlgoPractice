import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = cnt
    while len(queue) > 0:
        curr = queue.popleft()
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                cnt += 1
                visited[nxt] = cnt
                queue.append(nxt)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(n+1):
    graph[i].sort(reverse=True)

bfs(r)
for i in range(1, n+1):
    print(visited[i])