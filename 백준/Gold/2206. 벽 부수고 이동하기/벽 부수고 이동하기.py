'''
1. 벽의 좌표를 보관
2. 벽을 부수지 않고 BFS
3. 벽을 하나씩 부수며 BFS

원래 맵
0   0   0   0
-1 -1  -1   0 
-1  0   0   0
0   0   0   0
0  -1  -1  -1
0   0   0   0

1  2  3  4
         5
    8  7 6
10  9  8 7
11
12 13 14 15

1  2  3  4
2         5
    8  7 6
10  9  8 7
11
12 13 14 15

1  2  3  4
   3     5
    8  7 6
10  9  8 7
11
12 13 14 15




'''

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
left_wall = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = deque()
q.append((0,0,left_wall))
visit[0][0][left_wall] = 1
while q:
    x,y,left_wall = q.popleft()
    if x==n-1 and y==m-1:
        break
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if maps[nx][ny] == 0 and visit[nx][ny][left_wall] == 0:
                visit[nx][ny][left_wall] = visit[x][y][left_wall] + 1
                q.append((nx,ny,left_wall))
            if maps[nx][ny] == 1 and left_wall==1:
                visit[nx][ny][left_wall-1] = visit[x][y][left_wall] + 1
                q.append((nx,ny,left_wall-1))
if visit[n-1][m-1][left_wall] == 0:
    print(-1)
else:
    print(visit[n-1][m-1][left_wall])
                

    
    
    
    
    