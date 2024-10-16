import sys
from collections import deque
input = sys.stdin.readline

r, c, n = map(int, input().split())

queue = deque([])

board = []
for i in range(r):
    row = input().rstrip()
    for j in range(c):
        if row[j] == 'O':
            queue.append((i, j))
    board.append(list(row))

n -= 1

while n > 0:
    # 폭탄 없는 곳에 폭탄 설치
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
    n -= 1
    if n == 0 :
        break
    
    # 폭탄 폭발
    while queue:
        bi, bj = queue.popleft()
        board[bi][bj] = '.'
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni = bi+di
            nj = bj+dj
            if 0<=ni<r and 0<=nj<c:
                board[ni][nj] = '.'
    n -= 1
    
    # 다음에 터질 폭탄 queue에 넣기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                queue.append((i, j))
                
for line in board:
    print("".join(line))