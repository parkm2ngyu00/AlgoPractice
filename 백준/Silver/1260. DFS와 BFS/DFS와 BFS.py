from collections import deque

n, m, v = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n+1)] # 1번부터 n번까지 정점 사용

# 간선 처리
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1) # 단방향이면 이거 주석처리 하면 됨

for i in range(1, n+1):
    graph[i].sort() # 순서 보정을 위해 오름차순 정렬 필요

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(n + 1)]
    queue.append(start)
    visited[start] = 1
    while len(queue) > 0:
        curr = queue[0]
        print(curr, end=' ')
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
        queue.popleft()

visit = [0 for _ in range(n + 1)]
visit[v] = 1

def dfs(curr):
    print(curr, end=' ')
    for nxt in graph[curr]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            dfs(nxt)

dfs(v)
print()
bfs(v)