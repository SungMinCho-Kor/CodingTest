'''
DFS 가능, BFS 가능
DFS

'''

da = [-1, 1, 0, 0]
db = [0, 0, 1, -1]

from collections import deque

def solution(land):

    h = len(land)
    w = len(land[0])
    visit = [[False] * w for _ in range(h)]
    result = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and land[i][j]:
                queue = deque([(i, j)])
                tmp = set([j])
                cnt = 1
                visit[i][j] = True
                while queue:
                    a, b = queue.popleft()
                    for k in range(4):
                        na = a + da[k]
                        nb = b + db[k]
                        if 0 <= na < h and 0 <= nb < w and not visit[na][nb] and land[na][nb]:
                            visit[na][nb] = True
                            queue.append((na, nb))
                            tmp.add(nb)
                            cnt += 1
                for k in tmp:
                    result[k] += cnt

    return max(result)