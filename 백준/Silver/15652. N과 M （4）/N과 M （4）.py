import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def dfs(arr, k):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(k, n+1):
        dfs(arr + [i], i)

dfs([], 1)