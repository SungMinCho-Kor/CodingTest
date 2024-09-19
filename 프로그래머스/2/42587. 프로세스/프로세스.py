import heapq
from collections import deque

def solution(priorities, location):
    queue = deque()
    priority_queue = []
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        heapq.heappush(priority_queue, -priorities[i])
    print(queue)
    print(priority_queue)
    answer = 0
    while queue:
        if queue[0][1] == -priority_queue[0]:
            answer += 1
            loc, priority = queue.popleft()
            heapq.heappop(priority_queue)
            if loc == location:
                return answer
        else:
            queue.rotate(-1)
    return answer