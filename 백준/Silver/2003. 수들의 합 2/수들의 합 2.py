import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))

dp = [0]
answer = 0
for i in range(n):
    dp.append(a[i] + dp[i])
start = 0
end = 1
while True:
    if start >= n+1 or end >= n+1:
        break
    if dp[end] - dp[start] == m:
        answer += 1
        start += 1
        end += 1
    elif dp[end] - dp[start] > m:
        start += 1
    else:
        end +=1
print(answer)