import sys

num = int(sys.stdin.readline())

space = [[0 for _ in range(100)] for _ in range(100)]

for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            space[k][j] = 1

count = 0

for i in range(100):
    for j in range(100):
        if space[i][j] == 1:
            count += 1

print(count)