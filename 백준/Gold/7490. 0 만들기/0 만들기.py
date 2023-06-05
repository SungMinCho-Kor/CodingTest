
'''
1,2,3,4,5
1,(),2,(),3,()...


'''
import sys
input = sys.stdin.readline
from itertools import product
from collections import deque

tool = ['+','-',' ']

t = int(input())

for _ in range(t):
    al = []
    n = int(input())
    tmp = [str(k) for k in range(1,n+1)]
    op = list(product(tool,repeat = n-1))
    nums = []
    for o in op:
        num = [tmp[0]]
        for i in range(n-1):
            if o[i]==' ':
                num[-1] = num[-1]+tmp[i+1]
            else:
                num.append(tmp[i+1])
        nums.append(num)
        
    
    for i in range(len(op)):
        answer = int(nums[i].pop(0))
        for o in op[i]:
            if o=='+':
                answer+=int(nums[i].pop(0))
            elif o=='-':
                answer-=int(nums[i].pop(0))
        if answer == 0:
            string = ""
            for j in range(n-1):
                string += tmp[j]+op[i][j]
            string+=tmp[-1]
            al.append(string)
    al.sort()
    for i in al:
        print(i)
    print()
    # for o in op:
    #     string = ""
    #     for i in range(n-1):
    #         string += tmp[i]+o[i]
    #     string+=tmp[-1]
    #     ls.append(string)
    # print(ls)
    # for eq in ls:
    #     answer =0
    #     operation = 0#0==+
    #     for i in list(eq):
    
    
    
    
    
    
    
    