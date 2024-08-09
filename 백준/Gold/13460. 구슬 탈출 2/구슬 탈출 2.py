import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
board = []

for i in range(n):
    row = list(input())
    board.append(row)
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def lean_color(k, ci, cj):
    nci = ci
    ncj = cj
    while True:
        nci += dx[k]
        ncj += dy[k]
        if board[nci][ncj] == '#':
            nci -= dx[k]
            ncj -= dy[k]
            break
        elif board[nci][ncj] == 'O':
            break
    return nci, ncj

def lean(direction, ri, rj, bi, bj):
    nri, nrj = lean_color(direction, ri, rj)
    nbi, nbj = lean_color(direction, bi, bj)
    red_flag = False
    blue_flag = False
    if board[nri][nrj] == 'O':
        red_flag = True
    if board[nbi][nbj] == 'O':
        blue_flag = True
    if nri == nbi and nrj == nbj:
        if abs(ri - nri) + abs(rj - nrj) > abs(bi - nbi) + abs(bj - nbj):
            nri -= dx[direction]
            nrj -= dy[direction]
        else:
            nbi -= dx[direction]
            nbj -= dy[direction]
    return nri, nrj, nbi, nbj, red_flag, blue_flag
        
    
def bfs(ri, rj, bi, bj):
    cnt = 0 
    visit = []
    queue = deque()
    queue.append((ri, rj, bi, bj))
    while queue:
        for _ in range(len(queue)):
            ri, rj, bi, bj = queue.popleft()
            if (ri, rj, bi, bj) in visit:
                continue
            visit.append((ri, rj, bi, bj))
            for k in range(4):
                nri, nrj, nbi, nbj, red_flag, blue_flag = lean(k, ri, rj, bi, bj)
                if blue_flag:
                    continue
                if red_flag:
                    return cnt + 1 
                elif not blue_flag:
                    queue.append((nri, nrj, nbi, nbj))
        cnt += 1
        if cnt >= 10:
            return -1
    return -1
print(bfs(ri, rj, bi, bj))