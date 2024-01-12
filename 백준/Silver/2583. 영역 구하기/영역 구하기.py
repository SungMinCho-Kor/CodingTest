import sys
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, sys.stdin.readline().rstrip().split())

square_map = [[1 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            square_map[i][j] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = []
def dfs(i, j):
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<M and 0<=ny<N and square_map[nx][ny] == 1:
            square_map[nx][ny] = 0
            answer[-1] += 1
            dfs(nx, ny)
            

for i in range(M):
    for j in range(N):
        if square_map[i][j] == 1:
            answer.append(1)
            square_map[i][j] = 0
            dfs(i, j)
            
answer.sort()
print(len(answer))
print(*answer)
