import sys
input = sys.stdin.readline

n, m = map(int, input().split())

picture = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei + 1):
        for j in range(sj, ej + 1):
            picture[i][j] += 1

answer = 0
for i in range(101):
    for j in range(101):
        if picture[i][j] > m:
            answer += 1
print(answer)