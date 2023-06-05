'''
설계
바깥 흰 부분에서 4방향 체크해서 치즈면 c로 만들기(c개수 체크)
시간 +=1
c 흰색으로 만들기

시간이랑 c개수 출력

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
# print(check)

def dfs(i,j):
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx,ny)
h = 0
while check!=board:
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    dfs(0,0)
    cnt = 0
    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<n and 0<=ny<m and visit[i][j]==1 and board[nx][ny]==1:
                    board[nx][ny] = 0
                    cnt+=1
    h+=1
    
print(h)
print(cnt)
    