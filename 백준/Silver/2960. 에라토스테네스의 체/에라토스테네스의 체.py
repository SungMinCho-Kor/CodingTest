import sys
input = sys.stdin.readline

n, k = map(int, input().split())

numbers = [True for _ in range(n + 1)]
numbers[0] = False
numbers[1] = False

cnt = 0
for j in range(2, n+1):
    for i in range(j, n+1, j):
        if numbers[i] == True:
            numbers[i] = False
            cnt += 1
        if cnt == k:
            print(i)
            break
    if cnt == k:
        break