class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=0
        for i in range (0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    n+=1
                    break
            if n>=1:
                return True
        return False