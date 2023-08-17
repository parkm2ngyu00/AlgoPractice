import sys

n = str(sys.stdin.readline().rstrip())

sorted_list = sorted(n, reverse=True)
print(''.join(sorted_list))