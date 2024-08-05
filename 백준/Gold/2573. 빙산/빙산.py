import sys
from collections import deque

# 입력
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
ices = []
ice_location = deque()
for i in range(n):
    ices.append(list(map(int, input().rstrip().split())))
    for j in range(m):
        if ices[i][j] > 0:
            ice_location.append((i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

# 주변 물 개수 구하기 함수
def get_water_count(i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<n and 0<=ny<m and ices[nx][ny] == 0:
            cnt +=1
    return cnt

# 얼음의 위치를 담고있는 큐 1년 경과
def melted_queue(queue):
    global ices
    new_queue = deque()
    new_ice = [[0 for _ in range(m)] for _ in range(n)]
    while queue:
        i, j = queue.popleft()
        water_count = get_water_count(i, j)
        if ices[i][j] - water_count > 0:
            new_ice[i][j] = ices[i][j] - water_count
            new_queue.append((i, j))
    ices = new_ice
    return new_queue

answer = 0
while True:
    visit = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i, j in ice_location:
        if not visit[i][j]:
            cnt += 1
            visit[i][j] = True
            tmp_queue = deque()
            tmp_queue.append((i, j))
            while tmp_queue:
                x, y = tmp_queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and ices[nx][ny] > 0:
                        visit[nx][ny] = True
                        tmp_queue.append((nx, ny))
    # print("cnt:", cnt)
    if cnt == 0:
        answer = 0
        break
    elif cnt >= 2:
        break
    answer += 1
    # print("---before-year", answer, "---")
    # for line in ices:
    #     print(*line)
    ice_location = melted_queue(ice_location)
    # print("---after---")
    # for line in ices:
    #     print(*line)
print(answer)