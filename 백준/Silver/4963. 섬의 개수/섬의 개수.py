import sys
sys.setrecursionlimit(2500)

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

w, h = map(int, sys.stdin.readline().rstrip().split())

def dfs(islands, i, j):
    for k in range(8):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < h and 0 <= nj < w:
            if visit[ni][nj] == False and islands[ni][nj] == 1:
                visit[ni][nj] = True
                dfs(islands, ni, nj)

while not (w == 0 and h == 0):
    islands = []
    for _ in range(h):
        islands.append(list(map(int, sys.stdin.readline().rstrip().split())))
    visit = [[False for _ in range(w)] for _ in range(h)]
    
    island_count = 0
    for i in range(h):
        for j in range(w):
            if islands[i][j] == 1 and visit[i][j] == False:
                island_count += 1
                visit[i][j] = True
                dfs(islands, i, j)
    
    print(island_count)
    
    w, h = map(int, sys.stdin.readline().rstrip().split())
    