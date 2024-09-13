import sys

input = sys.stdin.readline

n = int(input())
local = list(map(int, input().split()))
m = int(input())

local.sort()
local_max = local[-1]
if sum(local) < m:
    print(local_max)
else:
    
    def func(k):
        total = 0
        
        start, end = 0, n-1
        while start < end:
            mid = (start + end)//2
            if local[mid] > k:
                end = mid
            else:
                start = mid + 1
        total += sum(local[:start])
        total += (n - end) * k
        return total
    
    start, end = 0, local_max
    while start <= end:
        mid = (start + end)//2
        result = func(mid)
        if result <= m:
            start = mid + 1
        else:
            end = mid-1
    print(end)