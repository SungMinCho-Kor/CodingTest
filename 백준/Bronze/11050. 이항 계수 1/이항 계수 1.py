import sys

n,k= map(int, sys.stdin.readline().split())
num = 1 
for _ in range(k):
    num*=n
    n-=1
for _ in range(k):
    num//=k
    k-=1
print(num)