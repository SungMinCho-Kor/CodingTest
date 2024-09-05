import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    parent[b] = a

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 1:#검사
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:#합집합
        union(a, b)