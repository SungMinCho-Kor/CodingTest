import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        dfs(result + [i])

dfs([])