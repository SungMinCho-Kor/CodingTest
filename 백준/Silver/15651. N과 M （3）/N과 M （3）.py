import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        dfs(arr + [i])
dfs([])