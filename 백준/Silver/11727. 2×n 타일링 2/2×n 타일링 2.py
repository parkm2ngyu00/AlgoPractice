import sys

n = int(sys.stdin.readline())

dp = [0, 1, 3]

for i in range(3, n+1):
    if i % 2 == 0:
        dp.append(sum(dp) + 2)
    else:
        dp.append(sum(dp) + 1)

print(dp[n] % 10007)