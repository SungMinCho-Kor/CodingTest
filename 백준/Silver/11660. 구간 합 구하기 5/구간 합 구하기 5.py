import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split()))for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = table[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i-1] + table[0][i]
    dp[i][0] = dp[i-1][0] + table[i][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 > 0 and y1 > 0:
        print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))
    elif x1 > 0:
        print(dp[x2][y2] - dp[x1 - 1][y2])
    elif y1 > 0:
        print(dp[x2][y2] - dp[x2][y1 - 1])
    else:
        print(dp[x2][y2])