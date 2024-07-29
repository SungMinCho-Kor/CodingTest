'''
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.

1. 바이러스를 놓을 수 있는 칸을 DFS로 완전 탐색
    - 놓을 수 있는 칸 개수 > M
        -> M 개를 다 놓으면 탈출
    - 놓을 수 있는 칸 개수 < M
        -> 놓을 수 있는 칸에 다 놓으면 탈출

2. 바이러스 퍼트리기

3. 맵이 모두 바이러스로 찬 것을 확인하는 함수

'''

import sys
import copy
from collections import deque
from itertools import combinations
# sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().rstrip().split())

maps = []
virus_candidates = []
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if maps[i][j] == 2:
            virus_candidates.append((i, j))

dx =  [0,0,-1,1]
dy =  [-1,1,0,0]

answer_candidate = []

candidates = list(combinations(virus_candidates,M))

def check(maps):
    flag = True
    for i in range(N):
        if 0 in maps[i] or 2 in maps[i]:
            flag = False
    return flag
    
def difuse(copy_map):
    queue = deque()
    for i in range(N):
        for j in range(N):
            if copy_map[i][j] == 3:
                queue.append((i,j))
    time = 0
    while queue:
        tmp = len(queue)
        for i in range(tmp):
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N and (copy_map[nx][ny] == 0 or copy_map[nx][ny] == 2):
                    copy_map[nx][ny] = 3
                    queue.append((nx,ny))
        if queue:
            time += 1
    if check(copy_map):
        answer_candidate.append(time)
    
for candidate in candidates:
    for point in candidate:
        i, j = point
        maps[i][j] = 3
    copy_map = copy.deepcopy(maps)
    difuse(copy_map)
    for point in candidate:
        i, j = point
        maps[i][j] = 2

if answer_candidate:
    print(min(answer_candidate))
else:
    print(-1)

