import sys

n = int(sys.stdin.readline())

if n == 1:
    print('*')
else:
    for k in range(n):
        if k % 2 == 0:
            for i in range(n):
                print('* ', end='')
            print()
        else:
            for i in range(n):
                print(' *', end='')
            print()