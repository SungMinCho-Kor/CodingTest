import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.append(points[0])
answer = 0
for i in range(n):
    answer += points[i][0] * points[i+1][1] - points[i+1][0]*points[i][1]
print(round(abs(answer)/2.0, 1))