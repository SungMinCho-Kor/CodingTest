import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(result, k):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(k+1, n+1):
        dfs(result + [i], i)

dfs([], 0)