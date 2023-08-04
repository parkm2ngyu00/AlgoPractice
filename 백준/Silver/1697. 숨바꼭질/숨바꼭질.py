from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001
max = 100000

def bfs(n):
    queue = deque()
    queue.append(n)
    while len(queue) > 0:
        curr = queue.popleft()
        if curr == k:
            print(dist[curr])
            break
        for next in (curr+1, curr-1, curr*2):
            if 0 <= next <= max and dist[next] == 0:
                dist[next] = dist[curr] + 1
                queue.append(next)

bfs(n)