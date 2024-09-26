import sys

N = int(sys.stdin.readline())

dp = [0] *(N+1)
nums = [i*i for i in range(1, 334)]
for i in range(1, N + 1):
   tmp = []
   for j in nums:
      if j>i:
         break
      tmp.append(dp[i - j])
   dp[i] = min(tmp) + 1
print(dp[-1])