'''
num1, num2 오름차순
int m, n


'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        point = m+n - 1
        while point>=0 and n>0 :
            if m == 0:
                nums1[point] = nums2[n-1]
                n-=1
            elif nums1[m-1] >= nums2[n-1]:
                nums1[point], nums1[m-1] = nums1[m-1], nums1[point]
                m-=1
            else:
                nums1[point] = nums2[n-1]
                n-=1
            point -= 1