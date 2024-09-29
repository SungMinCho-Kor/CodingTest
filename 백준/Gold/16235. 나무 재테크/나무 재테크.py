import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 겨울마다 추가되는 양분 : A배열
A = [list(map(int, input().split())) for _ in range(n)]

# 땅
land = [[5 for _ in range(n)] for _ in range(n)]

# 심은 나무 양분 정보 : tree (x, y, year)

tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, year = map(int, input().split())
    tree[i-1][j-1].append(year)

for i in range(n):
    for j in range(n):
        tree[i][j] = deque(sorted(tree[i][j]))

di = [1,1,1,-1,-1,-1,0,0]
dj = [1,0,-1,1,0,-1,-1,1]

# k년 
for _ in range(k):
    for i in range(n):
        for j in range(n):
            l = len(tree[i][j])
            p = 0
            while p < l and land[i][j] >= tree[i][j][p]:
                land[i][j] -= tree[i][j][p]
                tree[i][j][p] += 1
                p+=1
            while p < l:
                land[i][j] += tree[i][j].pop()//2
                p+=1
    # 가을
    for i in range(n):
        for j in range(n):
            for year in tree[i][j]:
                if year % 5 == 0:
                    for p in range(8):
                        ni = i + di[p]
                        nj = j + dj[p]
                        if 0<=ni<n and 0<=nj<n:
                            tree[ni][nj].appendleft(1)
    
    # 겨울
    for i in range(n):
        for j in range(n):
            land[i][j] += A[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)