'''

왼쪽으로 갈지 오른쪽으로 갈지 결정해야 함
 -> 2가지 경우의 수
 
'''

import sys

input = sys.stdin.readline

w, h = map(int, input().split())

n = int(input())

stores = []

for _ in range(n):
    direction, location = map(int, input().split())
    stores.append((direction, location))
    
md, ml = map(int, input().split())

answer = 0

for d, l in stores:
    if md == 1:
        if d == 1:
            answer += abs(ml - l)
        elif d == 2:
            answer += min(ml + l + h, 2*w - ml - l + h)
        elif d == 3:
            answer += ml + l
        elif d == 4:
            answer += w - ml + l
    elif md == 2:
        if d == 1:
            answer += min(ml + l + h, 2*w - ml - l + h)
        elif d == 2:
            answer += abs(ml - l)
        elif d == 3:
            answer += ml + h - l
        elif d == 4:
            answer += w - ml + h - l
    elif md == 3:
        if d == 1:
            answer += l + ml
        elif d == 2:
            answer += l + h - ml
        elif d == 3:
            answer += abs(ml - l)
        elif d == 4:
            answer += min(w + 2*h - l - ml, w + ml + l)
    elif md == 4:#동
        if d == 1:
            answer += ml + w - l
        elif d == 2:#남
            answer += h - ml + w - l
        elif d == 3:# 서
            answer += min(w + 2*h - l - ml, w + ml + l)
        elif d == 4:
            answer += abs(ml - l)
print(answer)