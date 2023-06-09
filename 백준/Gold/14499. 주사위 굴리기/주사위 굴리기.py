'''

'''

import sys

n,m,x,y,k = map(int,sys.stdin.readline().split())

maps = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ops = list(map(int,sys.stdin.readline().split()))
dice = [0,0,0,0,0,0]
newdice = [0,0,0,0,0,0]
#다이스 움직임 설정 dice[0]이 제일 위 dice[2]가 바닥
#동:1 / 서 : 2 / 남 : 4 / 북 : 3
#동 -> [0,1,2,3,4,5] -> [3,0,1,2,4,5]
#서 -> [0,1,2,3,4,5] -> [1,2,3,0,4,5]
#남 -> [0,1,2,3,4,5] -> [4,1,5,3,2,0]
#북 -> [0,1,2,3,4,5] -> [5,1,4,3,0,2]


for op in ops:
    if op == 1:#동
        if y+1>=m:
            continue
        y+=1
        newdice[0] = dice[3]
        newdice[1] = dice[0]
        newdice[2] = dice[1]
        newdice[3] = dice[2]
        newdice[4] = dice[4]
        newdice[5] = dice[5]
        dice = newdice[:]
    elif op == 2:#서
        if y-1<0:
            continue
        y-=1
        newdice[0] = dice[1]
        newdice[1] = dice[2]
        newdice[2] = dice[3]
        newdice[3] = dice[0]
        newdice[4] = dice[4]
        newdice[5] = dice[5]
        dice = newdice[:]
    elif op == 3:#북
        if x-1<0:
            continue
        x-=1
        newdice[0] = dice[5]
        newdice[1] = dice[1]
        newdice[2] = dice[4]
        newdice[3] = dice[3]
        newdice[4] = dice[0]
        newdice[5] = dice[2]
        dice = newdice[:]
    elif op == 4:#남
        if x+1>=n:
            continue
        x+=1
        newdice[0] = dice[4]
        newdice[1] = dice[1]
        newdice[2] = dice[5]
        newdice[3] = dice[3]
        newdice[4] = dice[2]
        newdice[5] = dice[0]
        dice = newdice[:]
    if maps[x][y]==0:
        maps[x][y] = dice[2]
    else:
        dice[2] = maps[x][y]
        maps[x][y] = 0
    print(dice[0])
        
    