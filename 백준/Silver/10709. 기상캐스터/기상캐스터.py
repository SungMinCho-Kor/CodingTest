import sys

input = sys.stdin.readline
h, w = map(int, input().split())

sky = [list(input().rstrip()) for _ in range(h)]

for i in range(h):
    region = [-1] * w
    for j in range(w):
        if sky[i][j] == 'c':
            region[j] = 0
        elif j > 0 and region[j-1] >= 0:
            region[j] = region[j-1] + 1
    print(*region)