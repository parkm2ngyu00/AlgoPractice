from itertools import combinations
import sys

res = []

while True:
    testcase = list(map(int, sys.stdin.readline().split()))
    if testcase[0] == 0:
        break
    k = testcase[0]
    s = testcase[1:]
    for case in combinations(s, 6):
        res.append(case)
    res.append([])

res.pop()
for i in res:
    print(' '.join(map(str, i)))