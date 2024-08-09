import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    row = input()
    if row[0] == '1':
        order, num = map(int, row.split())
    else:
        order = int(row)
    if order == 1:
        stack.append(num)
    elif order == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == 3:
        print(len(stack))
    elif order == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)