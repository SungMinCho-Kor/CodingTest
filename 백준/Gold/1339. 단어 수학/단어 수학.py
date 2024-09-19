import sys
import heapq
input = sys.stdin.readline

n = int(input())

dic = {}
for _ in range(n):
    string = input().rstrip()
    for i in range(len(string)):
        if string[i] in dic:
            dic[string[i]] += 10**(len(string) - i - 1)
        else:
            dic[string[i]] = 10**(len(string) - i - 1)
queue = []

for key in dic:
    heapq.heappush(queue, (-dic[key], key))

answer = 0
for i in range(9, -1, -1):
    if not queue:
        break
    answer += i * (-heapq.heappop(queue)[0])
print(answer)