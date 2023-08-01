natural_number = set(range(1, 10001))
self_number = set()

def self_num(n):
    new_num = sum(list(map(int, str(n)))) + n
    return new_num


for i in range(1, 10001):
    n = self_num(i)
    self_number.add(n)


number = sorted(natural_number - self_number)

for i in number:
    print(i)