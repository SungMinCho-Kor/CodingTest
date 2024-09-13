import sys

input = sys.stdin.readline

n = int(input())

nums = []

cnt_dict = dict()

avg = 0.0
min_num = 4000
max_num = -4000
max_cnt = 0
max_cnt_nums = []
for _ in range(n):
    num = int(input())
    
    #최빈값
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1
        
    if cnt_dict[num] > max_cnt:
        max_cnt = cnt_dict[num]
        max_cnt_nums = [num]
    elif cnt_dict[num] == max_cnt:
        max_cnt_nums.append(num)
    
    #범위
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num
    
    #중앙값
    nums.append(num)
    
    #산술평균
    avg += num

nums.sort()
avg = round(avg/n)
max_cnt_nums.sort()

print(int(avg))
print(nums[n//2])
if len(max_cnt_nums) > 1:
    print(max_cnt_nums[1])
else:
    print(max_cnt_nums[0])
print(max_num - min_num)