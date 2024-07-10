import sys

H, W, N, M = map(int, sys.stdin.readline().rstrip().split())

width = W//(M+1) + (1 if W%(M+1) > 0 else 0)
height = H//(N+1) + (1 if H%(N+1) > 0 else 0)
answer = width * height

print(answer)