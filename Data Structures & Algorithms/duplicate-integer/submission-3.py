class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1= {}
        for i in nums:
            if i in d1:
                #d1[i] +=1
                return True 
            else:
                d1[i] = 1
        return False
