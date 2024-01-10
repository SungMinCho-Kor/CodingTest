'''
톱니바퀴 A를 회전할 때, 
맞닿은 톱니의 극이 다르다면, 
B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
'''

import sys
from collections import deque

def rotate(direction, gear):
    if direction == 1:
        gear.rotate(1)
    elif direction == -1:
        gear.rotate(-1)
    return gear

def score(gears):
    scores = [1, 2, 4, 8]
    score = 0
    for i in range(4):
        if gears[i][0] == '1':
            score += scores[i]
    return score

gears = []

for _ in range(4):
    gears.append(deque(sys.stdin.readline().rstrip()))

K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    gear_number, direction = map(int, sys.stdin.readline().rstrip().split())
    gear_number -= 1
    
    rotate_list = [0, 0, 0, 0]
    rotate_list[gear_number] = direction
    
    for i in range(gear_number, 0, -1):
        if gears[i][6] == gears[i - 1][2]:
            break
        else:
            rotate_list[i - 1] = -rotate_list[i]
    for i in range(gear_number, 4 - 1):
        if gears[i][2] == gears[i + 1][6]:
            break
        else:
            rotate_list[i + 1] = -rotate_list[i]
        
    for i in range(4):
        gears[i] = rotate(rotate_list[i], gears[i])

print(score(gears))
        
        
        
        