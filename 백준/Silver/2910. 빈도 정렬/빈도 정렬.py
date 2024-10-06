import sys
input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))
cnt = {}
for i in range(n):
    if nums[i] in cnt:
        cnt[nums[i]] = (cnt[nums[i]][0] + 1, cnt[nums[i]][1])
    else:
        cnt[nums[i]] = (1, -i)

result = []
for num in cnt:
    val, order = cnt[num]
    result.append((val,order,num))
result.sort(reverse=True)
for val, _, num in result:
    print(f"{num} " * val, end = "")