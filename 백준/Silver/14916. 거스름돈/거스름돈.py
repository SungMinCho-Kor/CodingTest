import sys

input = sys.stdin.readline

n = int(input())

k = n//5
flag = False
for i in range(k, 0-1, -1):
    if (n-i*5)%2 == 0:
        print(i + (n-i*5)//2)
        flag = True
        break
if not flag:
    print(-1)