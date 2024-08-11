import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

answer = 0
while len(t) >= len(s):
    if s == t:
        answer = 1
        break
    ch = t.pop()
    if ch == 'B':
        t.reverse()
print(answer)