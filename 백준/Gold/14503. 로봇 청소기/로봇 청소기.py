'''

청소기는 바라보는 방향이 있다. 
0,0 시작 N-1,M-1 에서 끝.
$d$가 
$0$인 경우 북쪽, 
$1$인 경우 동쪽, 
$2$인 경우 남쪽, 
$3$인 경우 서쪽을 바라보고 있는 것이다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    (1).바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    (2). 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    (1). 반시계 방향으로 90도 회전한다.
    (2). 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    (3). 1번으로 돌아간다.
    
0 : 청소 안된 곳
1 : 벽
2 : 청소한곳으로 하자.

'''

import sys

n, m = map(int, sys.stdin.readline().split())
r,c,d = map(int, sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [-1,0,1,0]
# robot = [r,c]
room = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(robot)
cnt = 0
while True:
    if room[r][c]==0:#1번조건
        room[r][c]=2
        cnt+=1
    if all([room[r+dy[(d+k)%4]][c+dx[(d+k)%4]] for k in range(4) if 0<=r+dy[(d+k)%4]<n and 0<=c+dx[(d+k)%4]<m]):
        if 0<=r+dy[(d+2)%4]<n and 0<=c+dx[(d+2)%4]<m and room[r+dy[(d+2)%4]][c+dx[(d+2)%4]] != 1:
            r+=dy[(d+2)%4]
            c+=dx[(d+2)%4]
            continue
        else:
            break
    else:
        d = (d-1)%4
        if room[r+dy[d]][c+dx[d]] == 0:
            r+=dy[d]
            c+=dx[d]
print(cnt)
        
    
    
    