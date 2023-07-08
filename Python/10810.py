import sys

n, m = map(int, sys.stdin.readline().split())

bag = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(j - i + 1):
        bag[i-1] = k
        i += 1
        if i > j:
            break

for i in range(len(bag)):
    print(bag[i], end=' ')
