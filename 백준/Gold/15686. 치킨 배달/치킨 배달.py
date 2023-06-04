import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i,j])
        elif city[i][j] == 1:
            house.append([i,j])
chicken_m = list(combinations(chicken, m))
print(min(sum(min(abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in i) for h in house) for i in chicken_m))