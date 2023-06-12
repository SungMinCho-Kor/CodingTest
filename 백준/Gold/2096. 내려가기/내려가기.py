'''
1 2 3 

1에서 시작한 최소
1에서 시작한 최대
2에서 시작한 최소
2에서 시작한 최대
3에서 시작한 최소
3에서 시작한 최대

1 2 3 
4 5 6
4 9 0

[1 2 3]
 4 5 6

너 가??

'''
import sys
n = int(sys.stdin.readline())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

mins = [board[0][0],board[0][1],board[0][2]]
maxs = [board[0][0],board[0][1],board[0][2]]

for i in range(1,n):
    tmp = [0,0,0]
    tmp[0] = min(mins[0],mins[1])
    tmp[1] = min(mins[0],mins[1],mins[2])
    tmp[2] = min(mins[1],mins[2])
    for j in range(3):
        mins[j] = tmp[j] + board[i][j]
    tmp[0] = max(maxs[0],maxs[1])
    tmp[1] = max(maxs[0],maxs[1],maxs[2])
    tmp[2] = max(maxs[1],maxs[2])
    for j in range(3):
        maxs[j] = tmp[j] + board[i][j]
print(max(maxs) , min(mins))
    


            
            
            