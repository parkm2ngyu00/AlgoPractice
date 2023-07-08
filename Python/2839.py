import sys

n = int(sys.stdin.readline())
list_sum = []

for x in range(n):
    for y in range(n):
        if (n == 3 * x + 5 * y):
            list_sum.append(x + y)

if len(list_sum) == 0:
    print(-1)
else:
    print(min(list_sum))