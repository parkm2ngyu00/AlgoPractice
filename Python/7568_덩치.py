import sys

n = int(sys.stdin.readline())
class_list = [[] for _ in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    class_list[i].append(x)
    class_list[i].append(y)

for i in class_list:
    rank = 1
    for j in class_list:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    print(rank, end=' ')