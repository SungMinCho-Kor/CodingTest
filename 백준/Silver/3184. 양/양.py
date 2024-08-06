import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sheep_count = 0
wolf_count = 0
tmp_sheep_count = 0
tmp_wolf_count = 0
def dfs(i,j,visit):
    global tmp_sheep_count
    global tmp_wolf_count
    if graph[i][j] == 'o':
        tmp_sheep_count += 1
    elif graph[i][j] == 'v':
        tmp_wolf_count += 1
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<= nx < R and 0 <= ny < C and not visit[nx][ny] and (graph[nx][ny] == 'v' or graph[nx][ny] == 'o' or graph[nx][ny] == '.'):
            visit[nx][ny] = True
            dfs(nx,ny,visit)
    
visit = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visit[i][j] and (graph[i][j] == 'v' or graph[i][j] == 'o'):
            visit[i][j] = True
            tmp_sheep_count = 0
            tmp_wolf_count = 0
            dfs(i,j,visit)
            if tmp_sheep_count > tmp_wolf_count:
                sheep_count += tmp_sheep_count
            else:
                wolf_count += tmp_wolf_count
print(sheep_count, wolf_count)