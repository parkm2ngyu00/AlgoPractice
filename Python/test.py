import sys

n = int(sys.stdin.readline())

result = 0
fib_list = [0, 1]
for i in range(n):
    next = fib_list[-1] + fib_list[-2]
    fib_list.append(next)

print(fib_list[-2])