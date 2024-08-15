
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

v, e = map(int, input().split())

graph = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key = lambda x: x[2])

def find(parent, k):
    if parent[k] == k:
        return k
    parent[k] = find(parent, parent[k])
    return parent[k]

def union(parent, a, b):
    p_a = find(parent, a)
    p_b = find(parent, b)
    
    if p_a != p_b:
        parent[p_b] = p_a
    
answer = 0
for a, b, c in graph:
    # 부모는 a 와 b 중 작은 것을 따라간다고 하자.
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += c
        
print(answer)