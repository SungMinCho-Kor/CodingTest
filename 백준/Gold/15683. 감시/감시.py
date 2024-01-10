import sys
import copy

modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

class CCTV:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

N, M = map(int, sys.stdin.readline().rstrip().split())

office = []
CCTV_list = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        if line[j] != 0 and line[j] != 6:
            CCTV_list.append(CCTV(j, i, line[j]))
    office.append(line)

min_area = N * M

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def fill_office(office, mode, cctv):
    for i in mode:
        nx = cctv.x
        ny = cctv.y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                break
            if office[ny][nx] == 6:
                break
            elif office[ny][nx] == 0:
                office[ny][nx] = -1

def dfs(depth, office):
    global min_area
    if depth == len(CCTV_list):
        min_area = min(min_area, sum(map(lambda x: x.count(0), office)))
        return
    for mode in modes[CCTV_list[depth].type]:
        temp_office = copy.deepcopy(office)
        fill_office(temp_office, mode, CCTV_list[depth])
        dfs(depth + 1, temp_office)
        
dfs(0, office)
print(min_area)