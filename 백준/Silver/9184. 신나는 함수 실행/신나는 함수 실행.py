import sys

input = sys.stdin.readline

dp = [[[0 for _ in range(20+1)] for _ in range(20+1)] for _ in range(20+1)]
for i in range(20+1):
    for j in range(20+1):
        for k in range(20+1):
            if i == 0 or j == 0 or k == 0:
                dp[i][j][k] = 1
            elif i<j<k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a<=0 or b<=0 or c<=0:
        ta = tb = tc = 0
    elif a>20 or b>20 or c>20:
        ta = tb = tc = 20
    else:
        ta, tb, tc = a, b, c
    
    print(f"w({a}, {b}, {c}) = {dp[ta][tb][tc]}")