import sys

import sys

n, v = map(int, sys.stdin.readline().split())

num_list = list(map(int, input().split()))

count = 0

result_list = []

for i in num_list:
    if i < v:
        result_list.append(i)
    else:
        continue

for i in result_list:
    print(i, end=' ')