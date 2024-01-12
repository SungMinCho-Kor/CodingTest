import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(N - 1):
    point1, point2 = map(int, sys.stdin.readline().rstrip().split())
    graph[point1].append(point2)
    graph[point2].append(point1)

queue = deque()
queue.append(1)
parents = [ 0 for _ in range(N+1) ]

while queue:
    parent = queue.popleft()
    for point in graph[parent]:
        if parents[point] == 0:
            parents[point] = parent
            queue.append(point)
for i in range(2, N+1):
    print(parents[i])