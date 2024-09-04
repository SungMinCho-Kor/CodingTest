import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

cards = list(map(int, input().split()))
rival = list(map(int, input().split()))
cards.sort()

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if b >= m:
        return
    a = find(a)
    b = find(b)
    parent[a] = b

parent = [i for i in range(m)]

for r in rival:
    start = 0
    end = m
    while start<end:
        mid = (start + end)//2
        if cards[mid] > r:
            end = mid 
        else:
            start = mid + 1
    end = find(end)
    print(cards[end])
    union(end, end+1)