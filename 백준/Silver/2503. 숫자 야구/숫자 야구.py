import sys
from itertools import permutations

n = int(sys.stdin.readline())
num_list = [x for x in range(1, 10)]
available_list = list(permutations((num_list), 3))

for _ in range(n):
    test, s, b = map(int, sys.stdin.readline().split())
    test = list(str(test))
    remove_cnt = 0
    for i in range(len(available_list)):
        s_cnt = b_cnt = 0
        i -= remove_cnt
        for k in range(3):
            test[k] = int(test[k])
            if test[k] in available_list[i]:
                if test[k] == available_list[i][k]:
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            available_list.remove(available_list[i])
            remove_cnt += 1

print(len(available_list))