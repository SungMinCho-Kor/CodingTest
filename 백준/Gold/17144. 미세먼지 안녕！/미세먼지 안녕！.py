'''
설계

0 30 7
x 10 0
x 0 20

1. 자신의 + - 양을 저장하는 리스트 만들기

6 -15 +4
x 0 +7
x +6 -8

2. 그 양 만큼 원래 리스트에 + - 해준다.

6 15 11
x 10 7
x 6 12

3. 공기청정기 작동 시킨다.


'''


import sys
r,c,t = map(int,sys.stdin.readline().split())

room = [list(map(int,sys.stdin.readline().split()))for _ in range(r)]

for i in range(r):
    if -1 in room[i]:
        air1= i
        air2 = i+1
        break

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air1, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air1 and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air2, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air2 and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny
        
def spread():
    
    pm = [[0 for _ in range(c)]for _ in range(r)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(r):
        for j in range(c):
            if room[i][j]==-1 or room[i][j]==0:
                continue
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<r and 0<=ny<c and room[nx][ny] != -1:
                    pm[i][j] -= room[i][j]//5
                    pm[nx][ny] += room[i][j]//5
    for i in range(r):
        for j in range(c):
            room[i][j]+=pm[i][j]
for _ in range(t):
    spread()
    air_up()
    air_down()
print(sum(sum(room[i]) for i in range(r))+2)
    
    













