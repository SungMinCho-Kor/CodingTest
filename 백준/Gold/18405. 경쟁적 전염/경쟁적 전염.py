from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

board = []
virus = {}
for i in range(1, k+1):
    virus[i] = deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] > 0:
            virus[row[j]].append((i,j))
    board.append(row)
s, x, y = map(int, input().split())

di, dj = (0,0,-1,1), (1,-1,0,0)
for _ in range(s):
    for num in range(1, k+1):
        for t in range(len(virus[num])):
            i, j = virus[num].popleft()
            for p in range(4):
                ni, nj = di[p] + i, dj[p] + j
                if 0<=ni<n and 0<=nj<n and board[ni][nj] == 0:
                    board[ni][nj] = num
                    virus[num].append((ni, nj))

print(board[x-1][y-1])