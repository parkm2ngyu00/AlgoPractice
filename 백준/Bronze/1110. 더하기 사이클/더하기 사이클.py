n = int(input())
num = n
cnt = 0
while True:
    a = num // 10       # 몫
    b = num % 10        # 나머지
    c = (a + b) % 10        
    num = (b * 10) + c

    cnt += 1
    if (num == n):
        break

print(cnt)
