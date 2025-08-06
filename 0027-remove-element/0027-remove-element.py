class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []
        k = len(nums)
        for num in nums:
            if num == val:
                k -= 1
            else:
                answer.append(num)
        for i in range(len(answer)):
            nums[i] = answer[i]
        return k