import sys
input = sys.stdin.readline

N = int(input())

# count를 가로로 온 count, 세로로 온 count, 대각으로 온 count로 나눠서 관리
count = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
house = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    if house[0][i] == 1:
        break
    count[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if house[i][j] != 1:
            count[i][j][0] += count[i][j-1][0] + count[i][j-1][2]
            count[i][j][1] += count[i-1][j][1] + count[i-1][j][2]
            if house[i-1][j] != 1 and house[i][j-1] != 1:
                count[i][j][2] += count[i-1][j-1][0] + count[i-1][j-1][1] + count[i-1][j-1][2]
                
print(sum(count[N-1][N-1]))