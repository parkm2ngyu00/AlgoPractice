import sys

n = int(sys.stdin.readline())

dp = [0, 0, 1, 1]

for i in range(4, n+1):
    if i % 2 == 0 and i % 3 == 0:
        min_value = min(dp[i-1], dp[i//2], dp[i//3])
    elif i % 2 == 0:
        min_value = min(dp[i-1], dp[i//2])
    elif i % 3 == 0:
        min_value = min(dp[i-1], dp[i//3])
    else:
        min_value = dp[i-1]
    dp.append(min_value + 1)

print(dp[n])