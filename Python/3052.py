import sys

num_list = []

res_list = []

for i in range(10):
    x = int(sys.stdin.readline())
    num_list.append(x)
    res = x % 42
    res_list.append(res)

# 중복을 없애기 위해서 집합을 만들어 주는 아이디어 기억하기
res_set = set(res_list)

if len(res_set) == 0:
    print(1)
else:
    print(len(res_set))