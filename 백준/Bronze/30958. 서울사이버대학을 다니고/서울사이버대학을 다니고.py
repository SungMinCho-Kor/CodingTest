import sys

input = sys.stdin.readline

n = int(input())
string = input().rstrip()
dic = dict()
answer = 0
for c in string:
    if 'a' <= c <= 'z':
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
        if dic[c] > answer:
            answer = dic[c]
print(answer)