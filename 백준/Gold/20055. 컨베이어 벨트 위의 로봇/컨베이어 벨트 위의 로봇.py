import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

A = deque(list(map(int, input().split())))
upper = deque([False for _ in range(n)])

answer = 0
while True:
    answer += 1
    A.rotate(1)
    upper.rotate(1)
    
    upper[-1] = False

    for i in range(n-1, 0, -1):
        if upper[i] == False and upper[i-1] == True and A[i] > 0:
            A[i] -= 1
            upper[i] = True
            upper[i-1] = False
    upper[-1] = False
    
    if A[0] > 0:
        A[0] -= 1
        upper[0] = True
    if A.count(0) >= k:
        break
print(answer)