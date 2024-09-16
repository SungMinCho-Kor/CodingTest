import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(dp[i] + nums[i])
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])
    