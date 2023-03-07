# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

request_chess = [1, 1, 2, 2, 2, 8]
current_chess = []
result_chess = []

current_chess = input().split(' ')

for i in range(6):
    x = int(request_chess[i]) - int(current_chess[i])
    result_chess.append(x)

str_chess = [str(i) for i in result_chess]

print(' '.join(str_chess))