import sys
from itertools import permutations

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

max_ans = 0

# permutations : 3P2 = 3 * 2
# combinations : 3C2 = (3 * 2) / 2
for i in permutations(num_list):
    result = 0
    for j in range(n-1):
        result += abs(i[j] - i[j+1])
    max_ans = max(max_ans, result)

print(max_ans)