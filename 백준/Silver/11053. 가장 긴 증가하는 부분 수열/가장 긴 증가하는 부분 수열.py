import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

# 자기 자신을 끝으로 할 때 가장 긴 수열
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    maximum = 0
    min_list = [x for x in input_list[:i] if x < input_list[i]]
    idx_list = []
    for value in min_list:
        idx_list += [i for i, x in enumerate(input_list) if x == value]
    if len(idx_list) == 0:
        dp[i] = 1
    else:
        for j in idx_list:
            maximum = max(maximum, dp[j])
        dp[i] = maximum + 1

print(max(dp))