import sys

# 내 코드
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

# 프로님 코드
n = int(sys.stdin.readline())

answer = -1
for five in range(n//5*5, -1, -5):
    left = n - five
    if left % 3 == 0:
        answer = five // 5 + left // 3
        break

print(answer)