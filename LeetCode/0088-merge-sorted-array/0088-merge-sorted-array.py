class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer = nums1[:m] + nums2[:n]
        answer.sort()
        for i in range(n+m):
            if i < len(nums1):
                nums1[i] = answer[i]
            else:
                nums1.append(answer[i])