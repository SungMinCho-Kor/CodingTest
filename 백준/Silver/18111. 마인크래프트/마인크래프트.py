import sys

N, M, B = map(int, sys.stdin.readline().rstrip().split())

block_count = [0 for _ in range(257)]
max_height = 0
min_height = 257

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        block_count[row[j]] += 1

for i in range(257):
    if block_count[i] > 0 and min_height == 257:
        min_height = i
    if block_count[256-i] > 0 and max_height == 0:
        max_height = 256 - i

time = 0
while min_height != max_height:
    min_count = block_count[min_height]
    max_count = block_count[max_height]
    
    min_expense = min_count
    max_expense = max_count * 2
    
    if B < min_expense or max_expense < min_expense:
        time += max_expense
        block_count[max_height - 1] += block_count[max_height]
        B += block_count[max_height]
        max_height -= 1
    else:
        time += min_expense
        block_count[min_height + 1] += block_count[min_height]
        B -= block_count[min_height]
        min_height += 1
print(time, max_height)