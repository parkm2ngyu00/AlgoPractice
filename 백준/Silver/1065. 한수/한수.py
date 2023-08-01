N = int(input())

def number_check(n):
    count = 0
    n = str(n)
    a = int(n[1]) - int(n[0])
    b = int(n[2]) - int(n[1])
    if a == b:
        return 1
    else:
        return 0

num = 0

if N >= 100:
    for i in range(100, N + 1):
        num += number_check(i)
    print(99 + num)

elif N < 100 and N >= 1:
    print(N)