import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
score = dict()

for num in nums:
    score[num] = 0
sorted_nums = sorted(nums)
max_num = sorted_nums[-1]

for num in sorted_nums:
    for k in range(num*2, max_num+1, num):
        if k in score:
            score[k] -= 1
            score[num] += 1

for num in nums:
    print(score[num], end=' ')