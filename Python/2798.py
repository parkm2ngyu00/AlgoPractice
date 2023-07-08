import sys

n, m = map(int, sys.stdin.readline().split())

card_list = list(map(int, sys.stdin.readline().split()))

max = 3

for i in range(len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            sum = card_list[i] + card_list[j] + card_list[k]
            if ((sum > max) and (sum <= m)):
                max = sum

print(max)