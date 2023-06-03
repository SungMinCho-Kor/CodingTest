import sys
n,m = map(int,sys.stdin.readline().split())
if n-m < m:
    m = n-m
a = 1
b=  1
for i in range(n,n-m,-1):
    a*=i
for i in range(1,m+1):
    b*=i
print(a//b)