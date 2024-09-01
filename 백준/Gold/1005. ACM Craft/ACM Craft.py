import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

t = int(input())
    
def func(graph, w, d, visit):
    if visit[w]:
        return d[w]
    if not graph[w]:
        visit[w] = True
        return d[w]
    max_value = 0
    for g in graph[w]:
        max_value = max(max_value, func(graph, g, d, visit))
    visit[w] = True
    d[w] += max_value
    return d[w]

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y-1].append(x-1)
    w = int(input())
    visit = [False] * n
    print(func(graph, w-1, d, visit))