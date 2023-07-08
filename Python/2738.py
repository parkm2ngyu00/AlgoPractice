import sys

n, m = map(int, sys.stdin.readline().split())

A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(m)] for _ in range(n)]
C = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        A[i][j] = num_list[j]

for i in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        B[i][j] = num_list[j]

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j], end=' ')
    print()