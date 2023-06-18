import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    print(str(1+(n-1)%h) + str((n-1)//h + 1).zfill(2))