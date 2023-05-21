from collections import deque

def solution(prices):
    answer =[]
    for i in range(len(prices)):
        j = i
        while j <len(prices):
            if prices[i]<=prices[j]:
                j+=1
            else:
                j+=1
                break
        answer.append(j-i-1)
    return answer


# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         while stack != [] and stack[-1][1] > prices[i]:
#             past, _ = stack.pop()
#             answer[past] = i - past
#             # print(answer)
#         stack.append([i, prices[i]])
#         print(stack)
#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer