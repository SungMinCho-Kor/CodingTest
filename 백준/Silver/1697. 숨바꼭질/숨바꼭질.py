
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

queue = deque()
queue.append(N)

MAX = 100000
distance = [0] * (MAX + 1)

while queue:
    location = queue.popleft()
    if location == K:
        print(distance[location])
        break
    for loc in (location - 1, location + 1, location * 2):
        if 0<= loc <= MAX and distance[loc] == 0:
            distance[loc] = distance[location] + 1
            queue.append(loc)
            
            