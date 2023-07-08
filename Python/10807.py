import sys

n = int(sys.stdin.readline())

num_list = list(map(int, input().split()))

v = int(sys.stdin.readline())

count = 0

for i in num_list:
    if i == v:
        count += 1
    else:
        continue

print(count)