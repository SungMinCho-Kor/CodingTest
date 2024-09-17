import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for ai in a:
    if ai-b > 0:
        answer += 1 + (ai-b)//c
        if (ai-b)/c != (ai-b)//c:
            answer += 1
    else:
        answer += 1
print(answer)