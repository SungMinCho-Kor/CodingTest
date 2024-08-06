import sys
input = sys.stdin.readline

numbers = [False for _ in range(1000001)]

T = int(input())

max_number = 0
for i in range(2, 1000001):
    if numbers[i] == False:
        for j in range(i*2, 1000001, i):
            numbers[j] = True

for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N//2 + 1):
        if numbers[i] == False and numbers[N - i] == False:
            cnt += 1
    print(cnt)