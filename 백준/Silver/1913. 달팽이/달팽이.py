import sys
import math

n = int(sys.stdin.readline())
search = int(sys.stdin.readline())
result_search = [0, 0]

max = n ** 2
space = [[0 for _ in range(n)] for _ in range(n)]
count = 1
num = 2

x = y = (n // 2)

if count == search:
        result_search[0] = x
        result_search[1] = y
        
space[x][y] = count
count += 1
x -= 1

def cycle(num):
    global count, x, y
    for i in range(num):
        if count == search:
            result_search[0] = x
            result_search[1] = y
        space[x][y] = count
        y += 1
        count += 1
    y -= 1
    x += 1
    for i in range(num):
        if count == search:
            result_search[0] = x
            result_search[1] = y
        space[x][y] = count
        x += 1
        count += 1
    x -= 1
    y -= 1
    for i in range(num):
        if count == search:
            result_search[0] = x
            result_search[1] = y
        space[x][y] = count
        count += 1
        y -= 1
    y += 1
    x -= 1
    for i in range(num):
        if count == search:
            result_search[0] = x
            result_search[1] = y
        space[x][y] = count
        count += 1
        x -= 1

def get_even_numbers(n):
    even_numbers = []
    for i in range(2, n, 2):
        even_numbers.append(i)
    return even_numbers

results = get_even_numbers(n)
for result in results:
    cycle(result)


for i in range(n):
    for j in range(n):
        print(space[i][j], end=' ')
    print()

print(result_search[0]+1, result_search[1]+1)