import sys

# a, b, c = map(int, sys.stdin.readline().split())
# time = []

# for i in range(3):
#     time.append(list(map(int, sys.stdin.readline().split())))

# truck1 = [x for x in range(time[0][0], time[0][1])]
# truck2 = [x for x in range(time[1][0], time[1][1])]
# truck3 = [x for x in range(time[2][0], time[2][1])]

# count1 = count2 = count3 = 0

# min = min(time, key=lambda x : x[0])[0]
# max = max(time, key=lambda x : x[1])[1]

# for i in range(min, max+1):
#     if i in truck1 and i in truck2 and i in truck3:
#         count3 += 1
#     elif (i in truck1 and i in truck2) or (i in truck1 and i in truck3) or (i in truck2 and i in truck3):
#         count2 += 1
#     elif i in truck1 or i in truck2 or i in truck3:
#         count1 += 1

# print(count1 * a * 1 + count2 * b * 2 + count3 * c * 3)

a, b, c = map(int, input().split())
time_table = [0]*101
for i in range(3):
    arrive, depart = map(int, input().split())
    for j in range(arrive, depart):
        time_table[j] += 1

answer = 0
for k in time_table:
    if k == 1:
        answer += a * k
    elif k == 2:
        answer += b * k
    elif k == 3:
        answer += c * k

print(answer)