from collections import deque
def solution(maps):
    answer = 0
    visited = [[False for i in range(len(maps[0]))] for j in range(len(maps))]    
    return bfs(maps, 0, 0, visited)

def bfs(maps, x, y, visited):
    n = len(maps)
    m = len(maps[0])
    queue = deque([(x, y)])

    visited[x][y] = True
    distance = {(x, y) : 1}

    # print(queue)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] == 1:
                if (nx, ny) == (n-1, m-1):
                    return distance[(x, y)] + 1
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited[nx][ny] = True
    return -1