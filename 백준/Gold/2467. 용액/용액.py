import sys
input = sys.stdin.readline
n = int(input())
liquid = list(map(int, input().split()))

start = 0
end = n-1
result = 1e10
answer1 = 0
answer2 = n-1
while start != end:
    tmp = liquid[start] + liquid[end]
    if abs(result) > abs(tmp):
        result = tmp
        answer1 = start
        answer2 = end
    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1
    else:
        break
    
print(liquid[answer1], liquid[answer2])