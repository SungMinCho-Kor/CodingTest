import sys
import copy
from collections import deque

board = [list(sys.stdin.readline().rstrip().split()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer_set = set()

def dfs(i, j, string):
    if len(string) == 6:
        answer_set.add(string)
        return
    
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, string + board[nx][ny])
    
for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(answer_set))