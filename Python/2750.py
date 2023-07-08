import sys

n = int(sys.stdin.readline())

num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])