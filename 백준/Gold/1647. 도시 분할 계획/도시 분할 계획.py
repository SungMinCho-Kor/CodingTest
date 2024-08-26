import sys
import heapq

input = sys.stdin.readline
n,m = map(int, input().split())

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

queue = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

answer = []
while queue:
    c, a, b = heapq.heappop(queue)
    if find(a) == find(b):
        continue
    union(a, b)
    answer.append(c)
print(sum(answer) - max(answer))