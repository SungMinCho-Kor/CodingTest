
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix1 = set()
        for val in arr1:
            while val > 0 and val not in prefix1:
                prefix1.add(val)
                val //= 10
        prefix2 = set()
        for val in arr2:
            while val > 0 and val not in prefix2:
                prefix2.add(val)
                val //= 10
        answer_set = prefix1.intersection(prefix2)
        if answer_set:
            return len(str(max(answer_set)))
        return 0