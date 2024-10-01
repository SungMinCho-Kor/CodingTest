import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]


def down(board):
    stack = [[] for _ in range(6)]
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                stack[j].append(board[i][j])
                board[i][j] = '.'
    for j in range(6):
        i = 11
        for k in range(len(stack[j])):
            board[i][j] = stack[j][k]
            i -= 1
    
di, dj = (0,0,1,-1), (1,-1,0,0)
def erase(board):
    visit = [[False for _ in range(6)] for _ in range(12)]
    queue = deque()
    area = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visit[i][j]:
                queue.append((i, j, board[i][j]))
                erase_queue = deque()
                while queue:
                    p, q, ball = queue.popleft()
                    visit[p][q] = True
                    erase_queue.append((p, q))
                    for k in range(4):
                        ni = di[k] + p
                        nj = dj[k] + q
                        if 0<=ni<12 and 0<=nj<6 and not visit[ni][nj] and board[ni][nj] == ball:
                            queue.append((ni, nj, ball))
                if len(erase_queue) >= 4:
                    area += 1
                    for p, q in erase_queue:
                        board[p][q] = '.'
    return area

connection = 0
while True:
    k = erase(board)
    if k>0:
        connection += 1
    else:
        break
    down(board)
print(connection)