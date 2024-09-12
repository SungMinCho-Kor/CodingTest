import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def func(n):
    queue = deque([i for i in range(1, n+1)])
    stack = []
    answer = []
    for _ in range(n):
        num = int(input())
        if queue and queue[0] <= num:
            while queue:
                k = queue.popleft()
                answer.append('+')
                stack.append(k)
                if k == num:
                    break
                elif k > num:
                    print('NO')
                    return
        if stack:
            while stack:
                k = stack.pop()
                answer.append('-')
                if k == num:
                    break
                elif k < num:
                    print('NO')
                    return
        else:
            print('NO')
            return
    for ans in answer:
        print(ans)
func(n)