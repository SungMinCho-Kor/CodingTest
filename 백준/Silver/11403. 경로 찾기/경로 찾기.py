import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if row[j] == 1:
            graph[i].append(j)

visit = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

for start in range(N):
    queue.append(start)
    while queue:
        prev = queue.popleft()
        for target in graph[prev]:
            if visit[start][target] == 0:
                visit[start][target] = 1
                queue.append(target)
                
for line in visit:
    print(*line)