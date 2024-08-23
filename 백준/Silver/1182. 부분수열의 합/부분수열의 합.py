import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
def dfs(arr, start):
    global answer
    if arr and sum(arr) == s:
        answer += 1
    
    for i in range(start + 1, n):
        dfs(arr + [numbers[i]], i)

dfs([], -1)
print(answer)