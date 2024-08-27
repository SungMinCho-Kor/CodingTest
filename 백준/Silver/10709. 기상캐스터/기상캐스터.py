import sys

input = sys.stdin.readline
h, w = map(int, input().split())

sky = [list(input().rstrip()) for _ in range(h)]
region = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c':
            region[i][j] = 0
        elif j > 0 and region[i][j-1] >= 0:
            region[i][j] = region[i][j-1] + 1
    
for line in region:
    print(*line)