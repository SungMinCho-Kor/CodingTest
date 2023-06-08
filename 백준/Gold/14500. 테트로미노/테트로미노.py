'''
도형 1 : 가로 or 세로                        : 2
도형 2                                       : 1
도형 3 : ㄴ : 회전시 4 + 대칭후 회전시 4     : 8
도형 4 : 회전시 2 + 대칭후 회전시 2          : 4
도형 5 : 회전시 4 : 4                        : 4

1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

0,0 일때
1 2 3 4

'''

import sys

n,m = map(int,sys.stdin.readline().split())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
max_board = [[0]*m for _ in range(n)]

# print(board)

for i in range(n):
    for j in range(m):#19개
        sums = []
        if j+3<m:#ㅡ
            sums.append(sum(board[i][j:j+4]))
        if i+3<n:#ㅣ
            sums.append(sum([board[i+k][j] for k in range(4)]))
        if j+1<m and i+1<n:#ㅁ
            sums.append(sum(board[i][j:j+2] + board[i+1][j:j+2]))
        if j+1<m and i+2<n:
            #순서 원본ㄴ -> 회전 ㄱ-> 대칭 -> 대칭회전
            sums.append(sum(board[i+k][j] for k in range(3)) + board[i+2][j+1])
            sums.append(sum(board[i+k][j+1] for k in range(3)) + board[i][j])
            sums.append(sum(board[i+k][j] for k in range(3)) + board[i][j+1])
            sums.append(sum(board[i+k][j+1] for k in range(3)) + board[i+2][j])
            #ㄹ자
            sums.append(sum(board[i+k][j] for k in range(2)) + sum(board[i+1+k][j+1] for k in range(2)))
            sums.append(sum(board[i+k][j+1] for k in range(2)) + sum(board[i+1+k][j] for k in range(2)))
            # ㅓ자
            sums.append(sum(board[i+k][j+1] for k in range(3)) + board[i+1][j])
            sums.append(sum(board[i+k][j] for k in range(3)) + board[i+1][j+1])
            
        if j+2<m and i+1<n:
            #순서 원본ㄴ -> 회전 ㄱ-> 대칭 -> 대칭회전
            sums.append(board[i][j]+sum(board[i+1][j:j+3]))
            sums.append(board[i+1][j+2]+sum(board[i][j:j+3]))
            sums.append(board[i+1][j] + sum(board[i][j:j+3]))
            sums.append(board[i][j+2] + sum(board[i+1][j:j+3]))
            #ㄹ자
            sums.append(sum(board[i][j+1:j+3]) + sum(board[i+1][j:j+2]))
            sums.append(sum(board[i][j:j+2]) + sum(board[i+1][j+1:j+3]))
            # ㅗ자
            sums.append(board[i][j+1] + sum(board[i+1][j:j+3]))
            sums.append(board[i+1][j+1] + sum(board[i][j:j+3]))
        if sums:
            max_board[i][j] = max(sums)
print(max(map(max,max_board)))
        
        
