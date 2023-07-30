n = int(input())

schedule = []

for _ in range(n):
    schedule.append(list(map(int, input().split())))

max_price = 0
for start in range(n):
    can_next = start
    curr_price = 0
    for i in range(start, n):
        if i < can_next:
            continue
        can_next += schedule[i][0]
        if can_next > n:
            break
        curr_price += schedule[i][1]
    max_price = max(max_price, curr_price)
    # print(curr_price)
print(max_price)