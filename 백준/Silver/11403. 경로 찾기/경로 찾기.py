import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N)]
maps = []
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if maps[i][j] == 1:
            graph[i].append(j)

visit = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

for i in range(N):
    queue.append(i)
    while queue:
        p = queue.popleft()
        for q in graph[p]:
            if visit[i][q] == 0:
                visit[i][q] = 1
                queue.append(q)
for line in visit:
    print(*line)