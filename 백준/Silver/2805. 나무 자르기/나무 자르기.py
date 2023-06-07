import sys


n,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start = 1
end = max(trees)

while start<=end:
    mid = (start+end)//2
    if sum([tree - mid for tree in trees if tree - mid > 0]) >=m:
        start = mid+1
    else:
        end = mid-1
print(end)
    