'''
맞닿은 부분의 극이 같으면 회전X
극이 다르면 반대방향으로 회전
하나가 회전하면 그 옆에 회전하는 애들도 회전하고 
그것때문에 연쇄작용으로 회전해도 회전 시켜야 함.
'''

import sys

t = int(sys.stdin.readline())
gears = [list(sys.stdin.readline().rstrip()) for _ in range(t)]
k = int(sys.stdin.readline())


for _ in range(k):
    n,d = map(int,sys.stdin.readline().split())
    directions = [0]*t
    directions[n-1] = d
    for i in range(n-1,0,-1):
        if gears[i][-2] == gears[i-1][2]:
            break
        if directions[i]==1:
            directions[i-1] = -1
        else:
            directions[i-1] = 1
    for i in range(n-1,t-1):
        if gears[i][2]==gears[i+1][-2]:
            break
        if directions[i]==1:
            directions[i+1] = -1
        else:
            directions[i+1] = 1
    for i in range(t):#회전
        if directions[i]==1:
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        elif directions[i]==-1:
            gears[i] = gears[i][1:] + [gears[i][0]]
cnt = 0
for gear in gears:
    if gear[0] == '1':
        cnt+=1
print(cnt)
        