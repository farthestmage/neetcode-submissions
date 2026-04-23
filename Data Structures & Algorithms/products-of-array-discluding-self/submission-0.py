class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prox=[1]*len(nums)
        for i in range(len(prox)):
            for j in range(len(nums)):
                if i !=j:
                    prox[i]=nums[j]*prox[i]
        return prox        