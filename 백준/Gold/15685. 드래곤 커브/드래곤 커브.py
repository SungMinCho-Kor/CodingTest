import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [[False for _ in range(101)] for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    sx, sy, d, g = map(int, input().split())
    nx = sx+dx[d]
    ny = sy+dy[d]
    queue = deque([(sx,sy), (nx, ny)])
    board[nx][ny] = True
    board[sx][sy] = True
    
    for _ in range(g):
        l = len(queue)
        x, y = queue[-1]
        for i in range(l):
            nx, ny = queue[l - i - 1]
            next_x, next_y = x + y - ny, - x + y + nx
            queue.append((next_x, next_y))
            board[next_x][next_y] = True
            
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1
            
print(answer)
