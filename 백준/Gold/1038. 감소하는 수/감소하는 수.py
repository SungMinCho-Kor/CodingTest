
'''

0,1,2,3,4,5,6,7,8,9
10C1+10C2+...10C10
2**10 - 1
1023

0 1 2 3 4 5 6 7 8 9

0~9 부분집합 중에서 n번째를 찾는 것.
10C1 = 10
10C2 = 45  
10C3 = 120   
10C4 = 210   
10C5 = 252    10 9 8
'''

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
num = ['9','8','7','6','5','4','3','2','1','0']


if n<10:
    l = list(combinations(num,1))
elif n<55:
    n-=10
    l = list(combinations(num,2))
elif n<175:
    n-=55
    l = list(combinations(num,3))
elif n<385:
    n-=175
    l = list(combinations(num,4))
elif n<637:
    n-=385
    l = list(combinations(num,5))
elif n<847:
    n-=637
    l = list(combinations(num,6))
elif n<967:
    n-=847
    l = list(combinations(num,7))
elif n<1012:
    n-=967
    l = list(combinations(num,8))
elif n<1022:
    n-=1012
    l = list(combinations(num,9))
elif n<1023:
    n-=1022
    l = list(combinations(num,10))
else:
    print('-1')
    sys.exit()
l.sort()
print("".join(list(l[n])))
    