'''

n*m 배열 회전 시키기
min(n,m) % 2 == 0

1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

반시계로 돌리는 거임


'''

import sys

n,m,r = map(int,sys.stdin.readline().split())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# r%= (n-1)*2 + (m-1)*2

dx = [1,0,-1,0]
dy = [0,1,0,-1]
for _ in range(r):
    depth = min(n,m)//2
    for t in range(depth):
        i = t
        j = t
        tmp = board[i][j]
        d = 0
        while i+dx[d] != t or j+dy[d] != t:
            if t<=i+dx[d]<n-t and t<=j+dy[d]<m-t:
                board[i+dx[d]][j+dy[d]],tmp = tmp, board[i+dx[d]][j+dy[d]]
                i+=dx[d]
                j+=dy[d]
            else:
                d = (d+1)%4
        board[t][t] = tmp
# print()
for i in board:
    for j in i:
        print(j,end=" ")
    print()
        






