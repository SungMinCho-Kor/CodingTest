import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

people = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    people[b].append(a)

line = []

def func(m):
    visit[m] = True
    for person in people[m]:
        if visit[person] == False:
            func(person)
    line.append(m)

for i in range(1, n+1):
    if visit[i] == False:
        func(i)
print(*line)