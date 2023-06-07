
import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

q = deque()
q.append(n)
visit = [-1]*100001
distance = [0] * 100001

visit[n] = n
while q:
    l = q.popleft()
    
    if visit[k]!=-1:
        print(distance[k])
        break
    if 0<=l*2<=100000 and visit[l*2]==-1:
        visit[l*2] = l
        distance[l*2] = distance[l] + 1
        q.append(l*2)
    if 0<=l-1<=100000 and visit[l-1]==-1:
        visit[l-1]=l
        distance[l-1] = distance[l] + 1
        q.append(l-1)
    if 0<=l+1<=100000 and visit[l+1]==-1:
        visit[l+1]=l
        distance[l+1] = distance[l] + 1
        q.append(l+1)

path = []
tmp = k
path.append(k)
for _ in range(distance[k]):
    path.append(visit[tmp])
    tmp = visit[tmp]
for i in path[::-1]:
    print(i,end=" ")

