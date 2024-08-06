import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]

answer = 0
# 가로 세기
for i in range(N):
    flag = False
    for j in range(M):
        if graph[i][j] == '-' and flag == False:
            flag = True
            answer += 1
        elif graph[i][j] == '|' and flag == True:
            flag = False
# 세로 세기
for i in range(M):
    flag = False
    for j in range(N):
        if graph[j][i] == '|' and flag == False:
            flag = True
            answer += 1
        elif graph[j][i] == '-' and flag == True:
            flag = False
print(answer)