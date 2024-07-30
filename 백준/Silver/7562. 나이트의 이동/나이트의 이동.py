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
    point = tuple(map(int, sys.stdin.readline().rstrip().split()))
    target_point = tuple(map(int, sys.stdin.readline().rstrip().split()))
    
    if point == target_point:
        print(0)
        continue
    
    board = [[0 for _ in range(l)] for _ in range(l)]
    tmp_i, tmp_j = point
    board[tmp_i][tmp_j] = 1
    
    queue = deque()
    queue.append(point)
    
    while queue:
        i, j = queue.popleft()
        for k in range(8):
            nx = dx[k] + i
            ny = dy[k] + j
            
            if 0<=nx<l and 0<=ny<l and board[nx][ny] == 0:
                board[nx][ny] = board[i][j] + 1
                if (nx, ny) == target_point:
                    print(board[nx][ny] - 1)
                    queue = deque() # while 과 for 둘다 끝내기
                    break
                else:
                    queue.append((nx, ny))
    