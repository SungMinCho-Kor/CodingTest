import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

q = []
visit = [[False for _ in range(m)] for _ in range(n)]
boxes = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            q.append((i,j))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
time = 0
while q:
    tmp = deque(q[:])
    q = []
    while tmp:
        x,y = tmp.popleft()
        visit[x][y] = True
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == False and boxes[nx][ny] ==0:
                visit[nx][ny] = True
                boxes[nx][ny] = boxes[x][y]+1
                q.append((nx,ny))
    time+=1
for i in boxes:
    if 0 in i:
        print(-1)
        sys.exit()
print(time-1)
    