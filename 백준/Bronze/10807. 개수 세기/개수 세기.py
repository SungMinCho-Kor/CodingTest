import sys

n = int(sys.stdin.readline())
ls = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
print(ls.count(m))