import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visit = [False for _ in range(n + 1)]
visit [0] = True

def dfs(result, visit, k):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(k, n+1):
        if visit[i] == False:
            visit[i] = True
            dfs(result + [i], visit, i)
            visit[i] = False

dfs([], visit, 1)