import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())

jews = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jews, (m, v))# 무게를 기준으로 최소힙
bag = [int(input()) for _ in range(k)]
bag.sort()

answer = 0
candidate = []
for b in bag:
    while jews and b >= jews[0][0]:
        heapq.heappush(candidate, -heapq.heappop(jews)[1])
    if candidate:
        answer -= heapq.heappop(candidate)
    elif not jews:
        break
print(answer)