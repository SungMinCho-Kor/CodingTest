import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

queue = []

for _ in range(m):
    a, b, c = map(int, input().split())
    queue.append((c, a, b))
queue.sort()

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

answer = 0
for cost, a, b in queue:
    if find(a) != find(b):
        union(a, b)
        answer += cost
print(answer)