import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    
    note1.sort()
    for num in note2:
        start = 0
        end = n-1
        while start<end:
            mid = (start + end)//2
            if note1[mid] < num:
                start = mid + 1
            else:
                end = mid
        if num == note1[start]:
            print(1)
        else:
            print(0)