'''
1. 사과를 먹으면 꼬리가 늘어남
2. 꼬리나 벽을 만나면 게임 종료
3. (0, 0)에서 시작
4. 길이 1에서 시작
5. 처음 방향 ->

방향
0 : 우
1 : 하
2 : 좌
3 : 상

'''

import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

apples = []
for _ in range(K):
    apple = list(map(int,sys.stdin.readline().rstrip().split()))
    apple = [apple[1] - 1, apple[0] - 1]
    apples.append(apple)

d = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

sec = 0

L = int(sys.stdin.readline().rstrip())

snake = [[0, 0]]

for _ in range(L):
    X, C = sys.stdin.readline().rstrip().split()
    
    for _ in range(int(X) - sec):
        nx, ny = snake[-1][0] + dx[d], snake[-1][1] + dy[d]
        sec += 1
        # print("head = ", nx, ny,"sec = ", sec)
        if [nx, ny] in snake or nx < 0 or nx >= N or ny < 0 or ny >= N:
            print(sec)
            exit()
        snake.append([nx, ny])
        if [nx, ny] in apples:
            apple = apples.pop(apples.index([nx, ny]))
            # print("apple", apple)
        else :
            tail = snake.pop(0)
            # print("꼬리 삭제", tail)
        
    if C == 'D':
        d = (d + 1) % 4
    elif C == 'L':
        d = (d - 1) % 4
    
for _ in range(N):
    nx, ny = snake[-1][0] + dx[d], snake[-1][1] + dy[d]
    sec += 1
    if [nx, ny] in snake or nx < 0 or nx >= N or ny < 0 or ny >= N:
        print(sec)
        exit()
    snake.append([nx, ny])
    # print("head = ", nx, ny)
    if [nx, ny] in apples:
        apple = apples.pop(apples.index([nx, ny]))
        # print("apple", apple)
    else :
        tail = snake.pop(0)
        # print("꼬리 삭제", tail)
    
print(sec)
    