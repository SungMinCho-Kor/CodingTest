import sys

t = int(sys.stdin.readline())

for _ in range(t):
    string = list(sys.stdin.readline().rstrip())
    stack = []
    flag = 0
    for i in string:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                tmp = stack.pop()
                if tmp== ')':
                    flag = 1
                    break
            else:
                flag=1
                break
    if stack or flag == 1:
        print('NO')
    elif flag == 0:
        print('YES')