import sys

board = []
zero_points = []

for i in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(9):
        if board[i][j] == 0:
            zero_points.append((i, j))

def make_candidates(i, j):
    candidates = [1,2,3,4,5,6,7,8,9]
    start_i = (i//3) * 3
    start_j = (j//3) * 3
    
    for x in range(start_i, start_i + 3):
        for y in range(start_j, start_j + 3):
            if board[x][y] in candidates:
                candidates.remove(board[x][y])
    for x in range(9):
        if board[i][x] in candidates:
            candidates.remove(board[i][x])
        if board[x][j] in candidates:
            candidates.remove(board[x][j])
    
    return candidates

def dfs(k):
    global stop_flag
    if stop_flag:
        return
    if k == len(zero_points):
        stop_flag = True
        for line in board:
            print(*line)
        return
    
    i, j = zero_points[k]
    candidates = make_candidates(i, j)
    for candidate in candidates:
        board[i][j] = candidate
        dfs(k+1)
        board[i][j] = 0
    
stop_flag = False
dfs(0)