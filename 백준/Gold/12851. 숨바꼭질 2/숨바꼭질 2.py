


'''
1초
현재 위치 : x
3가지 선택지 : x-1, x+1, 2*x

n위치에서 k위치까지 최단시간 구하기
최단시간 -> BFS
'''

import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())

visit = [[0,0] for _ in range(100001)]

q = [n]
if n==k:
    print(0)
    print(1)
    sys.exit()
while q:
    tmp = q[:]
    q=[]
    while tmp:
        loc = tmp.pop(0)
        if 0<=loc-1<=100000 and (visit[loc-1][0] == 0 or visit[loc][0]+1 == visit[loc-1][0]):
            visit[loc-1][0] = visit[loc][0] + 1
            visit[loc-1][1] += 1
            q.append(loc-1)
        if 0<=loc+1<=100000 and (visit[loc+1][0] == 0 or visit[loc][0]+1 == visit[loc+1][0]):
            visit[loc+1][0] = visit[loc][0] + 1
            visit[loc+1][1] += 1
            q.append(loc+1)
        if 0<=loc*2<=100000 and (visit[loc*2][0] == 0 or visit[loc][0]+1 == visit[loc*2][0]):
            visit[loc*2][0] = visit[loc][0] + 1
            visit[loc*2][1] += 1
            q.append(loc*2)
    if visit[k][1]>0:
        print(visit[k][0])
        print(visit[k][1])
        break
    
    