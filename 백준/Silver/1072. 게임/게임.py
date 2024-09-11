import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

x, y = map(int, input().split())

def binary_find(start, end):
    
    mid = (start + end)//2
    if start == end:
        print(start)
        return
    if (y+mid)*100 // (x+mid) > (y * 100) // x:
        binary_find(start, mid)
    else:
        binary_find(mid+1, end)

if (y/x)*100 >= 99:
    print(-1)
else:
    binary_find(0, 1000000000)
    
