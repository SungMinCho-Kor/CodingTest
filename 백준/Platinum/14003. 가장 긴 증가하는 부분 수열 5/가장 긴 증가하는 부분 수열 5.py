import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = []
dp2 = []
for i in range(n):
    start, end = 0, len(dp)-1
    while start <= end:
        mid = (start + end)//2
        if dp[mid] < arr[i]:
            start = mid + 1
        else:
            end = mid - 1
    if start < len(dp):
        dp[start] = arr[i]
    else:
        dp.append(arr[i])
    dp2.append((arr[i], start))
k = len(dp) - 1
answer = []
for i in range(len(dp2) -1 , -1 ,-1):
    if dp2[i][1] == k:
        answer.append(dp2[i][0])
        k-=1
    if k == -1:
        break
print(len(dp))
print(*answer[::-1])