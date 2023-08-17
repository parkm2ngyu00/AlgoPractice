import sys

N = int(sys.stdin.readline())
array = []

for _ in range(N):
    new = list(map(int, sys.stdin.readline().split()))
    array.append(new)

sorted_list = sorted(array, key=lambda x : (x[0], x[1]))

for i in sorted_list:
    print(i[0], i[1])