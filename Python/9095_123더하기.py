n = int(input())

test = []

for _ in range(n):
    test.append(int(input()))

num_list = [1, 2, 4]

while len(num_list) < 11:
    num_list.append(num_list[-1]+num_list[-2]+num_list[-3])

for i in test:
    print(num_list[i-1])