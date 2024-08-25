import sys

input = sys.stdin.readline


def recur(line, k):
    if k == 1:
        return line
    return recur(''.join(line[:k//3]), k//3)+ ' '*(k//3) + recur(''.join(line[(k//3) * 2:]), k//3)

n_arr = sys.stdin.readlines()
for n in n_arr:
    n = int(n.rstrip())
    
    line = (3**n)*'-'
    k = 3**n
    print(recur(line, k))