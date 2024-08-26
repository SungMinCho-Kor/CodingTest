import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

def check(board):
    cnt = 0
    for i in range(5):
        if board[i] == [-1, -1, -1, -1, -1]:
            cnt += 1
        if [j[i] for j in board] == [-1, -1, -1, -1, -1]:
            cnt += 1
    if [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]] == [-1, -1, -1, -1, -1]:
        cnt += 1
    if [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]] == [-1, -1, -1, -1, -1]:
        cnt += 1
    return cnt >= 3
for i in range(5):
    for j in range(5):
        for p in range(5):
            for q in range(5):
                if board[p][q] == call[i][j]:
                    board[p][q] = -1
                    if check(board):
                        print((i) * 5 + j + 1)
                        exit(0)