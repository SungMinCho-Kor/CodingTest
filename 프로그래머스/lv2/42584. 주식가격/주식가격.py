# from collections import deque

def solution(prices):
    # answer = deque()
    # queue = deque(prices)
    # while queue:
    #     now = queue.popleft()
    #     i = 0
    #     while len(queue)>i and queue[i]>=now:
    #         i+=1
    #     if len(queue)==i:
    #         answer.append(i)
    #     else:
    #         answer.append(i+1)
    answer =[]
    for i in range(len(prices)):
        j = i
        while j <len(prices):
            if prices[i]<=prices[j]:
                j+=1
            else:
                j+=1
                break
                
        answer.append(j-i - 1)
    return answer