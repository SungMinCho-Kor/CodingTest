import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().rstrip())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

areas = []
area_count = 0
area_temp = 0

def dfs(x, y, maps, visit):
    global area_temp
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == '1' and not visit[nx][ny]:
            visit[nx][ny] = True
            area_temp += 1
            dfs(nx, ny, maps, visit)

for i in range(N):
    for j in range(N):
        if not visit[i][j] and maps[i][j] == '1':
            visit[i][j] = True
            area_count += 1
            dfs(i, j, maps, visit)
            areas.append(area_temp + 1)
            area_temp = 0
print(area_count)
areas.sort()
for area in areas:
    print(area)