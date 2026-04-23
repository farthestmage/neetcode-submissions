class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1 ={}
        for i in nums:
            if i not in d1:
                d1[i] = 1
            elif i in d1:
                return True
        return False