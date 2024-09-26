import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if 0<=i-1<n and 0<=j-1<m:
            maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])
        elif 0<=i-1<n:
            maze[i][j] += maze[i-1][j]
        elif 0<=j-1<m:
            maze[i][j] += maze[i][j-1]
print(maze[-1][-1])