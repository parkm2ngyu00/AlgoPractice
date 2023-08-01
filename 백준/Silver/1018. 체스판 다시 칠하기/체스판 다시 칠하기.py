import sys

n, m = map(int, sys.stdin.readline().split())
board = list()
black_start_board = list()
white_start_board = list()

for i in range(8):
    if i % 2 == 0:
        white_start_board.append(list('WBWBWBWB'))
    else:
        white_start_board.append(list('BWBWBWBW'))

for i in range(8):
    if i % 2 == 1:
        black_start_board.append(list('WBWBWBWB'))
    else:
        black_start_board.append(list('BWBWBWBW'))

for i in range(n):
    temp_list = []
    temp_list = list(input())
    board.append(temp_list)

min = 32

for i in range(n-7):
    for j in range(m-7):
        white_count = 0
        black_count = 0
        for w, k in enumerate(range(i, i+8)):
            for q, p in enumerate(range(j, j+8)):
                if white_start_board[w][q] != board[k][p]:
                    white_count += 1
        for w, k in enumerate(range(i, i+8)):
            for q, p in enumerate(range(j, j+8)):
                if black_start_board[w][q] != board[k][p]:
                    black_count += 1
        count = black_count if black_count < white_count else white_count
        if count < min:
            min = count

print(min)