import sys

n,m = map(int,sys.stdin.readline().split())
basket = [0 for _ in range(n)]
for _ in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    for p in range(i-1,j):
        basket[p] = k
for i in basket:
    print(i,end = " ")
