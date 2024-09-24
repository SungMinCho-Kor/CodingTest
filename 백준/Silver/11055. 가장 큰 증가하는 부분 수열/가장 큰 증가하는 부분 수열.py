import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = a[0]
answer = a[0]
for i in range(1, n):
    max_val = 0
    for j in range(i):
        if a[i] > a[j]:
            dp[i][j] = dp[j][j]
        if max_val < dp[i][j]:
            max_val = dp[i][j]
    dp[i][i] = max_val + a[i]
    if dp[i][i] > answer:
        answer = dp[i][i]
print(answer)