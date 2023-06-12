'''
H F D 끝
H F J A D G 

DFS()로 해보자.

'''

import sys

n,m = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

visit = [False]*26


cnt = 0
def dfs(i,j,tmp,visit):
    global cnt    
    cnt = max(tmp,cnt)
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<n and 0<=ny<m and visit[ord(board[nx][ny]) - ord('A')] == False:
            visit[ord(board[nx][ny]) - ord('A')] = True
            dfs(nx,ny,tmp+1, visit)
            visit[ord(board[nx][ny]) - ord('A')] = False
visit[ord(board[0][0]) - ord('A')] = True
dfs(0,0,1, visit)
print(cnt)