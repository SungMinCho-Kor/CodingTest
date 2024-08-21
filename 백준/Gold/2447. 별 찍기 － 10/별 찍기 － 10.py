import sys
input = sys.stdin.readline
n = int(input())

def star(k):
    if k == 1:
        return ["*"]
    s = star(k//3)
    lst = []
    for i in s:
        lst.append(i*3)
    for i in s:
        lst.append(i + ' '*(k//3) + i)
    for i in s:
        lst.append(i*3)
    return lst

print('\n'.join(star(n)))