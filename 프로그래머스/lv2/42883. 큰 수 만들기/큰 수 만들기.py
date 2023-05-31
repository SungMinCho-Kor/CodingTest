'''
1924 , 3

'''
def solution(number, k):
    number = list(number)
    stack = []
    for i in number:
        while len(stack)>0 and stack[-1]<i and k>0:
            stack.pop()
            k-=1    
        stack.append(i)
    for i in range(k):
        stack.pop()
    return "".join(stack)