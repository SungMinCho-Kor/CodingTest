'''
BFS


'''

import sys
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    l = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    target_x, target_y = map(int, sys.stdin.readline().rstrip().split())
    
    if x == target_x and y == target_y:
        print(0)
        continue
    
    board = [[-1 for _ in range(l)] for _ in range(l)]
    board[x][y] = 0
    
    queue = deque()
    queue.append((x, y))
    
    break_flag = False
    while queue and not break_flag:
        i, j = queue.popleft()
        for k in range(8):
            nx = dx[k] + i
            ny = dy[k] + j
            
            if 0<=nx<l and 0<=ny<l and board[nx][ny] == -1:
                board[nx][ny] = board[i][j] + 1
                if nx == target_x and ny == target_y:
                    print(board[nx][ny])
                    break_flag = True
                    break
                else:
                    queue.append((nx, ny))
    