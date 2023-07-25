a = [] # 행렬 a 입력
n,m = map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))

b = [] # 행렬 b 입력
m,k = map(int,input().split())
for i in range(m):
    b.append(list(map(int,input().split())))

c = [] # 행렬 c 생성
for i in range(n): # a의 행
    c.append([])
    for j in range(k): # b의 열
        temp = 0
        for l in range(m): # a의 열, b의 행
            temp += a[i][l] * b[l][j]
        c[i].append(temp)

for i in range(n):
    for j in range(k):
        print(c[i][j], end=' ')
    print()
