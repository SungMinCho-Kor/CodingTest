import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    ac = sys.stdin.readline().rstrip()
    ac = ac.replace("RR","")
    n = int(sys.stdin.readline())
    nums = sys.stdin.readline().rstrip().strip("[]")
    if nums:
        q = deque(map(int,nums.split(",")))
    else:
        q = deque()
    direction = True
    error = 0
    for op in ac:
        if op == 'R':
            direction = not direction
        else:
            if q:
                if direction==True:
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                error = 1
                break
    if error != 1:
        print("[",end="")
        while q and direction==True:
            print(f"{q.popleft()}",end="")
            if q:
                print(",",end="")
        while q and direction==False:
            print(f"{q.pop()}",end="")
            if q:
                print(",",end="")
        print("]")
'''
1
RDD
4
[1,2,3,4]
'''