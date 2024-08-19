import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

brokes = list(map(int, input().split()))
controller = [False if i in brokes else True for i in range(10)]

answer = abs(n - 100)

for number in range(1000001):
    numstr = str(number)
    
    flag = True
    for k in numstr:
        if controller[int(k)] == False:
            flag = False
            break
    if flag:
        answer = min(answer, len(numstr) + abs(n - number))
print(answer)