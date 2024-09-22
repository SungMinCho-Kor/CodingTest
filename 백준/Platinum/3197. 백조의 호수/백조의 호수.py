import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

lake = []
bird = []
ice_visit = [[False for _ in range(c)] for _ in range(r)]
ice_queue = deque()
water_queue = deque()
visit = [[False for _ in range(c)] for _ in range(r)]

for i in range(r):
    row = list(input().rstrip())
    for j in range(c):
        if row[j] == 'L':
            bird.append((i, j))
            row[j] = '.'
        if row[j] == '.':
            ice_queue.append((i, j))
            ice_visit[i][j] = True
    lake.append(row)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

time = 0
queue = deque([bird[0]])
next_queue = deque()
while True:
    # 녹여야할 놈 queue
    while ice_queue:
        i, j = ice_queue.popleft()
        lake[i][j] = '.'
        for k in range(4):
            ni = di[k] + i
            nj = dj[k] + j
            if 0<=ni<r and 0<=nj<c and ice_visit[ni][nj] == False:
                if lake[ni][nj] == 'X':
                    water_queue.append((ni, nj))
                else:
                    ice_queue.append((ni, nj))
                ice_visit[ni][nj] = True
    ice_queue = water_queue
    water_queue = deque()
    # 백조가 만날 수 있는지 확인
    while queue:
        i, j = queue.popleft()
        if (i, j) == bird[1]:
            print(time)
            exit(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<r and 0<=nj<c and visit[ni][nj] == False:
                if lake[ni][nj] == 'X':
                    next_queue.append((ni, nj))
                else:
                    queue.append((ni, nj))
                visit[ni][nj] = True
    queue = next_queue
    next_queue = deque()
    time +=1
print(time)