import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
paper = []
cheese = deque()
for i in range(N):
    row = list(map(int, input().split()))
    paper.append(row)
    for j in range(M):
        if 1 == row[j]:
            cheese.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
while cheese:
    # 외부 확인
    queue = deque([(0, 0)])
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and paper[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = True
    
    melt = [[0 for _ in range(M)] for _ in range(N)]
    new_paper = copy.deepcopy(paper)
    l = len(cheese)
    for _ in range(l):
        ci, cj = cheese.popleft()
        outside_count = 0
        for k in range(4):
            nx = ci + dx[k]
            ny = cj + dy[k]
            if 0<=nx<N and 0<=ny<M and paper[nx][ny] == 0 and visit[nx][ny]:
                outside_count += 1
        if outside_count >= 2:
            new_paper[ci][cj] = 0
        else:
            cheese.append((ci, cj))
    paper = new_paper
    answer += 1
print(answer)