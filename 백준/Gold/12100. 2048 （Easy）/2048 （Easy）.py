import sys
import copy
from itertools import product
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def slide(board, d):
    prev = None
    now = None
    if d == 0:
        for i in range(n):
            # 합치기
            tmp = []
            prev = None
            for j in range(n):
                if board[j][i] != 0:
                    if prev == None:
                        prev = board[j][i]
                    elif prev == board[j][i]:
                        tmp.append(prev*2)
                        prev = None
                    else:
                        tmp.append(prev)
                        prev = board[j][i]
            if prev != None:
                tmp.append(prev)
                
            # 채우기
            for j in range(len(tmp)):
                board[j][i] = tmp[j]
            for j in range(len(tmp), n):
                board[j][i] = 0
    elif d == 1:
        for i in range(n):
            # 합치기
            tmp = []
            prev = None
            for j in range(n-1, 0-1, -1):
                if board[j][i] != 0:
                    if prev == None:
                        prev = board[j][i]
                    elif prev == board[j][i]:
                        tmp.append(prev*2)
                        prev = None
                    else:
                        tmp.append(prev)
                        prev = board[j][i]
            if prev != None:
                tmp.append(prev)
                
            # 채우기
            k = 0
            while k < n - len(tmp):
                board[k][i] = 0
                k += 1
            while k < n:
                board[k][i] = tmp.pop()
                k+=1
    elif d == 2:
        for i in range(n):
            # 합치기
            tmp = []
            prev = None
            for j in range(n):
                if board[i][j] != 0:
                    if prev == None:
                        prev = board[i][j]
                    elif prev == board[i][j]:
                        tmp.append(prev*2)
                        prev = None
                    else:
                        tmp.append(prev)
                        prev = board[i][j]
            if prev != None:
                tmp.append(prev)
                
            # 채우기
            for j in range(len(tmp)):
                board[i][j] = tmp[j]
            for j in range(len(tmp), n):
                board[i][j] = 0
    elif d == 3:
        for i in range(n):
            # 합치기
            tmp = []
            prev = None
            for j in range(n-1, 0-1, -1):
                if board[i][j] != 0:
                    if prev == None:
                        prev = board[i][j]
                    elif prev == board[i][j]:
                        tmp.append(prev*2)
                        prev = None
                    else:
                        tmp.append(prev)
                        prev = board[i][j]
            if prev != None:
                tmp.append(prev)
                
            # 채우기
            k = 0
            while k < n - len(tmp):
                board[i][k] = 0
                k += 1
            while k < n:
                board[i][k] = tmp.pop()
                k+=1

answer = 0
for directions in product([0, 1, 2, 3], repeat = 5):
    tmp_board = copy.deepcopy(board)
    for d in directions:
        slide(tmp_board, d)
    answer = max(answer, max(list(map(max, tmp_board))))
print(answer)