import sys
input = sys.stdin.readline

n, b = map(int ,input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]


def mul(arr1, arr2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j]%=1000
    return result

def power(arr, b):
    if b == 1:
        return arr
    elif b % 2 == 0:
        powed = power(arr, b//2)
        return mul(powed, powed)
    else:
        powed = power(arr, b//2)
        return mul(mul(powed, powed), arr)

answer = power(arr, b)
for i in range(n):
    for j in range(n):
        print(answer[i][j] % 1000, end = " ")
    print()