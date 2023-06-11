import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    op = sys.stdin.readline().rstrip()
    if op=="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif op=="size":
        print(len(stack))
    elif op=="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif op=="pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        op,num = op.split()
        num = int(num)
        stack.append(num)
        