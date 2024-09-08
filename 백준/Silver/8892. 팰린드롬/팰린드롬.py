import sys
input = sys.stdin.readline

t = int(input())

def is_pd(num):
    for i in range(len(num) // 2):
        if num[i] != num[-1-i]:
            return False
    return True

def func(k, nums):
    for i in range(k-1):
        for j in range(i+1, k):
            password1 = nums[i] + nums[j]
            password2 = nums[j] + nums[i]
            if is_pd(password1):
                print(password1)
                return
            if is_pd(password2):
                print(password2)
                return
    print(0)
    
for _ in range(t):
    k = int(input())
    nums = [input().rstrip() for _ in range(k)]
    func(k, nums)