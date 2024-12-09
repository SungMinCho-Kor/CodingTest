class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = []
        for idx, val in enumerate(nums):
            nums_list.append([val, idx])
        print(nums_list)
        nums_list.sort()
        print(nums_list)
        start = 0
        end = len(nums_list) - 1
        while start != end:
            mid = (start + end)//2
            standard = nums_list[start][0] + nums_list[end][0] 
            if standard > target:
                end -= 1
            elif standard < target:
                start += 1
            else:
                return [nums_list[start][1], nums_list[end][1]]