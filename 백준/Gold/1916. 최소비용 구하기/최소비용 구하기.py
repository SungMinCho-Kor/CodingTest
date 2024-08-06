import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

# 그래프 그리기
graph = [[] for _ in range(n + 1)]
costs = [float('inf') for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
start, end = map(int, input().split())

# 다익스트라
costs[start] = 0
queue = []
heapq.heappush(queue, (costs[start], start))
while queue:
    cost, start_point = heapq.heappop(queue)
    
    if cost > costs[start_point]:
        continue
    
    for end_point, end_cost in graph[start_point]:
        if cost + end_cost < costs[end_point]:
            costs[end_point] = cost + end_cost
            heapq.heappush(queue, (costs[end_point], end_point))
print(costs[end])