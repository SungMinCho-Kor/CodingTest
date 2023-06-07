
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

q = deque()
q.append(n)
visit = [0]*100001
distance = [0] * 100001
visit[n] = 1
while q:
    l = q.popleft()
    
    if visit[k]!=0:
        print(distance[k])
        break
    if 0<=l*2<=100000 and visit[l*2]==0:
        visit[l*2] = 1
        distance[l*2] = distance[l]
        q.append(l*2)
    if 0<=l-1<=100000 and visit[l-1]==0:
        visit[l-1]=1
        distance[l-1] = distance[l] + 1
        q.append(l-1)
    if 0<=l+1<=100000 and visit[l+1]==0:
        visit[l+1]=1
        distance[l+1] = distance[l] + 1
        q.append(l+1)