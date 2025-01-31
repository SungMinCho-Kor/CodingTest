from collections import deque

def solution(people, limit):
    people.sort(reverse = True)
    queue = deque(people)
    answer = 0
    while queue:
        l = queue.popleft()
        answer += 1
        if not queue:
            break
        
        if limit - l >= queue[-1]:
            r = queue.pop()
    return answer