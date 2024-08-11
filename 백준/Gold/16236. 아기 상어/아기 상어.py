import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
space = []
for i in range(N):
    row = list(map(int, input().split()))
    space.append(row)
    for j in range(N):
        if row[j] == 9:
            shark = (i, j)
            space[i][j] = 0

answer = 0
size = 2
shark_exp = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

while True:
    queue = deque()
    queue.append(shark)
    visit = [[False for _ in range(N)] for _ in range(N)]
    tsi, tsj = shark
    visit[tsi][tsj] = True
    fi, fj = N, N
    distance = 0
    while queue:
        distance += 1
        fish_box = []
        l = len(queue)
        for _ in range(l):
            si, sj = queue.popleft()
            for k in range(4):
                ni = si + dx[k]
                nj = sj + dy[k]
                if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and space[ni][nj] <= size: # 이동 가능한 곳
                    if 0 < space[ni][nj] < size: # 잡아먹을 수 있는 물고기가 있는 곳
                        fish_box.append((ni, nj))
                        visit[ni][nj] = True
                    else:
                        queue.append((ni, nj))
                        visit[ni][nj] = True
        
        if fish_box:
            for fish in fish_box:
                nfi, nfj = fish
                if fi > nfi or fi == nfi and fj > nfj:
                    fi, fj = nfi, nfj
            break
    if fi == N and fj == N:
        break
    else:
        shark_exp += 1
        if shark_exp == size:
            shark_exp = 0
            size += 1
        
        si, sj = shark
        answer += distance
        shark = (fi, fj)
        space[fi][fj] = 0
        
print(answer)