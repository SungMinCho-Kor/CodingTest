from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0)])
    distance = [[100*100 + 1 for _ in range(m)] for _ in range(n)]
    distance[0][0] = 1
    di, dj = (0,0,1,-1), (1,-1,0,0)
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and distance[i][j] + 1 < distance[ni][nj]:
                queue.append((ni, nj))
                distance[ni][nj] = distance[i][j] + 1
    if distance[-1][-1] == 10001:
        return -1
    return distance[-1][-1]
            