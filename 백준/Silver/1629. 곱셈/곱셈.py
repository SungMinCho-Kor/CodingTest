import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

def das(A, B, C):
    if B == 1:
        return A % C
    if B % 2 != 0:
        return ((das(A, B // 2, C) ** 2) * A) % C
    else:
        return (das(A, B // 2, C) ** 2) % C


print(das(A, B, C))