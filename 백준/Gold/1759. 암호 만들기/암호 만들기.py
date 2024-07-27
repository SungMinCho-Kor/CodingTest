
import sys
from itertools import combinations 
input = sys.stdin.readline

l,c = map(int,input().split())
arr = input().split()
arr.sort()
answer = list(combinations(arr,l))
answer = list(map("".join,answer))
for i in answer:
    l = len(set(i).intersection(('a', 'e', 'i', 'o', 'u')))#모음 개수
    if l>=1 and len(i)-l >=2:
        print(i)