import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
arr = []

for num in numbers:
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid
        else:
            start = mid + 1
    if start >= len(arr):
        arr.append(num)
    else:
        arr[start] = num
print(len(arr))
                