import sys
from collections import deque
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

q = deque()
m = 0
for i in str1:
    q.append(i)
    while "".join(q) not in str2:
        q.popleft()
    m = max(m,len(q))
print(m)