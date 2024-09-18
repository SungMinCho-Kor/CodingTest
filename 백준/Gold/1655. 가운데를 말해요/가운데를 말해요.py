import sys
import heapq
input = sys.stdin.readline

n = int(input())

left = []#작은 애들 저장(좌)
right = []#큰 애들 저장(우)

for t in range(n):
    k = int(input())
    
    if not left or -left[0] > k:
        heapq.heappush(left, -k)
    else:
        heapq.heappush(right, k)
    
    if len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))
    elif len(right) < len(left) - 1:
        heapq.heappush(right, -heapq.heappop(left))
        
    print(-left[0])