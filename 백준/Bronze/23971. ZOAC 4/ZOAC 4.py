import sys

def function(H, W, N, M):
    
    width = W//(M+1) + (1 if W%(M+1) > 0 else 0)
    height = H//(N+1) + (1 if H%(N+1) > 0 else 0)
    
    return width * height
    
H, W, N, M = map(int, sys.stdin.readline().rstrip().split())

print(function(H, W, N, M))