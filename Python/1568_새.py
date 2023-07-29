import sys

n = int(sys.stdin.readline())

k = 1
count = 0
sum = 0
while True:
    if sum == n:
        break
    if sum + k > n:
        k = 1
        sum += k
    else:
        sum += k
    k += 1
    count += 1

print(count)