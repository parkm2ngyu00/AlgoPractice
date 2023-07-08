import sys

n, m = map(int, sys.stdin.readline().split())

bag = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp = bag[i-1]
    bag[i-1] = bag[j-1]
    bag[j-1] = temp

for i in range(len(bag)):
    print(bag[i], end=' ')