import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    if i < n-1:
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
for i in range(2, n):
    p, q = 0, i
    while p < n and q < n:
        if dp[p+1][q-1] == 1 and nums[p] == nums[q]:
            dp[p][q] = 1
        p+=1
        q+=1

for _ in range(m):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    print(dp[p][q])