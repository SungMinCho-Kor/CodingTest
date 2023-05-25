import sys

n,m = map(int,sys.stdin.readline().split())
ls = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    i-=1
    j-=1
    for k in range((i+j)//2 + 1 - i):
        ls[i + k], ls[j-k] = ls[j-k], ls[i+k]
for i in ls:
    print(i,end=" ")