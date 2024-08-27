import sys

input = sys.stdin.readline
h, w = map(int, input().split())

sky = [list(input().rstrip()) for _ in range(h)]
region = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    k = 0
    while k < w:
        if sky[i][k] == 'c':
            region[i][k] = 0
        elif k > 0 and region[i][k-1] >= 0:
            region[i][k] = region[i][k-1] + 1
        k += 1
for line in region:
    print(*line)