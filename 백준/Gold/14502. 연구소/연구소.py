'''
0 : 빈칸
1 : 벽
2 : 바이러스
'''


import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
virusing = [[0]*m for _ in range(n)]
result = []
def dfs(cnt):
    if cnt == 3:#3개 벽 다 세웠다.
        q = deque()
        for i in range(n):
            for j in range(m):
                virusing[i][j] = maps[i][j]
                if virusing[i][j] == 2:
                    q.append([i,j])
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        while q:
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<n and 0<=ny<m and virusing[nx][ny]==0:
                    virusing[nx][ny] = 2
                    q.append([nx,ny])
        safe_area = 0
        for i in range(n):
            safe_area+=virusing[i].count(0)
        result.append(safe_area)
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j]==0:
                maps[i][j] = 1
                dfs(cnt+1)
                maps[i][j] = 0
dfs(0)
print(max(result))