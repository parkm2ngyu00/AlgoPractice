N, M, x, y, k = map(int, input().split())

dice_map = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    temp = []
    temp = input().split()
    for j in range(M):
        dice_map[i][j] = int(temp[j])

command_list = list(map(int, input().split()))

# 입력 끝, 추후 구현