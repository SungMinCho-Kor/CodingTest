'''



'''

import sys
n,m = map(int,sys.stdin.readline().split())

nums =list(map(int,sys.stdin.readline().split()))
visit = [False] * n
nums.sort()
def dfs(ls):
    if len(ls)==m:
        print(" ".join(map(str,ls)))
        return
    overlap = 0
    for i in range(n):
        if visit[i]==False and overlap != nums[i]:
            visit[i] = True
            overlap = nums[i]
            dfs(ls + [nums[i]])
            visit[i] = False
dfs([])