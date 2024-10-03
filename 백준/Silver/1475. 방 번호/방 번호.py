import sys
input = sys.stdin.readline

num = list(map(int, list(input().rstrip())))
nums = {}
for i in range(10):
    nums[i] = 0

for i in num:
    nums[i] += 1
s = nums[6] + nums[9]
if s%2 == 0:
    nums[6] = nums[9] = s//2
else:
    nums[6] = nums[9] = s//2 + 1
    
max_cnt = 0
for i in range(10):
    if max_cnt<nums[i]:
        max_cnt = nums[i]
print(max_cnt)