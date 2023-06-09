'''
1. 상하반전
2. 좌우반전
3. 오른쪽으로 90도
4. 왼쪽으로 90도
5. 4등분하여 시계방향으로 회전
6. 4등분하여 반시계방향으로 회전


3. 오른쪽으로 90도 :
    n,m -> m, n
    board -> new
    0,0 -> 0,n-1
    0,1 -> 1,n-1
    0,2 -> 2, n-1
    0,m-1 -> m-1, n-1
    
    n-1,0 -> 0,0
    n-1,1 -> 1,0
4. 왼왼쪽으로
    n,m -> m, n
    board -> new
    0,0 -> m-1,0
    1,0 -> m-1,1
'''

import sys

n,m,r = map(int,sys.stdin.readline().split())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

r_ls = list(map(int,sys.stdin.readline().split()))

def func1():
    for i in range(n//2):
        board[i],board[n-i-1] = board[n-i-1],board[i]
def func2():
    for i in range(n):
        board[i] = board[i][::-1]
def func3():
    global n
    global m
    global board
    new = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = board[i][j]
    board = new
    n,m = m,n
def func4():
    global n
    global m
    global board
    new = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = board[i][j]
    board = new
    n,m = m,n
    
def func5():
    global board
    tmp = [[0 for _ in range(m//2)] for _ in range(n//2)]
    for i in range(n//2):#1분면 저장
        for j in range(m//2):
            tmp[i][j] = board[i][j]
    for i in range(n//2):#4->1
        for j in range(m//2):
            board[i][j] = board[i+n//2][j]
    for i in range(n//2,n):#3->4
        for j in range(m//2):
            board[i][j] = board[i][j+m//2]
    for i in range(n//2,n):#2->3
        for j in range(m//2,m):
            board[i][j] = board[i-n//2][j]
    for i in range(n//2):#1->2
        for j in range(m//2,m):
            board[i][j] = tmp[i][j-m//2]
    
def func6():
    global board
    tmp = [[0 for _ in range(m//2)] for _ in range(n//2)]
    for i in range(n//2):#1분면 저장
        for j in range(m//2):
            tmp[i][j] = board[i][j]
            
    for i in range(n//2):#2->1
        for j in range(m//2):
            board[i][j] = board[i][j+m//2]
    for i in range(n//2):#3->2
        for j in range(m//2,m):
            board[i][j] = board[i+n//2][j]
    for i in range(n//2,n):#4->3
        for j in range(m//2,m):
            board[i][j] = board[i][j-m//2]
    for i in range(n//2,n):#1->4
        for j in range(m//2):
            board[i][j] = tmp[i-n//2][j]
            
            
for op in r_ls:
    if op==1:
        func1()
    elif op==2:
        func2()
    elif op==3:
        func3()
    elif op==4:
        func4()
    elif op==5:
        func5()
    elif op==6:
        func6()

for i in board:
    for j in i:
        print(j,end=" ")
    print()
        
        
        
        
        
        